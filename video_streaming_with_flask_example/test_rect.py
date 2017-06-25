import numpy as np
    2 import cv2
    3 
    4 cap = cv2.VideoCapture(0)
    5 
    6 while(True):
    7     # Capture frame-by-frame
    8     ret, frame = cap.read()
    9 
   10     # Our operations on the frame come here
   11     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   12 
   13     # Display the resulting frame
   14     cv2.imshow('frame',gray)
   15     if cv2.waitKey(1) & 0xFF == ord('q'):
   16         break
   17 
   18 # When everything done, release the capture
   19 cap.release()
   20 cv2.destroyAllWindows()