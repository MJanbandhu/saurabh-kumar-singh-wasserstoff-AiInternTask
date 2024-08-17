import cv2
import matplotlib.pyplot as plt
import pandas as pd

def generate_output(original_image_path, segmented_image_path, data_file):
    original_image = cv2.imread(original_image_path)
    segmented_image = cv2.imread(segmented_image_path)
    
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(segmented_image, cv2.COLOR_BGR2RGB))
    plt.title("Segmented Image")
    plt.show()
    
    with open(data_file, 'r') as file:
        data = pd.read_json(file)
    
    print(data)

# Example usage
if __name__ == "__main__":
    generate_output("data/input_images/sample.jpg", "data/output/segmented_image.jpg", "data/output/mapped_data.json")