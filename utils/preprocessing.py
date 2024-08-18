import cv2
import os

def preprocess_image(image):
    """ Example preprocessing step: resize image """
    resized_image = cv2.resize(image, (256, 256))
    return resized_image

if __name__ == "__main__":
    # Note: Ensure the path provided is valid
    image_path = 'data/input_images/your_image_name.jpg'  # image path or handle dynamically
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image file not found: {image_path}")
    preprocessed_image = preprocess_image(image)
    preprocessed_image_path = 'preprocessed_image.png'
    cv2.imwrite(preprocessed_image_path, preprocessed_image)