import cv2
import easyocr

# Initialize EasyOCR reader for English and Hindi
reader = easyocr.Reader(['en', 'hi'])

# Set font for displaying recognized text
font = cv2.FONT_HERSHEY_SIMPLEX

# Capture webcam feed
cap = cv2.VideoCapture(0)

while True:
    # Read frame from webcam
    ret, frame = cap.read()
    
    # Perform text recognition on the frame
    results = reader.readtext(frame)
    
    # Display recognized text overlaid on the frame
    for result in results:
        top_left = tuple(result[0][0])
        bottom_right = tuple(result[0][2])
        text = result[1]
        confidence = result[2]
        
        # Draw bounding box around the text
        cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)
        
        # Display recognized text and confidence level
        cv2.putText(frame, f"{text} ({confidence:.2f})", (top_left[0], top_left[1] - 10),
                    font, 0.5, (0, 255, 0), 2)
    
    # Display the frame with overlaid text
    cv2.imshow('Webcam', frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
