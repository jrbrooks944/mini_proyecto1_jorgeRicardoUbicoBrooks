


import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

cv2.namedWindow("Hand Tracking Drag & Drop", cv2.WINDOW_NORMAL)

# Coordenadas del disquete (parte superior izquierda)
disk_x, disk_y = 50, 50
disk_width, disk_height = 100, 100

# Coordenada inicial del objeto dragable (círculo verde)
object_position = [300, 200]  # Posición inicial del objeto virtual
grabbed = False

# Umbral para detectar si el dedo está cerca del disquete
threshold_distance = 50

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            x, y = int(index_finger_tip.x * w), int(index_finger_tip.y * h)
            
            # Detección de agarre para mover el objeto
            if grabbed:
                object_position[0] = x
                object_position[1] = y
            
            # Calcular la distancia entre el índice y el disquete
            distance = np.sqrt((x - (disk_x + disk_width // 2)) ** 2 + (y - disk_y) ** 2)
            
            # Si el índice está cerca del disquete, mostrar el mensaje
            if distance < threshold_distance:  
                cv2.putText(frame, "Archivo guardado", (x - 50, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                # Reposicionar la pelota verde en el centro de la pantalla
                object_position = [w // 2, h // 2]
            
            # Detección de gesto de agarre basado en la proximidad de la punta del índice y el pulgar
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)
            
            # Si la distancia entre el índice y el pulgar es pequeña, se considera que se está "agarrando"
            finger_distance = np.sqrt((x - thumb_x) ** 2 + (y - thumb_y) ** 2)
            if finger_distance < 40:  # Umbral de detección de agarre
                grabbed = True
            else:
                grabbed = False
    
    # Dibujar el objeto dragable (círculo verde)
    cv2.circle(frame, tuple(object_position), 30, (0, 255, 0), -1)
    
    # Dibujar el disquete (rectángulo y círculo)
    cv2.rectangle(frame, (disk_x, disk_y), (disk_x + disk_width, disk_y + disk_height), (0, 0, 255), 2)  # Rectángulo
    cv2.circle(frame, (disk_x + disk_width // 2, disk_y), 20, (0, 0, 255), 2)  # Círculo
    
    # Mostrar la imagen
    cv2.imshow("Hand Tracking Drag & Drop", frame)
    
    # Salir al presionar la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

