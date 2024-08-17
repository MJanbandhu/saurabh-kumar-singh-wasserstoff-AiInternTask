import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import cv2

def segment_image(image):
    # Load a pre-trained segmentation model
    model = load_model('models/segmentation_model.h5')  # Update the path to your model
    
    # Preprocess the image
    image = cv2.resize(image, (128, 128))  # Resize as per model input requirements
    image = image.astype('float32') / 255.0
    image = np.expand_dims(image, axis=0)
    
    # Perform segmentation
    segmented = model.predict(image)
    
    # Post-process the output
    segmented = (segmented > 0.5).astype(np.uint8) * 255
    segmented = np.squeeze(segmented)
    
    return segmented

if __name__ == "__main__":
    image = cv2.imread('data/input_images/input_image.png')  # Update the path to your image
    segmented = segment_image(image)
    cv2.imwrite('data/segmented_objects/output_segmented_image.png', segmented)