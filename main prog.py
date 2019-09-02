import cv2
import numpy as np
import datetime

cap = cv2.VideoCapture(0)
hand_cascade = cv2.CascadeClassifier('D:/closed_frontal_palm.xml')
counter = 0

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hands = hand_cascade.detectMultiScale(gray, 1.5, 2)
    contour = hands
    contour = np.array(contour)

    now = datetime.datetime.now()
    time = now.strftime("%Y/%m/%d %H:%M:%S %Z") 
    cv2.putText(img=frame, text="Date & Time : "+time , org=(325,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(0,0,255))

    if counter==0:

        if len(contour)==2:
            cv2.putText(img=frame, text='Your engine started', org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.5,
                        color=(0, 255, 0))
            for (x, y, w, h) in hands:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (100, 100, 100), 5)

    if counter>0:

        if len(contour)>=2:
            cv2.putText(img=frame, text='You can go as fast as you wish', org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.5,
                        color=(255, 0, 0))
            for (x, y, w, h) in hands:
                cv2.rectangle(frame, (x, y),(x + w ,y + h), (100, 100, 100), 5)

        elif len(contour)==1:
            cv2.putText(img=frame, text='Speed limited to 30km/h', org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.5,
                        color=(0, 255, 0))
            for (x, y, w, h) in hands:
                cv2.rectangle(frame, (x, y),(x + w ,y + h), (100, 100, 100), 5)

        elif len(contour)==0:
            cv2.putText(img=frame, text='Retarding', org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.5,
                        color=(0, 0, 255))

    counter+=1

    cv2.imshow('Driver_frame', frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
