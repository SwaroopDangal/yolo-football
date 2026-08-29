from ultralytics import YOLO

model = YOLO('yolov8s')


results = model.predict("video/08fd33_4.mp4",save=True)
print(results[0])
for box in results[0].boxes:
    print(box)
