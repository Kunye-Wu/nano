import numpy as np
import cv2


# markerCorners, markerIds, rejectedCandidates = detector.detectMarkers(frame)

# LOAD CORRECT TAG DICTIONARY
arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_APRILTAG_16H5)
SIZE = 500 # pixels

# CREATE ARRAY FOR MARKER
marker = np.zeros((SIZE, SIZE, 1), dtype=np.uint8)

# DRAW AND SAVE MARKER
ID = 23
cv2.aruco.drawMarker(arucoDict, ID, SIZE, marker, 1)
cv2.imwrite('DICT_APRILTAG_16H5_id_{}_{}.png'.format(ID, SIZE), marker)
