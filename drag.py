# import cv2
# import mediapipe as mp
# import numpy as np

# mp_hands = mp.solutions.hands
# mp_drawing = mp.solutions.drawing_utils

# cap = cv2.VideoCapture(0)
# hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# cv2.namedWindow("Hand Tracking Drag & Drop", cv2.WINDOW_NORMAL)

# object_position = [300, 200]  # Posición inicial del objeto virtual
# grabbed = False

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break
    
#     frame = cv2.flip(frame, 1)
#     h, w, _ = frame.shape
    
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     results = hands.process(rgb_frame)
    
#     if results.multi_hand_landmarks:
#         for hand_landmarks in results.multi_hand_landmarks:
#             mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
#             index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
#             thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            
#             x, y = int(index_finger_tip.x * w), int(index_finger_tip.y * h)
#             thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)
            
#             # Calcular la distancia entre la punta del índice y el pulgar
#             distance = np.sqrt((x - thumb_x) ** 2 + (y - thumb_y) ** 2)
            
#             if distance < 40:  # Si los dedos están juntos, se activa el agarre
#                 grabbed = True
#             elif distance > 60:  # Si los dedos se separan, se suelta el objeto
#                 grabbed = False
            
#             if grabbed:
#                 object_position[0] = x
#                 object_position[1] = y
    
#     # Dibujar el objeto virtual
#     cv2.circle(frame, tuple(object_position), 30, (0, 0, 0), -1)
    
#     cv2.imshow("Hand Tracking Drag & Drop", frame)
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()









# import cv2
# import mediapipe as mp
# import numpy as np

# mp_hands = mp.solutions.hands
# mp_drawing = mp.solutions.drawing_utils

# cap = cv2.VideoCapture(0)
# hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# cv2.namedWindow("Hand Tracking Drag & Drop", cv2.WINDOW_NORMAL)

# # Coordenadas del disquete (parte superior izquierda)
# disk_x, disk_y = 50, 50
# disk_width, disk_height = 100, 100

# # Umbral para detectar si el dedo está cerca del disquete
# threshold_distance = 50

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break
    
#     frame = cv2.flip(frame, 1)
#     h, w, _ = frame.shape
    
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     results = hands.process(rgb_frame)
    
#     if results.multi_hand_landmarks:
#         for hand_landmarks in results.multi_hand_landmarks:
#             mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
#             index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
#             x, y = int(index_finger_tip.x * w), int(index_finger_tip.y * h)
            
#             # Dibujar el disquete (rectángulo + círculo en la parte superior)
#             cv2.rectangle(frame, (disk_x, disk_y), (disk_x + disk_width, disk_y + disk_height), (0, 0, 255), 2)  # Rectángulo
#             cv2.circle(frame, (disk_x + disk_width // 2, disk_y), 20, (0, 0, 255), 2)  # Círculo
            
#             # Calcular la distancia entre el índice y el disquete
#             distance = np.sqrt((x - (disk_x + disk_width // 2)) ** 2 + (y - disk_y) ** 2)
            
#             if distance < threshold_distance:  # Si el índice está cerca del disquete
#                 cv2.putText(frame, "Guardar archivo", (x - 50, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

#     cv2.imshow("Hand Tracking Drag & Drop", frame)
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()









# import cv2
# import mediapipe as mp
# import numpy as np

# mp_hands = mp.solutions.hands
# mp_drawing = mp.solutions.drawing_utils

# cap = cv2.VideoCapture(0)
# hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# cv2.namedWindow("Hand Tracking Drag & Drop", cv2.WINDOW_NORMAL)

# # Coordenadas del disquete (parte superior izquierda)
# disk_x, disk_y = 50, 50
# disk_width, disk_height = 100, 100

# # Coordenada inicial del objeto dragable (círculo verde)
# object_position = [300, 200]  # Posición inicial del objeto virtual
# grabbed = False

# # Umbral para detectar si el dedo está cerca del disquete
# threshold_distance = 50

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break
    
#     frame = cv2.flip(frame, 1)
#     h, w, _ = frame.shape
    
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     results = hands.process(rgb_frame)
    
#     if results.multi_hand_landmarks:
#         for hand_landmarks in results.multi_hand_landmarks:
#             mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
#             index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
#             x, y = int(index_finger_tip.x * w), int(index_finger_tip.y * h)
            
#             # Detección de agarre para mover el objeto
#             if grabbed:
#                 object_position[0] = x
#                 object_position[1] = y
            
#             # Calcular la distancia entre el índice y el disquete
#             distance = np.sqrt((x - (disk_x + disk_width // 2)) ** 2 + (y - disk_y) ** 2)
            
#             # Si el índice está cerca del disquete, mostrar el mensaje
#             if distance < threshold_distance:  
#                 cv2.putText(frame, "Archivo guardado", (x - 50, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
#             # Detección de gesto de agarre basado en la proximidad de la punta del índice y el pulgar
#             thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
#             thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)
            
