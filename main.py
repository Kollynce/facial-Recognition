import cv2

# this is to read the image
img = cv2.imread("people.jpeg", 0)

# this resize the image to the dimensions that the user has specified
# resized = cv2.resize(img, (1200, 600))

# resizing the image to be half of the original image
resized = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))

# THIS WILL BE ABLE TO SHOW THE IMAGE
cv2.imshow("group", resized)

# this is a timer of the image how long it will last displayed on the screen
cv2.waitKey(0)

cv2.destroyAllWindows()
