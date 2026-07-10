import cv2

# 웹캠 켜기 (0번 = 기본 카메라)
cap = cv2.VideoCapture(0)

while True:
    # 카메라에서 한 프레임 읽기
    ret, frame = cap.read()
    if not ret:
        break

    # 흑백 -> 엣지 검출
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    
    # 두 창 띄우기: 원본 + 엣지
    cv2.imshow("Webcam", frame)
    cv2.imshow("Edges", edges)
    
    # q 키 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 정리
cap.release()
cv2.destroyAllWindows()
