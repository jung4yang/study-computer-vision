import cv2

img = cv2.imread("test.jpg")
print("원본 크기: ", img.shape)

# 1) 크기 줄이기 (가로 300, 세로 200으로)
resized = cv2.resize(img, (300,200))
cv2.imwrite("test_resized.jpg", resized)

# 2) 이미지 자르기 (일부분만)
# [세로 범위, 가로 범위] -> 위에서 0~200줄, 왼쪽에서 0~300칸
cropped = img[0:200, 0:300]
cv2.imwrite("test_cropped.jpg", cropped)