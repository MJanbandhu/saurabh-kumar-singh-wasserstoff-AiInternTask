import sys
import os
import streamlit as st
from PIL import Image
import numpy as np


# Add the 'models' directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../models')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../models')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../utils')))


import streamlit as st
from PIL import Image
import numpy as np
from segmentation_model import segment_image
from object_extraction import extract_objects
from object_identification import identify_objects
from text_extraction_model import extract_text
from summarization_model import summarize_attributes
from data_mapping import map_data
from visualization import generate_output

st.title("AI Pipeline for Image Segmentation and Object Analysis")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image_np = np.array(image)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    st.write("Running segmentation...")
    segmented = segment_image(image_np)
    
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
    
    st.write("Generating output...")
    final_image = generate_output(image_np, mapped_data)
    st.image(final_image, caption='Processed Image.', use_column_width=True)
    
    st.write("Pipeline completed.")