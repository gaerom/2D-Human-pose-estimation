import mediapipe as mp
import cv2
from mediapipe.tasks import python
from mediapipe.tasks. python import vision

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