import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture('rtsp://192.168.8.1:8900/live')

# Check if the capture object is opened successfully
if not cap.isOpened():
    print("Error opening video stream")

# Read a frame from the video stream
while True:
    ret, frame = cap.read()

    # Check if the frame is empty
    if not ret:
        break

    # Display the frame
    cv2.imshow('Frame', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture object
cap.release()

# Destroy all windows
cv2.destroyAllWindows()
