import cv2
import numpy as np
import glob

# Load Calibration Parameters:
#     Function load_calibration(calibration_file):
#         Load calibration data from the file
#         Extract camera matrix and distortion coefficients
#         Return camera matrix and distortion coefficients
checkerboard_dims = [8, 3]
def load_calibration():
    objpoints = []
    imgpoints = []
    checkerboard_images = glob.glob('calibration photos resized/*.jpg')
    for image in checkerboard_images:
        img = cv2.imread(image)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        print("hi")
        ret, corners = cv2.findChessboardCorners(img_gray, checkerboard_dims, None)
        print('he')
        if ret:
            objpoints.append(objp)
            corner_refined = cv2.cornerSubPix(img_gray, corners)
            imgpoints.append(corners)
            drawn = cv2.drawChessboardCorners(img, checkerboard_dims, corner_refined, ret)
    ret, matrix, distortion, rot, tran = cv2.calibrateCamera(objpoints, imgpoints, (756, 1008), None, None)
    return matrix, distortion


# Undistort Image:
#     Function undistort_image(image, camera_matrix, dist_coeffs):
#         Get image dimensions (height, width)
#         Compute new camera matrix for undistortion
#         Undistort the image (use cv2 undistort)
#         Crop the undistorted image using ROI
#         Return undistorted image
def undistort_image(image, camera_matrix, dist_coeffs):
    height, width = np.shape(image)
    new_camera_matrix, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, dist_coeffs, (width,height), 1, (width,height))
    undistorted_image = cv2.undistort(image, camera_matrix, dist_coeffs, None, new_camera_matrix)
    x, y, w, h = roi
    undistorted_image = undistorted_image[y:y+h, x:x+w]
    return undistorted_image


# Harris Corner Detection:
#     Function harris_corner_detection(image):
#         Convert the image to grayscale
#         Apply Harris corner detection
#         Dilate corners
#         Mark corners on the image
#         Return image with marked corners and detected corners
def harris_corner_detection(image):
    image = cv2.cvtColor(image, cv2.BGR2GRAY)
    dst = cv2.cornerHarris(image, 2, 3, 0.04)
    dst = cv2.dilate(dst, None)
    image[dst > 0.01 * dst.max()] = [0, 0, 255]
    return image

# Match Features Between Images:
#     Function match_features(image1, image2):
#         Detect keypoints and descriptors in image1 using SIFT
#         Detect keypoints and descriptors in image2 using SIFT
#         Match descriptors using brute-force matcher
#         Extract matched points from both images
#         Return matched points from image1 and image2
def match_features(image1, image2):
    sift = cv2.SIFT_create()
    kp1, desc1 = sift.detectAndCompute(image1, None)
    kp2, desc2 = sift.detectAndCompute(image2, None)
    
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(desc1, desc2, k=2)
    
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)
    
    matched_points_image1 = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    matched_points_image2 = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    
    return matched_points_image1, matched_points_image2

# Create Mosaic:
#     Function create_mosaic(images, camera_matrix, dist_coeffs):
#         Undistort all images using undistort_image function
#         Initialize mosaic with the first undistorted image
#         For each subsequent undistorted image:
#             Detect Harris corners in both mosaic and current image using harris_corner_detection
#             Match features between mosaic and current image using match_features
#             Estimate homography using matched points
#             Warp mosaic image using the estimated homography
#             Blend current image into mosaic
#         Return final mosaic image
def create_mosaic(images, camera_matrix, dist_coeffs):
    undistorted_images = [undistort_image(img, camera_matrix, dist_coeffs) for img in images]
    
    mosaic = undistorted_images[0].copy()
    for i in range(1, len(undistorted_images)):
        current_image = undistorted_images[i]
        
        mosaic_corners = harris_corner_detection(mosaic.copy())
        current_corners = harris_corner_detection(current_image.copy())
        
        matched_points_mosaic, matched_points_current = match_features(mosaic, current_image)
        
        H, _ = cv2.findHomography(matched_points_current, matched_points_mosaic, cv2.RANSAC)
        
        warped_image = cv2.warpPerspective(current_image, H, (mosaic.shape[1], mosaic.shape[0]))
        
        mask = np.where(warped_image != 0, 1, 0).astype(np.uint8)
        mosaic = mosaic * (1 - mask) + warped_image
        
    return mosaic


# Main:
#     Load camera matrix and distortion coefficients from calibration file
#     Load images from specified directory
#     Create mosaic using create_mosaic function
#     Save the mosaic image to a file
if __name__ == '__main__':
    camera_matrix, dist_coeffs = load_calibration()
    images = glob.glob("Latin Student Center/*.jpg")
    images = [cv2.imread(img) for img in images]
    
    mosaic_image = create_mosaic(images, camera_matrix, dist_coeffs)


# Display the mosaic image
cv2.imshow('Mosaic', mosaic_image)
cv2.waitKey(0)
cv2.destroyAllWindows()