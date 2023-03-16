import cv2
import numpy as np
import time
import PoseModule as pm
import math
N = 0
# h = 0
r = 0
theta = 0
setp = []
points = []

#path = r'C:\Users\KennyTruong\Documents\GitHub\Workout_Trainer\data\bicep_curl.mp4'

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
    results = detector.pose.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    image_height, image_width = 900, 1200

    if results.pose_landmarks:
        detector.mpDraw.draw_landmarks(img, results.pose_landmarks, detector.mpPose.POSE_CONNECTIONS)
        for ids, lm in enumerate(results.pose_landmarks.landmark):
            cx, cy = lm.x * image_width, lm.y * image_height
            #print(ids, cx, cy)
            setp.append([cx, cy])

    if bool(setp):
        # h = setp[16][1] - setp[12][1]
        abx = setp[14][0] - setp[12][0]
        aby = setp[14][1] - setp[12][1]
        acx = setp[24][0] - setp[12][0]
        acy = setp[24][1] - setp[12][1]
        theta = math.acos((abx*acx + aby*acy)/((math.sqrt(abx**2 + aby**2))*(math.sqrt(acx**2 + acy**2))))
        #print(h)

    if theta < math.pi/4:
        theta1 = theta
    if theta > 3*math.pi/4:
        if theta1 < math.pi/4:
            N = N + 1
            theta1 = theta

    # if h > 0:
    #     h1 = h
    # if h < 0:
    #     if h1 > 0:
    #         N = N+1
    #         h1 = h

    # TO RESET THE COUNTER
    if bool(setp):
        r = math.sqrt((setp[12][0] - setp[19][0]) ** 2 + (setp[12][1] - setp[19][1]) ** 2)
    if r < 20:
        N = 0

    print(N)
    cv2.putText(img, str("Jumping Jack Count"), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 3)
    cv2.putText(img, str(int(N)), (150, 250), cv2.FONT_HERSHEY_PLAIN, 10, (0, 255, 0), 4)
    setp.clear()

    cv2.imshow("Jumping Jack", img)
    #cv2.waitKey(1)
    if cv2.waitKey(1) == 27:  # ESC key
        break

cv2.destroyAllWindows()
cap.release()


