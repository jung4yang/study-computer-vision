import cv2

img = cv2.imread("test.jpg")

# 1) 흑백으로 (엣지 검출은 흑백에서 함)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2) 엣지 검출 (Canny): 숫자를 높이면 굵은 경계만 잡히고 낮추면 선이 더 많이 생김 (예민하게)
edges = cv2.Canny(gray, 100, 200)

# 3) 결과 저장
cv2.imwrite("test_edges.jpg", edges)