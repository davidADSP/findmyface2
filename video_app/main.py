import numpy as np
import cv2
import logging
import httplib, urllib
import json

import cognitive_face as CF

import base64




def get_attributes(image,conn, headers, params):
    
    # The URL of a JPEG image to analyze.
    # body = "{'url':'https://upload.wikimedia.org/wikipedia/commons/c/c3/RH_Louise_Lillian_Gish.jpg'}"
    # body = image
    try:
        # Execute the REST API call and get the response.
        
        conn.request("POST", "/face/v1.0/detect?%s" % params, image, headers)
        response = conn.getresponse()
        data = response.read()
        
        # 'data' contains the JSON data. The following formats the JSON data for display.
        parsed = json.loads(data)
        print(data)
        #json_out = json.dumps(parsed, sort_keys=True, indent=2)
        return parsed
    #conn.close()
    
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


KEY = '77abe08c92574606aa8aa15b3c987e7f'  # Replace with a valid Subscription Key here.
CF.Key.set(KEY)

BASE_URL = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)


logger = logging.getLogger()
hdlr = logging.FileHandler('./log.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.ERROR)

#cap = cv2.VideoCapture('./times.mp4') #use this line for the video
cap = cv2.VideoCapture() #use this line for the webcam
cv2.namedWindow("preview",cv2.WND_PROP_FULLSCREEN)

conn = httplib.HTTPSConnection('westeurope.api.cognitive.microsoft.com')

###############################################
#### Update or verify the following values. ###
###############################################

# Replace the subscription_key string value with your valid subscription key.
subscription_key = '77abe08c92574606aa8aa15b3c987e7f'

# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your subscription keys.
# For example, if you obtained your subscription keys from the westus region, replace 
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
# a free trial subscription key, you should not need to change this region.
uri_base = 'https://westeurope.api.cognitive.microsoft.com'

# Request headers.
headers = {
'Content-type': 'application/octet-stream',
    #'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

# Request parameters.
params = urllib.urlencode({
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    #'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    'returnFaceAttributes': '',

})

while(True):
    # Capture frame-by-frame
    ret, image = cap.read()
    ret, jpeg = cv2.imencode('.jpg', image)
    jpeg_bytes = jpeg.tobytes()



    people_in_frame = get_attributes(jpeg_bytes, conn, headers, params)

    logger.info(people_in_frame)
    
        #cv2.destroyAllWindows()
    if len(people_in_frame) > 0:
        rects = [x['faceRectangle'] for x in people_in_frame]
        coords = [(rect['left'], rect['top'], rect['height'], rect['width']) for rect in rects]

        for rect in rects:
            x,y,h,w = (rect['left'], rect['top'], rect['height'], rect['width'])
            logger.info(str(x) + ' ' + str(y)+ ' ' + str(h) + ' ' + str(w));
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        


        person = {}

        personGroupId = 'users'
        faceIds = [x['faceId'] for x in people_in_frame]
        #logger.info(out)
        #logger.info(faceIds)
        results = CF.face.identify(faceIds, personGroupId);
        #logger.info(results)
        i = 0
        for identifyResult in results :

            print("Result of face: " + identifyResult['faceId']);
            if len(identifyResult['candidates']) == 0:
                print("No one identified");
            else:
                # Get top 1 among all candidates returned
                candidateId = identifyResult['candidates'][0]['personId'];
                person = CF.person.get(personGroupId, candidateId);
                print(person)
                print("Identified as " + person['name']);
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(image,person['name'],(coords[i][0] + coords[i][3],coords[i][1]+ coords[i][2]), font, 1,(0, 255, 0),1,cv2.LINE_AA)
            #cv2.putText(image,'-'.join(json.loads(person['userData'])['skills']),(coords[i][0] ,coords[i][1]-7), font, 0.7,(0, 255, 0),1,cv2.LINE_AA)
                cv2.putText(image,json.loads(person['userData'])['Skills'],(coords[i][0] ,coords[i][1]-7), font, 0.7,(0, 255, 0),1,cv2.LINE_AA)
            i = i + 1

        cv2.imshow("preview", image)

    cv2.waitKey(3000) # add delay (in ms) to not trigger the threshold


# When everything done, release the capture
conn.close()
cap.release()
cv2.destroyAllWindows()
