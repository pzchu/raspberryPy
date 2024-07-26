import cv2
import mediapipe as mp


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)
mpDraw = mp.solutions.drawing_utils

image = cv2.imread('./image/victory.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
results = hands.process(image)

h,w,c = image.shape
if results.multi_hand_landmarks:
    for hand_landmarks in results.multi_hand_landmarks:
        print(type(results.multi_hand_landmarks))
        #print(hand_landmarks)
        #print(hand_landmarks.landmark)
        mpDraw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)



# if results.multi_hand_landmarks:
#     for hand_lm in results.multi_hand_landmarks:
#         for lm in hand_lm.landmark:
#             x = int(lm.x * w)
#             y = int(lm.y * h)
#             cv2.circle(image, (x,y),5,(255,0,12),-1)

image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

cv2.imshow('MediaPipe Hand Tracking', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
hands.close()