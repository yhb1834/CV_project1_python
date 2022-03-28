import cv2

first_img = cv2.imread("venv/1st.jpg")
second_img = cv2.imread("venv/2nd.jpg")

cv2.namedWindow('First Image', cv2.WINDOW_NORMAL)
cv2.moveWindow('First Image', 200, 200)
cv2.resizeWindow('First Image', 550, 400)

cv2.namedWindow('Second Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Second Image', 550, 400)

cv2.imshow("First Image", first_img)
cv2.imshow("Second Image", second_img)

key = cv2.waitKey(0)
cv2.destroyAllWindows()
