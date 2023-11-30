import cv2
import tkinter as tk
from tkinter import filedialog

def extract_human_and_faces(input_video, output_folder):
    # Load pre-trained deep learning models
    human_net = cv2.dnn.readNetFromCaffe('deploy.prototxt', 'mobilenet_iter_73000.caffemodel')
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Open the video file
    cap = cv2.VideoCapture(input_video)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    # Create VideoWriter for output video
    out = cv2.VideoWriter(output_folder + '/output_video.avi', cv2.VideoWriter_fourcc(*'DIVX'), 30, (frame_width, frame_height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Human detection
        blob = cv2.dnn.blobFromImage(frame, 0.007843, (300, 300), 127.5)
        human_net.setInput(blob)
        detections = human_net.forward()

        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.2:  # Confidence threshold
                box = detections[0, 0, i, 3:7] * np.array([frame_width, frame_height, frame_width, frame_height])
                (startX, startY, endX, endY) = box.astype("int")
                cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)

                # Face detection within the human bounding box
                human_roi = frame[startY:endY, startX:endX]
                gray_roi = cv2.cvtColor(human_roi, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray_roi, scaleFactor=1.3, minNeighbors=5)

                for (fx, fy, fw, fh) in faces:
                    cv2.rectangle(frame, (startX + fx, startY + fy), (startX + fx + fw, startY + fy + fh), (255, 0, 0), 2)

        # Write the frame with detections to the output video
        out.write(frame)

    # Release resources
    cap.release()
    out.release()

def select_video_file():
    video_file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])
    video_entry.delete(0, tk.END)
    video_entry.insert(0, video_file_path)

def select_output_folder():
    output_folder_path = filedialog.askdirectory()
    output_entry.delete(0, tk.END)
    output_entry.insert(0, output_folder_path)

def extract():
    input_video = video_entry.get()
    output_folder = output_entry.get()
    extract_human_and_faces(input_video, output_folder)
    result_label.config(text="Extraction complete!")

# GUI setup
root = tk.Tk()
root.title("Human and Face Extraction from Video")

# Video file selection
tk.Label(root, text="Select Video File:").pack()
video_entry = tk.Entry(root, width=50)
video_entry.pack()
tk.Button(root, text="Browse", command=select_video_file).pack()

# Output folder selection
tk.Label(root, text="Select Output Folder:").pack()
output_entry = tk.Entry(root, width=50)
output_entry.pack()
tk.Button(root, text="Browse", command=select_output_folder).pack()

# Extract button
tk.Button(root, text="Extract", command=extract).pack()

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

# Run the GUI
root.mainloop()
