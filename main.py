# importing necessary libraries
import cv2
import mediapipe as mp

# reading webcam input
cap = cv2.VideoCapture(0)


mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    # drawing landmarks
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow('image', img)
    if cv2.waitKey(5) & 0xFF == 27:
        break
cv2.destroyAllWindows()
