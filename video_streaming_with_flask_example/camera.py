import cv2
import logging
import time

import cognitive_face as CF

logger = logging.getLogger()
hdlr = logging.FileHandler('./log.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.DEBUG)

KEY = '77abe08c92574606aa8aa15b3c987e7f'  # Replace with a valid Subscription Key here.
CF.Key.set(KEY)

BASE_URL = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

class VideoCamera(object):
    def __init__(self):
        cv2.namedWindow("preview", CV_WINDOW_AUTOSIZE)
        self.video = cv2.VideoCapture(0)
        #cv2.waitKey(1);

       
    def __del__(self):
        self.video.release()

    
    
    def get_frame(self):
        

        success, image = self.video.read()

        ret, jpeg = cv2.imencode('.jpg', image)

        #cv2.imwrite("test.jpg", image)

        jpeg_bytes = jpeg.tobytes()
        #gets a list of the faces it's found in the webcam shot

        return {'image':image, 'jpeg_bytes':jpeg_bytes}

    def doAPI(self, image,people_in_frame):

        personGroupId = 'myfriends'
        rects = [x['faceRectangle'] for x in people_in_frame]
        logger.info(rects)
        for rect in rects:
            x, y, h, w = (rect['left'], rect['top'], rect['height'], rect['width'])
            logger.info(str(x) + ' ' + str(y)+ ' ' + str(h) + ' ' + str(w));
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow("preview", image)
        cv2.waitKey(100)


        person = {}

            #cv2.destroyAllWindows()
        if len(people_in_frame) > 0:
            #logger.info(out[0]['faceAttributes']['emotion']['surprise'])
            #logger.info(out)
            faceIds = [x['faceId'] for x in people_in_frame]
            #logger.info(out)
            #logger.info(faceIds)
            results = CF.face.identify(faceIds, personGroupId);
            #logger.info(results)
            for identifyResult in results :
                logger.info("Result of face: " + identifyResult['faceId']);
                if len(identifyResult['candidates']) == 0:
                    logger.info("No one identified");
                else:
                    # Get top 1 among all candidates returned
                    candidateId = identifyResult['candidates'][0]['personId'];
                    #person = CF.person.get(personGroupId, candidateId);
                    logger.info("Identified as " + candidateId);
                
        #time.sleep(1)

        return person
        #send image to API and compare against participants