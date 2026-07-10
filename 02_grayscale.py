import cv2

# 컬러 이미지 불러오기
img = cv2.imread("test.jpg")
print("컬러 이미지 크기:", img.shape)

# 흑백으로 변환 "cvw.cvtColor(img, cv2.COLOR_BGR2GRAY)" -> open cv에서는 RGB가 아닌 BGR
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print("흑백 이미지 크기:", gray.shape)

# 흑백 이미지를 새 파일로 저장
cv2.imwrite("test_gray.jpg", gray)
print("Open test_gray.jpg")