#             # Si la distancia entre el índice y el pulgar es pequeña, se considera que se está "agarrando"
#             finger_distance = np.sqrt((x - thumb_x) ** 2 + (y - thumb_y) ** 2)
#             if finger_distance < 40:  # Umbral de detección de agarre
#                 grabbed = True
#             else:
#                 grabbed = False
    
#     # Dibujar el objeto dragable (círculo verde)
#     cv2.circle(frame, tuple(object_position), 30, (0, 255, 0), -1)
    
#     # Dibujar el disquete (rectángulo y círculo)
#     cv2.rectangle(frame, (disk_x, disk_y), (disk_x + disk_width, disk_y + disk_height), (0, 0, 255), 2)  # Rectángulo
#     cv2.circle(frame, (disk_x + disk_width // 2, disk_y), 20, (0, 0, 255), 2)  # Círculo
    
#     # Mostrar la imagen
#     cv2.imshow("Hand Tracking Drag & Drop", frame)
    
#     # Salir al presionar la tecla 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()











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













# import cv2
# import mediapipe as mp
# import numpy as np

# mp_hands = mp.solutions.hands
# mp_drawing = mp.solutions.drawing_utils

# cap = cv2.VideoCapture(0)
# hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# # Configurar la ventana en pantalla completa
# cv2.namedWindow("Drawing with Hand", cv2.WND_PROP_FULLSCREEN)
# cv2.setWindowProperty("Drawing with Hand", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# # Color del lápiz (línea dibujada)
# pen_color = (0, 0, 255)  # Rojo (puedes cambiarlo por cualquier color)

# # Listado de puntos donde se dibujó
# drawing_points = []

# # Umbral para el gesto de agarre entre índice y pulgar
# finger_grab_threshold = 40

# # Variable para saber si se está dibujando
# drawing = False

# # Definir el área de los botones (en la parte superior izquierda y derecha)
# button_width = 150
# button_height = 50

# # Botón "Guardar" en la parte superior izquierda
# button_x_guardar = 10
# button_y_guardar = 10

# # Botón "Borrar" en la parte superior derecha
# button_x_borrar = 640 - button_width - 10
# button_y_borrar = 10

# # Definir las zonas de clic para los botones
# def check_button_click(x, y, button_x, button_y, button_width, button_height):
#     return button_x < x < button_x + button_width and button_y < y < button_y + button_height

# # Inicializar la variable `message`
# message = ""

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break
    
#     frame = cv2.flip(frame, 1)
#     h, w, _ = frame.shape
    
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     results = hands.process(rgb_frame)
    
#     if results.multi_hand_landmarks:
#         for hand_landmarks in results.multi_hand_landmarks:
#             mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
#             index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
#             x, y = int(index_finger_tip.x * w), int(index_finger_tip.y * h)
            
#             # Detección de gesto de agarre entre índice y pulgar
#             thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
#             thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)
            
#             # Calcular la distancia entre el índice y el pulgar
#             finger_distance = np.sqrt((x - thumb_x) ** 2 + (y - thumb_y) ** 2)
            
#             # Si la distancia entre el índice y el pulgar es menor al umbral, se considera agarre
#             if finger_distance < finger_grab_threshold:  
#                 drawing = True
#             else:
#                 drawing = False
            
#             # Si estamos dibujando, agregamos el punto a la lista de puntos
#             if drawing:
#                 drawing_points.append((x, y))
            
#             # Verificar si se presiona el botón "Borrar"
#             if check_button_click(x, y, button_x_borrar, button_y_borrar, button_width, button_height):
#                 drawing_points.clear()  # Borrar líneas dibujadas
            
#             # Verificar si se presiona el botón "Guardar"
#             if check_button_click(x, y, button_x_guardar, button_y_guardar, button_width, button_height):
#                 # Guardar la imagen con fondo blanco
#                 saved_image = np.ones((480, 640, 3), dtype=np.uint8) * 255  # Imagen blanca
#                 for i in range(1, len(drawing_points)):
#                     cv2.line(saved_image, drawing_points[i - 1], drawing_points[i], pen_color, 3)
                
#                 # Guardar la imagen como PNG
#                 cv2.imwrite("drawing.png", saved_image)
#                 print("Archivo guardado como drawing.png")
#                 message = "Archivo guardado"
#             else:
#                 message = ""
    
#     # Dibujar las líneas en la pantalla si se está dibujando
#     for i in range(1, len(drawing_points)):
#         cv2.line(frame, drawing_points[i - 1], drawing_points[i], pen_color, 3)
    
#     # Dibujar los botones en la pantalla
#     cv2.rectangle(frame, (button_x_guardar, button_y_guardar), (button_x_guardar + button_width, button_y_guardar + button_height), (0, 255, 0), -1)  # Botón Guardar
#     cv2.putText(frame, 'Guardar', (button_x_guardar + 40, button_y_guardar + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    
#     cv2.rectangle(frame, (button_x_borrar, button_y_borrar), (button_x_borrar + button_width, button_y_borrar + button_height), (0, 255, 0), -1)  # Botón Borrar
#     cv2.putText(frame, 'Borrar', (button_x_borrar + 40, button_y_borrar + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    
#     # Mostrar el mensaje de "Archivo guardado" si se ha guardado la imagen
#     if message:
#         cv2.putText(frame, message, (250, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    
#     # Mostrar la imagen
#     cv2.imshow("Drawing with Hand", frame)
    
