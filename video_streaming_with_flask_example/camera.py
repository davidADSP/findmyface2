import cv2
import logging
import time
from get_face import get_attributes
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
        self.video = cv2.VideoCapture(0)
       
    def __del__(self):
        self.video.release()

    
    
    def get_frame(self):
        personGroupId = 'myfriends'

        success, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)

        #cv2.imwrite("test.jpg", image)

        jpeg_bytes = jpeg.tobytes()
        #gets a list of the faces it's found in the webcam shot
        out = get_attributes(jpeg_bytes)

        if len(out) > 0:
            #logger.info(out[0]['faceAttributes']['emotion']['surprise'])
            logger.info(out)
            faceIds = [x['faceId'] for x in out]
            #logger.info(out)
            logger.info(faceIds)

            results = CF.face.identify(faceIds, personGroupId);

            logger.info(results)
            # for identifyResult in results :
            #     logger.info("Result of face: " + identifyResult['faceId']);
            #     if (identifyResult['Candidates'].Length == 0)
            #     {
            #         Console.WriteLine("No one identified");
            #     }
            #     else
            #     {
            #         // Get top 1 among all candidates returned
            #         var candidateId = identifyResult.Candidates[0].PersonId;
            #         var person = await faceServiceClient.GetPersonAsync(personGroupId, candidateId);
            #         Console.WriteLine("Identified as {0}", person.Name);
            #     }
            


   
        time.sleep(4)
        #send image to API and compare against participants

        return jpeg_bytes