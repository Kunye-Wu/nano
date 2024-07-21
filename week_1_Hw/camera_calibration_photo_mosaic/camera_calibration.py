import numpy as np
import cv2
import glob
import matplotlib.pyplot as plt

# Define checkerboard_dims as (9, 6) 
checkerboard_dims = [9, 6]

# Create objp as a zero array of shape (number of corners, 3), float32
objp = np.zeros((54, 3), dtype=np.float32)

# Set the first two columns of objp to the coordinate grid of corners
objp[:,:2] = np.mgrid[0:checkerboard_dims[0],0:checkerboard_dims[1]].T.reshape(-1,2)
print(objp)

# Initialize objpoints as an empty list
objpoints = []
# Initialize imgpoints as an empty list
imgpoints = []

# Load all checkerboard images using glob ('path/to/images/*.jpg')
checkerboard_images = glob.glob('calibration photos resized/*.jpg')
print(checkerboard_images)
# For each image in images:
for image in checkerboard_images:
    img = cv2.imread(image)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print("hi")
#     Read the image
#     Convert the image to grayscale
    
#     Find the chessboard corners in the grayscale image
    ret, corners = cv2.findChessboardCorners(img_gray, checkerboard_dims, None)
    print('he')
    if ret:
        objpoints.append(objp)
        corner_refined = cv2.cornerSubPix(img_gray, corners)
        imgpoints.append(corners)
        drawn = cv2.drawChessboardCorners(img, checkerboard_dims, corner_refined, ret)
        plt.imshow(drawn)
#     If corners are found:
#         Append objp to objpoints
#         Refine corner positions using cornerSubPix
#         Append refined corners to imgpoints
        
#         Optionally, draw chessboard corners on the image
#         Optionally, display the image with drawn corners
#         Wait for a short period
    
# Destroy all OpenCV windows
cv2.destroyAllWindows()
# Calibrate the camera using calibrateCamera with objpoints, imgpoints, and image size
# Get the camera matrix, distortion coefficients, rotation vectors, and translation vectors
ret, matrix, distortion, rot, tran = cv2.calibrateCamera(objpoints, imgpoints, (756, 1008), None, None)

# Save the calibration results (camera matrix, distortion coefficients) to a file. 
# A common and convenient format for storing camera calibration data is the NumPy .npz file format,
#     which allows you to store multiple NumPy arrays in a single compressed file.
np.save("matrix", matrix)
np.save("distortion", distortion)

# Verify the calibration:
#     Initialize mean_error to 0
#     For each pair of object points and image points:
#         Project the object points to image points using projectPoints
#         Compute the error between the projected and actual image points
#         Accumulate the error
#     Compute the average error
#     Print the total average error
error_totals = np.array({})
for o in objpoints:
    for i in imgpoints:
        points = cv2.projectPoints(objpoints, rot, tran, matrix)
        error = abs(i, points)
        np.append(error_totals, error)
print(np.mean(error_totals))

