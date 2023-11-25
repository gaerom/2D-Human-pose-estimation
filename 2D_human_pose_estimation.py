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

np_image = cv2.imread('male.jpg')
img_height, img_width = np_image.shape[:2]
mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=np_image)

detection_result = detector.detect(mp_image)
pose_landmarks_list = detection_result.pose_landmarks # detect된 keypoint들이 담긴 list
landmarks = pose_landmarks_list[0]


connections = [(0,1), (1,2), (2,3), (3,7), (0,4), (4,5), (5,6), (6,8), (9,10),
			   (12,14), (14,16), (16,18), (16,20), (16,22), (18,20), (11,12), (11,13), (13,15),
			   (15,21), (15,17), (15,19), (17,19), (12,24), (11,23), (23,24), (24,26), (23,25),
			   (26,28), (25,27), (28,32), (28,30), (30,32), (27,29), (29,31), (27,31)]

colors = [tuple(int(255 * i) for i in colorsys.hsv_to_rgb(x / len(connections), 1.0, 1.0)) for x in range(len(connections))]

for i, connection in enumerate(connections):
	start_point = (int(landmarks[connection[0]].x * img_width), int(landmarks[connection[0]].y * img_height))
	end_point = (int(landmarks[connection[1]].x * img_width), int(landmarks[connection[1]].y * img_height))

	cv2.line(np_image, start_point, end_point, colors[i], 2)

for landmark in landmarks:
	landmark_x = int(landmark.x * img_width)
	landmark_y = int(landmark.y * img_height)

	cv2.circle(np_image, (landmark_x, landmark_y), 3, (255, 255, 255), -1)

# 코의 좌표 확인
nose_landmarks = landmarks[0] # nose
# print(nose_landmarks)

nose_landmark_x = int(nose_landmarks.x * img_width)
nose_landmark_y = int(nose_landmarks.y * img_height)
visibility = nose_landmarks.visibility

print(f'nose:({nose_landmark_x}, {nose_landmark_y}, {visibility})')

cv2.imshow('Landmarks and lines', np_image)
cv2.waitKey()
cv2.destroyAllWindows()