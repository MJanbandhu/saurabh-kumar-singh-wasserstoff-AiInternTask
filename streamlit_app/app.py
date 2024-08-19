import os
import json
import sys
import streamlit as st
from PIL import Image
import numpy as np
import cv2

# Ensure directories exist and are writable
input_images_dir = 'data/input_images'
segmented_objects_dir = 'data/segmented_objects'
output_dir = 'data/output_images'


# Add directories to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../models')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../utils')))

# Import functions from models and utils
from segmentation_model import segment_image
from object_extraction import extract_objects
from object_identification import identify_objects
from text_extraction_model import extract_text
from summarization_model import summarize_attributes
from data_mapping import map_data
from visualization import generate_output

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
        # Save uploaded file to the input images directory
        image_path = os.path.join(input_images_dir, uploaded_file.name)
        save_uploaded_file(uploaded_file, image_path)
        
        # Load and display the uploaded image
        image = Image.open(image_path)
        st.image(image, caption='Uploaded Image.', use_column_width=True)

        # Preprocess the image
        image_cv = cv2.imread(image_path)
        preprocessed_image = preprocess_image(image_cv)
        preprocessed_image_path = os.path.join(output_dir, f'preprocessed_{uploaded_file.name}')
        cv2.imwrite(preprocessed_image_path, preprocessed_image)
        
        st.write("Running segmentation...")
        segmented = segment_image(preprocessed_image)
        segmented_path = os.path.join(output_dir, 'segmented_image.png')
        Image.fromarray(segmented).save(segmented_path)
        st.image(segmented_path, caption='Segmented Image', use_column_width=True)

        st.write("Extracting objects...")
        objects = extract_objects(segmented)

        st.write("Identifying objects...")
        identified_objects = identify_objects(objects)

        st.write("Extracting text...")
        text_data = [extract_text(obj) for obj in objects]

        st.write("Summarizing attributes...")
        summaries = summarize_attributes(identified_objects, text_data)

        st.write("Mapping data...")
        mapped_data = map_data(objects, text_data, identified_objects, summaries=summaries)
        mapped_data_path = os.path.join(output_dir, 'mapped_data.json')
        with open(mapped_data_path, 'w') as f:
            json.dump(mapped_data, f, indent=4)

        st.write("Generating output...")
        final_image_path = os.path.join(output_dir, 'final_image.png')
        generate_output(image_path, segmented_path, mapped_data_path)
        final_image = Image.open(final_image_path)
        st.image(final_image, caption='Processed Image.', use_column_width=True)

        st.write("Pipeline completed.")

if __name__ == "__main__":
    main()
