import cv2
import tensorflow as tf
import numpy as np
import pygame

# Use pygame to obtain the 'beeping' sound that plays when distracting objects are detected being used
pygame.init()
beep_sound = pygame.mixer.Sound('beep.wav')  # Ensure you have a beep.wav file in your directory

# Load the trained model
model = tf.saved_model.load('path/to/your/model') 

# Load label map
category_index = {
    1: {'id': 1, 'name': 'controller'},
    2: {'id': 2, 'name': 'phone'}
}

def detect_objects(image_np):
    input_tensor = tf.convert_to_tensor(image_np)
    input_tensor = input_tensor[tf.newaxis, ...]
    detections = model(input_tensor)
    return detections

# Utilize the OpenCV video capture
cap = cv2.VideoCapture(0)  # 0 for the default camera

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Preprocess the frame for detection
    image_np = np.asarray(frame)
    
    # Perform the object detection
    detections = detect_objects(image_np)
    
    # Extract these detection results
    boxes = detections['detection_boxes'][0].numpy()
    scores = detections['detection_scores'][0].numpy()
    classes = detections['detection_classes'][0].numpy()
    
    # Set detection threshold
    detection_threshold = 0.5
    
    detected_objects = set()
    
    for i in range(len(scores)):
        if scores[i] >= detection_threshold:
            class_id = int(classes[i])
            if class_id in category_index:
                detected_objects.add(category_index[class_id]['name'])
    
    # Check if any of the classified objects are detected
    if 'phone' in detected_objects or 'controller' in detected_objects:
        beep_sound.play()
      
    #Display frame
    cv2.imshow('Object Detection', frame)
    
    # Exit on 'q' press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release capture, close windows
cap.release()
cv2.destroyAllWindows()
