from ultralytics import YOLO
import cv2
from playsound import playsound
import argparse

def main(args):
    try:
        model = YOLO(args.model_path)
        cap = cv2.VideoCapture(args.camera_index)
        if not cap.isOpened():
            print(f"Error: Could not open camera with index {args.camera_index}.")
            return

        frame_count = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Failed to capture frame.")
                break

            results = model.predict(source=frame, conf=0.5, verbose=False)
            result = results[0]

            annotated_frame = result.plot()

            # Lấy danh sách class ID đã phát hiện
            detected_cls = [int(c) for c in result.boxes.cls]

            if any(cls in detected_cls for cls in args.targets):
                frame_count += 1
            else:
                frame_count = 0

            if frame_count >= args.thresh_frames:
                try:
                    playsound("sound.mp3")
                except Exception as e:
                    print(f"Error playing sound: {e}")
                # Reset đếm sau khi cảnh báo
                frame_count = 0

            cv2.imshow("YOLOv11 Detection", annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except FileNotFoundError:
        print(f"Error: Model file not found at {args.model_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if 'cap' in locals() and cap.isOpened():
            cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YOLOv11 Drowsiness Detection")
    parser.add_argument("--model_path", type=str, default="yolo_model/best.pt", help="Path to the YOLO model.")
    parser.add_argument("--camera_index", type=int, default=0, help="Index of the camera to use.")
    parser.add_argument("--thresh_frames", type=int, default=30, help="Number of consecutive frames to trigger an alert.")
    parser.add_argument("--targets", type=int, nargs='+', default=[1, 2, 3, 4, 5, 6, 10, 12, 13], help="List of target class IDs to detect.")
    args = parser.parse_args()
    main(args)