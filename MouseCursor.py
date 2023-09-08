import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy

##########################
wCam, hCam = 640, 480
frameR = 100  # Frame Reduction
smoothening = 5
#########################

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0
clicking = False  # Flag to indicate clicking state
clickHoldMode = False  # Flag to indicate click and hold mode

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()  # width and height of screen

while True:
    # 1. Find hand Landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    # 2. Get the tip of the index and middle fingers
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]  # Tip of the index finger (x1,y1)
        x2, y2 = lmList[12][1:]  # Tip of the Middle finger (x2,y2)
        print(x1, y1, x2, y2)

    # 3. Check which fingers are up
    fingers = detector.fingersUp()

    # Defining a rectangle for better hand detection
    cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)

    # 4. Click and Hold Mode: Both Index and Middle fingers are up and than take middle finger down
    if fingers[1] == 1 and fingers[2] == 1:
        # 9. Find distance between fingers
        length, img, lineInfo = detector.findDistance(8, 12, img)
        # 10. Click and hold the mouse if distance is short
        if length < 40:
            cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
            if not clickHoldMode:
                clickHoldMode = True
                autopy.mouse.toggle(down=True)  # Press and hold the left

    # 5. Clicking Mode: Only Index Finger is up and close to the thumb
    elif fingers[1] == 1 and fingers[2] == 0:

        length, img, _ = detector.findDistance(4, 8, img)

        # 13. Click mouse if distance is short
        if length < 30:
            if not clicking:
                clicking = True
                autopy.mouse.click()  # Press and hold the left mouse button
        elif clicking:
            clicking = False
            autopy.mouse.click()  # Release the left mouse button

        # 14. Move Mouse
        x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
        y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
        clocX = plocX + (x3 - plocX) / smoothening
        clocY = plocY + (y3 - plocY) / smoothening

        autopy.mouse.move(wScr - clocX, clocY)
        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        plocX, plocY = clocX, clocY

    # 6. Moving Mode: Only Index Finger is up and the middle finger is down
    elif fingers[1] == 1 and fingers[2] == 1:
        # 16. Move Mouse
        x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
        y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
        clocX = plocX + (x3 - plocX) / smoothening
        clocY = plocY + (y3 - plocY) / smoothening
        autopy.mouse.move(wScr - clocX, clocY)
        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        plocX, plocY = clocX, clocY

    # 7. Release the left mouse button if no fingers are up
    else:
        clicking = False
        clickHoldMode = False
        autopy.mouse.toggle(down=False)  # Release the left mouse button

    # 8. Frame Rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)

    # 9. Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)
