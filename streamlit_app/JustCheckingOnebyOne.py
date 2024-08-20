import os
import streamlit as st

# Define the directory to save uploaded images
input_images_dir = 'data/input_images'

# Ensure the directory exists
os.makedirs(input_images_dir, exist_ok=True)

def save_uploaded_file(uploaded_file, save_path):
    """ Save the uploaded file to the specified path """
    try:
        with open(save_path, "wb") as f:
            f.write(uploaded_file.read())
        return True
    except Exception as e:
        st.error(f"Error saving file: {e}")
        return False

def main():
    st.title("Upload and Save Image")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Define the path where the uploaded image will be saved
        image_path = os.path.join(input_images_dir, uploaded_file.name)
        
        if save_uploaded_file(uploaded_file, image_path):
            st.image(image_path, caption='Uploaded Image', use_column_width=True)
            st.write(f"Image saved at: {image_path}")
        else:
            st.write("Failed to save the image.")

if __name__ == "__main__":
    main()