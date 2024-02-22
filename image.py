import cv2
import pytesseract
from langdetect import detect  # Import language detection library

# Load image
image_path = 'your_image_path.jpg'  # Replace 'your_image_path.jpg' with the path to your image
image = cv2.imread(image_path)

# Perform text recognition using pytesseract
text = pytesseract.image_to_string(image, lang='hin+eng+mar')

# Detect language of the recognized text
try:
    language = detect(text)
except Exception as e:
    language = "Unknown"

# Print the detected language and recognized text in the terminal
print("Detected Language:", language)
print("Recognized Text:", text)

# Save the modified image with overlaid text
cv2.putText(image, f"Language: {language}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.putText(image, f"Text: {text}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
output_image_path = 'output_image.jpg'
cv2.imwrite(output_image_path, image)

# Print path to the output image
print("Output image saved as:", output_image_path)
