import cv2
import pytesseract
import pyttsx3

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Initialize text-to-speech engine
engine = pyttsx3.init()

while True:
    # Read frame from the webcam
    ret, frame = cap.read()
    
    # Convert frame to grayscale (improves text recognition)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Perform text recognition using pytesseract
    text = pytesseract.image_to_string(gray_frame, lang='hin+eng+mar')
    
    # Speak the recognized text
    engine.say(text)
    engine.runAndWait()
    
    # Display the recognized text on the frame
    cv2.putText(frame, f"Text: {text}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Display the frame with overlaid text
    cv2.imshow('Webcam', frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
