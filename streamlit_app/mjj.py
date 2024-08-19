# this file is for testing only

import streamlit as st
from utils.preprocessing import preprocess_image
from models.segmentation_model import segment_image, load_model
from models.object_extraction import extract_objects

st.title("AI Pipeline for Image Segmentation and Object Analysis")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    image_path = f"data/input_images/{uploaded_file.name}"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.image(image_path, caption='Uploaded Image.', use_column_width=True)
    st.write("Processing...")
    
    preprocessed_image = preprocess_image(image_path)
    model = load_model()
    segmented_image = segment_image(preprocessed_image, model)
    
    segmented_image_path = f"data/segmented_objects/segmented_{uploaded_file.name}"
    save_segmented_image(segmented_image, segmented_image_path)
    
    extract_objects(segmented_image_path, image_path, 'data/segmented_objects/')
    
    st.image(segmented_image_path, caption='Segmented Image.', use_column_width=True)
    st.success("Processing complete!")