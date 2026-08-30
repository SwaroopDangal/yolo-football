import cv2

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames=[]
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    return frames

def save_video(frames, output_path):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    height, width = frames[0].shape[:2]
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (width, height))
    for frame in frames:
        out.write(frame)
    out.release()