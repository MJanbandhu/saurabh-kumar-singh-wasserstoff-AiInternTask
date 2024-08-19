import cv2
import os

def preprocess_image(image):
    """ Example preprocessing step: resize image """
    resized_image = cv2.resize(image, (256, 256))
    return resized_image

if __name__ == "__main__":
    # Define the input and output paths
    input_dir = 'data/input_images/'
    output_dir = 'data/segmented_objects/'
    
    # Ensure the directories exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Example image filename
    image_filename = 'example_image.jpg'  # Change this to your image filename
    image_path = os.path.join(input_dir, image_filename)
    
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image file not found: {image_path}")
    
    # Preprocess the image
    preprocessed_image = preprocess_image(image)
    
    # Save the preprocessed image
    preprocessed_image_filename = 'preprocessed_image.png'
    preprocessed_image_path = os.path.join(output_dir, preprocessed_image_filename)
    cv2.imwrite(preprocessed_image_path, preprocessed_image)
    
    print(f"Preprocessed image saved to: {preprocessed_image_path}")