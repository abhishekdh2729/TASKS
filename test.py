from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")
TARGET_CLASS = 0  # 'person'

img_path = 'test_img.webp'
img = cv2.imread(img_path)

# Resizing the before inference
img = cv2.resize(img, (640, 480)) 

results = model(img)[0]

for box in results.boxes:
    class_id = int(box.cls[0])
    if class_id == TARGET_CLASS:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(img, "Person", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

cv2.imshow("Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
