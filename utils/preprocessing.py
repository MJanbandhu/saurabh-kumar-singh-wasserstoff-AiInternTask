import cv2

def preprocess_image(image):
    # Example preprocessing step: resize image
    resized_image = cv2.resize(image, (256, 256))
    return resized_image

if __name__ == "__main__":
    image = cv2.imread('path_to_image')
    preprocessed_image = preprocess_image(image)
    cv2.imwrite('preprocessed_image.png', preprocessed_image)