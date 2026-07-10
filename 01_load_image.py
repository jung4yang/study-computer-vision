import cv2

# 이미지 불러오기 (test.jpg를 폴더에 넣어둬야 함)
img = cv2.imread("test.jpg")

print("이미지 크기:", img.shape)
# 이미지 크기 출력 (세로, 가로, 색채널)
print("세로 픽셀:", img.shape[0])
print("가로 픽셀:", img.shape[1])
print("색 채널 수:", img.shape[2])