#     # Salir al presionar la tecla 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()










# import cv2
# import mediapipe as mp
# import numpy as np

# mp_hands = mp.solutions.hands
# mp_drawing = mp.solutions.drawing_utils

# cap = cv2.VideoCapture(0)
# hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# # Configurar la ventana en pantalla completa
# cv2.namedWindow("Drawing with Hand", cv2.WND_PROP_FULLSCREEN)
# cv2.setWindowProperty("Drawing with Hand", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# # Color del lápiz (línea dibujada)
# pen_color = (0, 0, 255)  # Rojo (puedes cambiarlo por cualquier color)

# # Listado de puntos donde se dibujó
# drawing_points = []

# # Umbral para el gesto de agarre entre índice y pulgar
# finger_grab_threshold = 40

# # Variable para saber si se está dibujando
# drawing = False

# # Definir el área de los botones (en la parte superior izquierda y derecha)
# button_width = 150
# button_height = 50

# # Botón "Guardar" en la parte superior izquierda
# button_x_guardar = 10
# button_y_guardar = 10

# # Botón "Borrar" en la parte superior derecha
# button_x_borrar = 640 - button_width - 10
# button_y_borrar = 10

# # Definir las zonas de clic para los botones
# def check_button_click(x, y, button_x, button_y, button_width, button_height):
#     return button_x < x < button_x + button_width and button_y < y < button_y + button_height

# # Inicializar la variable `message`
# message = ""

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break
    
#     frame = cv2.flip(frame, 1)
#     h, w, _ = frame.shape
    
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     results = hands.process(rgb_frame)
    
#     if results.multi_hand_landmarks:
#         for hand_landmarks in results.multi_hand_landmarks:
#             mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
#             index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
#             x, y = int(index_finger_tip.x * w), int(index_finger_tip.y * h)
            
#             # Detección de gesto de agarre entre índice y pulgar
#             thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
#             thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)
            
#             # Calcular la distancia entre el índice y el pulgar
#             finger_distance = np.sqrt((x - thumb_x) ** 2 + (y - thumb_y) ** 2)
            
#             # Si la distancia entre el índice y el pulgar es menor al umbral, se considera agarre
#             if finger_distance < finger_grab_threshold:  
#                 drawing = True
#             else:
#                 drawing = False
            
#             # Si estamos dibujando, agregamos el punto a la lista de puntos
#             if drawing:
#                 drawing_points.append((x, y))
            
#             # Verificar si se presiona el botón "Borrar"
#             if check_button_click(x, y, button_x_borrar, button_y_borrar, button_width, button_height):
#                 drawing_points.clear()  # Borrar líneas dibujadas
            
#             # Verificar si se presiona el botón "Guardar"
#             if check_button_click(x, y, button_x_guardar, button_y_guardar, button_width, button_height):
#                 # Guardar la imagen con fondo blanco
#                 saved_image = np.ones((480, 640, 3), dtype=np.uint8) * 255  # Imagen blanca
#                 for i in range(1, len(drawing_points)):
#                     cv2.line(saved_image, drawing_points[i - 1], drawing_points[i], pen_color, 3)
                
#                 # Guardar la imagen como PNG
#                 cv2.imwrite("drawing.png", saved_image)
#                 print("Archivo guardado como drawing.png")
#                 message = "Archivo guardado"
#             else:
#                 message = ""
    
#     # Dibujar las líneas en la pantalla si se está dibujando
#     for i in range(1, len(drawing_points)):
#         cv2.line(frame, drawing_points[i - 1], drawing_points[i], pen_color, 3)
    
#     # Dibujar los botones en la pantalla (botón "Guardar" y "Borrar")
#     cv2.rectangle(frame, (button_x_guardar, button_y_guardar), (button_x_guardar + button_width, button_y_guardar + button_height), (0, 255, 0), -1)  # Botón Guardar
#     cv2.putText(frame, 'Guardar', (button_x_guardar + 40, button_y_guardar + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    
#     cv2.rectangle(frame, (button_x_borrar, button_y_borrar), (button_x_borrar + button_width, button_y_borrar + button_height), (0, 255, 0), -1)  # Botón Borrar
#     cv2.putText(frame, 'Borrar', (button_x_borrar + 40, button_y_borrar + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    
#     # Mostrar el mensaje de "Archivo guardado" si se ha guardado la imagen
#     if message:
#         cv2.putText(frame, message, (250, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    
#     # Mostrar la imagen
#     cv2.imshow("Drawing with Hand", frame)
    
#     # Salir al presionar la tecla 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
