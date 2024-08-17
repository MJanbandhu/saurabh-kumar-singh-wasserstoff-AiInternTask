import cv2
import os

def extract_objects(segmented_image, output_dir):
    contours, _ = cv2.findContours(segmented_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    os.makedirs(output_dir, exist_ok=True)
    
    for idx, contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)
        object_img = segmented_image[y:y+h, x:x+w]
        cv2.imwrite(os.path.join(output_dir, f"object_{idx}.jpg"), object_img)

# Example usage
if __name__ == "__main__":
    segmented_image = cv2.imread("data/output/segmented_image.jpg", cv2.IMREAD_GRAYSCALE)
    extract_objects(segmented_image, "data/segmented_objects/")