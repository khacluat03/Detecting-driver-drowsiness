from ultralytics import YOLO
import cv2
from playsound import playsound
import winsound

model = YOLO("/runs/detect/train2/weights/best.pt")

cap = cv2.VideoCapture(0)

frame_count = 0
thresh_frames = 30

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(source=frame, conf=0.5, verbose=False)
    result = results[0]

    annotated_frame = result.plot()

    # Lấy danh sách class ID đã phát hiện
    detected_cls = [int(c) for c in result.boxes.cls]
    targets = [1, 2, 3, 4, 5, 6, 10, 12, 13]

    if any(cls in detected_cls for cls in targets):
        frame_count += 1
    else:
        frame_count = 0

    if frame_count >= thresh_frames:
        # winsound.Beep(1000, 2000)
        playsound("sound.mp3")
        # Reset đếm sau khi cảnh báo
        frame_count = 0

    cv2.imshow("YOLOv11 Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()