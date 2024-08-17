import cv2
import pytesseract

def extract_text(image):
    # Use Tesseract OCR to extract text
    text = pytesseract.image_to_string(image)
    return text

if __name__ == "__main__":
    # Update the path to the actual image location within your project directory
    image_path = 'data/segmented_objects/object_image.png'
    image = cv2.imread(image_path)
    text = extract_text(image)
    print(text)