import cv2

img = cv2.imread("test.jpg")

# 밝게 만들기 (모든 픽셀에 값 더하기)
brighter = cv2.add(img, 60)
cv2.imwrite("test_brighter.jpg", brighter)

# 어둡게 만들기 (모든 픽셀에 값 빼기)
darker = cv2.subtract(img, 60)
cv2.imwrite("test_darker.jpg", darker)