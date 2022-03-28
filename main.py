import cv2
import numpy as np

patch_size = 5

first_points_x = []
first_points_y = []
second_points_x = []
second_points_y = []

first_img = cv2.imread("venv/1st.jpg")
second_img = cv2.imread("venv/2nd.jpg")

cv2.namedWindow('First Image', cv2.WINDOW_NORMAL)
cv2.moveWindow('First Image', 200, 200)
cv2.resizeWindow('First Image', 550, 400)
cv2.namedWindow('Second Image', cv2.WINDOW_NORMAL)
cv2.moveWindow('Second Image', 600, 200)
cv2.resizeWindow('Second Image', 550, 400)

cv2.imshow("First Image", first_img)
cv2.imshow("Second Image", second_img)


def draw_rec(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        first_points_x.append(x)
        first_points_y.append(y)
        cv2.rectangle(first_img, (x, y), (patch_size, patch_size), (255, 0, 0), 3)
        print(first_points_x, first_points_y)


def draw_rec2(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        second_points_x.append(x)
        second_points_y.append(y)
        cv2.rectangle(second_img, (x, y), (patch_size, patch_size), (255, 0, 0), 3)
        print(second_points_x, second_points_y)


cv2.setMouseCallback('First Image', draw_rec)
cv2.setMouseCallback('Second Image', draw_rec2)

key = cv2.waitKey(0)
cv2.destroyAllWindows()
