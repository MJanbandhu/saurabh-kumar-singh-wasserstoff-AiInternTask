import os
import cv2
import streamlit as st
from PIL import Image

def preprocess_image(image):
    """ Example preprocessing step: resize image """
    resized_image = cv2.resize(image, (256, 256))
    return resized_image

def save_uploaded_file(uploaded_file, save_path):
    """ Save the uploaded file to the specified path """
    with open(save_path, "wb") as f:
        f.write(uploaded_file.read())

def main():
    st.title("AI Pipeline for Image Segmentation and Object Analysis")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Define save paths
        image_path = os.path.join('data/input_images', uploaded_file.name)
        preprocessed_image_path = os.path.join('data/output', f'preprocessed_{uploaded_file.name}')

        # Save uploaded file
        save_uploaded_file(uploaded_file, image_path)
        
        # Load and preprocess image
        image_cv = cv2.imread(image_path)
        if image_cv is None:
            st.error(f"Failed to load image at {image_path}")
            return
        
        preprocessed_image = preprocess_image(image_cv)
        cv2.imwrite(preprocessed_image_path, preprocessed_image)
        
        # Continue with other steps...

if __name__ == "__main__":
    main()