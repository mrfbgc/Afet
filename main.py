import time

import cv2
import pickle
import cvzone
import numpy as np

# Video feed
cap = cv2.VideoCapture(3)

with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)

width, height = 128, 115

def giveOutput(room_id):
    general_electric = 8 * 0.04 * 1.89
    para = 0.04 * 1.89
    if room_id==1:
        print("|---------------------|" + "\t|-------------------|")
        print("Light 5 and 6 are on %100." + "\t Consumption without project: ")
        print("Light 3, 4, 7, 8 are on %25." + "\t Consumption with project: ")
        print("Others are off." + "\t Saving Money: ",general_electric-3*para," TL")
        print("|---------------------|" + "\t|-------------------|")
    if room_id==2:
        print("|---------------------|" + "\t|-------------------|")
        print("Light 7 and 8 are on %100." + "\t Consumption without project: ")
        print("Light 5 and 6 are on %50." + "\t Consumption with project: ")
        print("Others are off." + "\t Saving Money: ",general_electric-2.5*para," TL")
        print("|---------------------|" + "\t|-------------------|")
    if room_id==3:
        print("|---------------------|" + "\t|-------------------|")
        print("Light 7 and 8 are on %100." + "\t Consumption without project: ")
        print("Light 5 and 6 are on %50." + "\t Consumption with project: ")
        print("Others are off." + "\t Saving Money: ",general_electric-2.5*para," TL")
        print("|---------------------|" + "\t|-------------------|")
    if room_id==4:
        print("|---------------------|" + "\t|-------------------|")
        print("Light 7 and 8 are on %100." + "\t Consumption without project: ")
        print("Light 5 and 6 are on %50." + "\t Consumption with project: ")
        print("Others are off." + "\t Saving Money: ",general_electric-2.5*para," TL")
        print("|---------------------|" + "\t|-------------------|")
    if room_id==5:
        print("|---------------------|" + "\t|-------------------|")
        print("Light 7 is on %100." + "\t Consumption without project: ")
        print("Light 5, 6 and 8 are on %50." + "\t Consumption with project: ")
        print("Others are off." + "\t Saving Money: ",general_electric-1.75*para," TL")
        print("|---------------------|" + "\t|-------------------|")
    if room_id==6:
        print("|---------------------|" + "\t|-------------------|")
        print("Light 7 and 8 are on %100." + "\t Consumption without project: ")
        print("Light 5 and 6 are on %50." + "\t Consumption with project: ")
        print("Others are off." + "\t Saving Money: ",general_electric-2.5*para," TL")
        print("|---------------------|" + "\t|-------------------|")
    if room_id==7:
        print("|---------------------|" + "\t|-------------------|")
        print("Light 4 and 6 are on %100." + "\t Consumption without project: ")
        print("Light 3 and 5 are on %25." + "\t Consumption with project: ")
        print("Others are off." + "\t Saving Money: ",general_electric-2.5*para," TL")
        print("|---------------------|" + "\t|-------------------|")
    if room_id==8:
        print("|---------------------|" + "\t|-------------------|")
        print("Light 4 and 6 are on %100." + "\t Consumption without project: ")
        print("Light 3 and 5 are on %25." + "\t Consumption with project: ")
        print("Others are off." + "\t Saving Money: ",general_electric-2.5*para," TL")
        print("|---------------------|" + "\t|-------------------|")
    if room_id==9:
        print("|---------------------|" + "\t|-------------------|")
        print("Light 4 is on %100." + "\t Consumption without project: ")
        print("Light 2, 3 and 6 are on %25." + "\t Consumption with project: ")
        print("Others are off." + "\t Saving Money: ",general_electric-2.75*para," TL")
        print("|---------------------|" + "\t|-------------------|")
    if room_id==10:
        print("|---------------------|" + "\t|-------------------|")
        print("Light 2 is on %100." + "\t Consumption without project: ")
        print("Light 1, 3 and 4 are on %25." + "\t Consumption with project: ")
        print("Others are off." + "\t Saving Money: ",general_electric-1.75*para," TL")
        print("|---------------------|" + "\t|-------------------|")
    if room_id==11:
        print("|---------------------|" + "\t|-------------------|")
        print("Light 2 is on %100." + "\t Consumption without project: ")
        print("Light 1, 3 and 4 are on %25." + "\t Consumption with project: ")
        print("Others are off." + "\t Saving Money: ",general_electric-1.75*para," TL")
        print("|---------------------|" + "\t|-------------------|")
    if room_id==12:
        print("|---------------------|" + "\t|-------------------|")
        print("Light 4 is on %100." + "\t Consumption without project: ")
        print("Light 2, 3 and 6 are on %25." + "\t Consumption with project: ")
        print("Others are off." + "\t Saving Money: ",general_electric-1.75*para," TL")
        print("|---------------------|" + "\t|-------------------|")
    if room_id==13:
        print("|---------------------|" + "\t|-------------------|")
        print("Light 3 is on %100." + "\t Consumption without project: ")
        print("Light 1, 4 and 5 are on %25." + "\t Consumption with project: ")
        print("Others are off." + "\t Saving Money: ",general_electric-1.75*para," TL")
        print("|---------------------|" + "\t|-------------------|")
    if room_id==14:
        print("|---------------------|" + "\t|-------------------|")
        print("Light 5 is on %100." + "\t Consumption without project: ")
        print("Light 3, 6 and 7 are on %25." + "\t Consumption with project: ")
        print("Others are off." + "\t Saving Money: ",general_electric-1.75*para," TL")
        print("|---------------------|" + "\t|-------------------|")


def checkParkingSpace(imgPro):
    spaceCounter = 0

    for pos in posList:
        x, y = pos

        imgCrop = imgPro[y:y + height, x:x + width]
        # cv2.imshow(str(x * y), imgCrop)
        count = cv2.countNonZero(imgCrop)


        if count < 2000:
            color = (0, 0, 255)
            thickness = 5
            spaceCounter += 1
        else:
            color = (0, 255, 0)
            thickness = 2
            giveOutput(posList.index(pos))



        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
        cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1,
                           thickness=2, offset=0, colorR=color)

    cvzone.putTextRect(img, f'Opened Lamb: {len(posList)-spaceCounter}/{len(posList)}', (100, 50), scale=2,
                           thickness=2, offset=20, colorR=(0,200,0))



while True:

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    checkParkingSpace(imgDilate)
    cv2.imshow("Image", img)
    #cv2.imshow("ImageBlur", imgBlur)
    cv2.imshow("ImageThres", imgMedian)
    cv2.waitKey(10)