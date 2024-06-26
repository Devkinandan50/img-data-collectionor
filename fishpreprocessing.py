import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import os
import math

offset = 20
imgSize = 300
folder = "Data/A"
counter = 0

DIR = 'D:\Project\ML\datasetoffish\Fish_Dataset\Fish_Dataset'
classes = [i for i in os.listdir(DIR) if '.' not in i]
classes


detector = HandDetector(maxHands=1)


folder ="D:\Project\ML\datasetoffish\Fish_Dataset\Fish_Dataset\Black Sea Sprat\Black Sea Sprat"
image_files = os.listdir(folder)

for image_file in image_files:
    img = cv2.imread(os.path.join(folder, image_file))

    hands, img = detector.findHands(img)
    img = cv2.flip(img, 1)

    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]
        imgCropShape = imgCrop.shape

        aspectRatio = h / w

        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize - wCal) / 2)
            imgWhite[:, wGap:wCal + wGap] = imgResize

        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - hCal) / 2)
            imgWhite[hGap:hCal + hGap, :] = imgResize

        cv2.imshow("ImageCrop", imgCrop)
        cv2.imshow("ImageWhite", imgWhite)

    cv2.imshow("Image", img)
    key = cv2.waitKey(0)
    

    # if key == ord("s"):
    #     counter += 1
    #     cv2.imwrite(f'{folder}/Image_{time.time()}.jpg', imgWhite)
    #     print(counter)

# Close all windows
cv2.destroyAllWindows()
