# AI Pipeline for Image Segmentation and Object Analysis

## Overview
This project implements an AI pipeline that segments, identifies, and analyzes objects within an image, then outputs a summary with mapped data.

## Folder Structure
- **data/**: Contains input images, segmented objects, and output files.
- **models/**: Scripts for segmentation, identification, text extraction, and summarization models.
- **utils/**: Helper functions for preprocessing, postprocessing, data mapping, and visualization.
- **streamlit_app/**: Contains the Streamlit app for testing the pipeline.
- **tests/**: Unit tests for different components.
- **README.md**: This file.
- **requirements.txt**: List of Python packages needed.
- **presentation.pptx**: Project summary presentation.

## Setup Instructions
1. Clone the repository.
2. Install the required packages: `pip install -r requirements.txt`.
3. Run the Streamlit app: `streamlit run streamlit_app/app.py`.

## Usage
1. Upload an image through the Streamlit app.
2. The pipeline will segment the image, extract objects, identify them, extract text, summarize attributes, and map the data.
3. The results are displayed and saved in the `data/output/` directory.

## Requirements
- Python 3.x
- OpenCV
- TensorFlow/Keras
- Pytesseract
- TextBlob
- Streamlit