import cv2

webcam = cv2.VideoCapture(0)

def generate_frames():
    while True:
        validation, frame = webcam.frame()
        if not validation:
            break
        else:
           ret, buffer =  cv2.imshow("Video da Webcam", frame)
           frame = buffer.tobytes()
        return frame

generate_frames()