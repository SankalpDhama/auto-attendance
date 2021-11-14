import cv2 as cv
import os
from face_recognition.api import face_distance, face_encodings
import numpy as np
import face_recognition
from datetime import datetime   

images=[]
classNames=[]
path='D:\python\opencv\photos'
mylist=os.listdir(path)

print(mylist)

for cl in mylist:
    curImg=cv.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findencodings(images):
    encodelist=[]
    for img in images:
        img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return(encodelist)

def markAttendance(name):
    with open('D:\python\attendance\attendance.xlsx','r+') as f:
        myDataList=f.readlines()
        nameList=[]
        print(myDataList)
        for line in myDataList:
            entry=line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now=datetime.now()
            dtString=now.strftime('%H:%M:%S')
            

markAttendance('a')

encodelistknown=findencodings(images)

print(len(encodelistknown))

cap=cv.VideoCapture(0)

while True:
    success,img=cap.read()
    imgS =cv.resize(img,(0,0,None,0.25,0.25)
    imgS = cv.cvtColor(img,cv.COLOR_BGR2RGB)

    faceCurFrame=face_recognition.face_locations(imgS)
    encodeCurFrame=face_recognition.face_encodings(imgS,FaceCurFrame)

    for encodeFace,faceloc in zip(encodesCurFrame,faceCurFrame):
        matches=face_recognition.compare_faces(encodelistknown,encodeface)
        faceDis=face_recognition.face_distance(encodelistknown,encodeface)
        print(faceDis)
        matchIndex=np.argmin(faceDis)

        if matches[matchIndex]:
            name=classNames[matchIndex].upper()
            print(name)
            y1,x2,y1,x1=faceloc
            y1,x2,y1,x1=y1*4,x2*4,y1*4,x1*4
            cv.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv.FILLED)
            cv.putText(img,name,(x1+6,y2-6),cv.cv.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)


    cv.imshow('webcam',img)
    cv.waitKey(0)
