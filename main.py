import cv2
import numpy as np

draw_size = 80
patch_size = 9

first_points_x = []
first_points_y = []
second_points_x = []
second_points_y = []

roi_1_1 = []
roi_1_2 = []
roi_1_3 = []
roi_1_4 = []

roi_2_1 = []
roi_2_2 = []
roi_2_3 = []
roi_2_4 = []

gx_1_1 = 0
gx_1_2 = 0
gx_1_3 = 0
gx_1_4 = 0
gy_1_1 = 0
gy_1_2 = 0
gy_1_3 = 0
gy_1_4 = 0

gx_2_1 = 0
gx_2_2 = 0
gx_2_3 = 0
gx_2_4 = 0
gy_2_1 = 0
gy_2_2 = 0
gy_2_3 = 0
gy_2_4 = 0

mag_1_1 = 0
mag_1_2 = 0
mag_1_3 = 0
mag_1_4 = 0
mag_2_1 = 0
mag_2_2 = 0
mag_2_3 = 0
mag_2_4 = 0

angle_1_1 = 0
angle_1_2 = 0
angle_1_3 = 0
angle_1_4 = 0
angle_2_1 = 0
angle_2_2 = 0
angle_2_3 = 0
angle_2_4 = 0



first_img = cv2.imread("venv/1st.jpg")
second_img = cv2.imread("venv/2nd.jpg")

cv2.namedWindow('First Image', cv2.WINDOW_NORMAL)
cv2.moveWindow('First Image', 200, 200)
cv2.resizeWindow('First Image', 600, 600)
cv2.namedWindow('Second Image', cv2.WINDOW_NORMAL)
cv2.moveWindow('Second Image', 800, 200)
cv2.resizeWindow('Second Image', 600, 600)


def draw_rec(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        first_points_x.append(x)
        first_points_y.append(y)
        cv2.rectangle(first_img, (x, y, draw_size, draw_size), (255, 0, 0), 3)
        print(first_points_x, first_points_y)


def draw_rec2(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        second_points_x.append(x)
        second_points_y.append(y)
        cv2.rectangle(second_img, (x, y, draw_size, draw_size), (255, 0, 0), 3)
        print(second_points_x, second_points_y)


cv2.setMouseCallback('First Image', draw_rec)
cv2.setMouseCallback('Second Image', draw_rec2)


def roi():
    global roi_1_1, roi_1_2, roi_1_3, roi_1_4
    global roi_2_1, roi_2_2, roi_2_3, roi_2_4
    roi_1_1 = first_img[first_points_y[0]:first_points_y[0] + patch_size,
              first_points_x[0]:first_points_x[0] + patch_size]
    roi_1_2 = first_img[first_points_y[1]:first_points_y[1] + patch_size,
              first_points_x[1]:first_points_x[1] + patch_size]
    roi_1_3 = first_img[first_points_y[2]:first_points_y[2] + patch_size,
              first_points_x[2]:first_points_x[2] + patch_size]
    roi_1_4 = first_img[first_points_y[3]:first_points_y[3] + patch_size,
              first_points_x[3]:first_points_x[3] + patch_size]

    roi_2_1 = first_img[second_points_y[0]:second_points_y[0] + patch_size,
              second_points_x[0]:second_points_x[0] + patch_size]
    roi_2_2 = first_img[first_points_y[1]:first_points_y[1] + patch_size,
              first_points_x[1]:first_points_x[1] + patch_size]
    roi_2_3 = first_img[first_points_y[2]:first_points_y[2] + patch_size,
              first_points_x[2]:first_points_x[2] + patch_size]
    roi_2_4 = first_img[first_points_y[3]:first_points_y[3] + patch_size,
              first_points_x[3]:first_points_x[3] + patch_size]


# cv2.namedWindow('First Image', cv2.WINDOW_NORMAL)
# rects = cv2.selectROI('First Image', first_img, False, True)
# for r in rects:
#    cv2.rectangle(first_img, (r[0], r[1]), (r[0]+r[2], r[1]+r[3]), 255)

def calculate_gradient(img):
    gx = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=1)
    gy = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=1)
    return gx, gy

def Gradient():
    global gx_1_1, gx_1_2, gx_1_3, gx_1_4, gy_1_1, gy_1_2, gy_1_3, gy_1_4
    global gx_2_1, gx_2_2, gx_2_3, gx_2_4, gy_2_1, gy_2_2, gy_2_3, gy_2_4
    gx_1_1, gy_1_1 = calculate_gradient(roi_1_1)
    gx_1_2, gy_1_2 = calculate_gradient(roi_1_2)
    gx_1_3, gy_1_3 = calculate_gradient(roi_1_3)
    gx_1_4, gy_1_4 = calculate_gradient(roi_1_4)

    gx_2_1, gy_2_1 = calculate_gradient(roi_2_1)
    gx_2_2, gy_2_2 = calculate_gradient(roi_2_2)
    gx_2_3, gy_2_3 = calculate_gradient(roi_2_3)
    gx_2_4, gy_2_4 = calculate_gradient(roi_2_4)

def mag_angle():
    #Calculate Gradient magnitude and direction in degrees
    global mag_1_1, mag_1_2, mag_1_3, mag_1_4, mag_2_1, mag_2_2, mag_2_3, mag_2_4
    global angle_1_1, angle_1_2, angle_1_3, angle_1_4, angle_2_1, angle_2_2, angle_2_3, angle_2_4
    mag_1_1, angle_1_1 = cv2.cartToPolar(gx_1_1, gy_1_1, angleInDegrees=True)
    mag_1_2, angle_1_2 = cv2.cartToPolar(gx_1_2, gy_1_2, angleInDegrees=True)
    mag_1_3, angle_1_3 = cv2.cartToPolar(gx_1_3, gy_1_3, angleInDegrees=True)
    mag_1_4, angle_1_4 = cv2.cartToPolar(gx_1_4, gy_1_4, angleInDegrees=True)
    mag_2_1, angle_2_1 = cv2.cartToPolar(gx_2_1, gy_2_1, angleInDegrees=True)
    mag_2_2, angle_2_2 = cv2.cartToPolar(gx_2_2, gy_2_2, angleInDegrees=True)
    mag_2_3, angle_2_3 = cv2.cartToPolar(gx_2_3, gy_2_3, angleInDegrees=True)
    mag_2_4, angle_2_4 = cv2.cartToPolar(gx_2_4, gy_2_4, angleInDegrees=True)

def main():
    while (True):
        cv2.imshow("First Image", first_img)
        cv2.imshow("Second Image", second_img)

        key = cv2.waitKey(1)
        if key == 27:
            break
    cv2.destroyAllWindows()
    roi()

    Gradient()

    mag_angle()



main()
