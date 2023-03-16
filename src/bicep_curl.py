import cv2
import numpy as np
import time
import PoseModule as pm
import math


path = r'C:\Users\KennyTruong\Documents\GitHub\Workout_Trainer\data\bicep_curl.mp4'

# Video file
#cap = cv2.VideoCapture(path)

# Webcam
cap = cv2.VideoCapture(0)
 
detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0
while True:
    success, img = cap.read()
    img = cv2.resize(img, (1200, 900))
    #img = cv2.flip(img, 1)
    
    #path = r'C:\Users\KennyTruong\Documents\GitHub\Workout_Trainer\data\dips_workout.JPG'
    #img = cv2.imread(path)
    img = detector.findPose(img)
    lmList = detector.findPosition(img, False)
    if len(lmList) != 0:
        # Right Arm 
        armAngle = detector.findAngle(img, 12, 14, 16)
        
        # Left Arm
        #armAngle = detector.findAngle(img, 11, 13, 15)
        #per_l = np.interp(armAngle_l, (210, 310), (0, 100))
        #bar_l = np.interp(armAngle_l, (220, 310), (650, 100))
        per = np.interp(armAngle, (210, 310), (0, 100))
        bar = np.interp(armAngle, (220, 310), (650, 100))
        print(armAngle, per)
 
        # Check for the dumbbell curls
        color = (255, 0, 255)
        if per == 100:
            color = (0, 255, 0)
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            color = (0, 255, 0)
            if dir == 1:
                count += 0.5
                dir = 0
        #print(count)
    

        # Draw Bar
        #avgBar = (bar_r + bar_l) / 2
        #avgPer = (per_r + per_l) / 2
        cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
        cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
        cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                    color, 4)
 
        # Draw Curl Count
        cv2.rectangle(img, (0, 525), (200, 720), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 10,
                    (255, 0, 0), 10)
 
    # cTime = time.time()
    # fps = 1 / (cTime - pTime)
    # pTime = cTime
    cv2.putText(img, "Bicep Curls", (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
                (255, 0, 0), 3)
    

    cv2.imshow("Bicep Curl", img)
    #cv2.waitKey(1)
    if cv2.waitKey(1) == 27:  # ESC key
        break

cv2.destroyAllWindows()
cap.release()


