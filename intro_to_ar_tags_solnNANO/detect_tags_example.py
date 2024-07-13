import cv2
import numpy as np

# LOAD IMAGE AND TAG DICTIONARY
tags = cv2.imread('data/two_tags_APRILTAG_16H5.png')
arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_APRILTAG_16H5)

# DETECT TAGS IN IMAGE
corners, ids, rejects = cv2.aruco.detectMarkers(cv2.cvtColor(tags, cv2.COLOR_BGR2GRAY), arucoDict)
# print(corners)
# print(corners[0][0])
min_distance = 10000000
for tag1 in corners[0][0]:
    for tag2 in corners[1][0]:
        dist = np.sqrt(((tag1[0] - tag2[0])**2) + ((tag1[1] - tag2[1])**2))
        if dist < min_distance:
            min_distance = dist
        # print(tag1, tag2)

print("minimum distance between tag corners:", min_distance / 500 * 3)

# DRAW DETECTION AND SAVE FILE
# detection = cv2.aruco.drawDetectedMarkers(tags, corners, borderColor=(255, 0, 0))

# cv2.imwrite('detection_two_tags_APRILTAG_16H5.png', detection)

