import video_streaming_with_flask_example/main

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  python main.py

if __name__ == '__main__':
  app.run()
