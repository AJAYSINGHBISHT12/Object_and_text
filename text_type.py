import cv2
import pytesseract
from langdetect import detect
import re

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    # Read frame from webcam
    ret, frame = cap.read()
    
    # Perform text recognition using pytesseract
    text = pytesseract.image_to_string(frame, lang='hin+eng+mar')
    
    # Detect language of the recognized text
    try:
        language = detect(text)
    except Exception as e:
        language = "Unknown"
    
    # Function to classify text structure
    def classify_text_structure(text):
        # Check for presence of tabular separators
        if re.search(r'\|\s*\|\s*\|', text):
            return "Table"
        # Check for typical paragraph structure
        elif '\n\n' in text:
            return "Paragraph"
        # Check for common phrases indicating newspaper article
        elif re.search(r'Breaking News|Opinion Piece', text):
            return "Newspaper Article"
        else:
            return "Unknown"

    # Classify text structure
    text_structure = classify_text_structure(text)
    
    # Print the detected language and recognized text
    print("Detected Language:", language)
    print("Text Structure:", text_structure)
    print("Recognized Text:", text)
    
    # Display the detected language and recognized text on the frame
    cv2.putText(frame, f"Language: {language}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f"Text Structure: {text_structure}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f"Text: {text}", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Display the frame with overlaid text
    cv2.imshow('Webcam', frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
