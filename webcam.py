import mediapipe as mp
import cv2
from mediapipe.tasks import python
from mediapipe.tasks. python import vision
import colorsys

model_path = 'pose_landmarker_full.task'

BaseOptions = mp.tasks.BaseOptions
PoseLandmarker = mp.tasks.vision.PoseLandmarker
PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = PoseLandmarkerOptions(
	base_options = BaseOptions(model_asset_path = model_path),
	running_mode = VisionRunningMode.IMAGE)

detector = vision.PoseLandmarker.create_from_options(options)


#video_path = 'squat.mp4'
cap = cv2.VideoCapture(0) # or video_path

output_path = 'output_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_path, fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))

connections = [(0,1), (1,2), (2,3), (3,7), (0,4), (4,5), (5,6), (6,8), (9,10),
			   (12,14), (14,16), (16,18), (16,20), (16,22), (18,20), (11,12), (11,13), (13,15),
			   (15,21), (15,17), (15,19), (17,19), (12,24), (11,23), (23,24), (24,26), (23,25),
			   (26,28), (25,27), (28,32), (28,30), (30,32), (27,29), (29,31), (27,31)]

colors = [tuple(int(255 * i) for i in colorsys.hsv_to_rgb(x / len(connections), 1.0, 1.0)) for x in range(len(connections))]

while cap.isOpened():
	ret, frame = cap.read()
	if not ret:
		break

	img_height, img_width = frame.shape[:2]
	mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)

	detection_result = detector.detect(mp_image)
	pose_landmarks_list = detection_result.pose_landmarks
	landmarks = pose_landmarks_list[0]


	for i, connection in enumerate(connections):
		start_point = (int(landmarks[connection[0]].x * img_width), int(landmarks[connection[0]].y * img_height))
		end_point = (int(landmarks[connection[1]].x * img_width), int(landmarks[connection[1]].y * img_height))

		cv2.line(frame, start_point, end_point, colors[i], 2)

	for landmark in landmarks:
		landmark_x = int(landmark.x * img_width)
		landmark_y = int(landmark.y * img_height)

		cv2.circle(frame, (landmark_x, landmark_y), 3, (255, 255, 255), -1)

	out.write(frame)
	cv2.imshow('Webcam', frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
out.release()
cv2.destroyAllWindows()