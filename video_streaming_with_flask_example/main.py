#!/usr/bin/env python

from flask import Flask, render_template, Response
from camera import VideoCamera
from get_face import get_attributes
import logging

#from test_rect import VideoCamera

logger = logging.getLogger()
hdlr = logging.FileHandler('./log.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.DEBUG)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        dict_out = camera.get_frame()

        frame = dict_out['jpeg_bytes']
        image = dict_out['image']

        people_in_frame = get_attributes(frame)
        logger.info(people_in_frame)

        matched_people = camera.doAPI(image,people_in_frame)
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/suggestions')
def suggestions():
    suggestions_list = [{'page':1},{'page':2},{'page':3}]
    return render_template('suggestions.html', suggestions=suggestions_list)



if __name__ == '__main__':
    app.run(host='0.0.0.0')