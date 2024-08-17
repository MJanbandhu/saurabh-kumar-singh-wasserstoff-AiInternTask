import cv2

def postprocess_segmented_image(segmented_image):
    # Example postprocessing step: remove small contours
    contours, _ = cv2.findContours(segmented_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        if cv2.contourArea(contour) < 500:  # Threshold for small contours
            cv2.drawContours(segmented_image, [contour], 0, (0, 0, 0), -1)
    
    return segmented_image

if __name__ == "__main__":
    segmented_image = cv2.imread('output_segmented_image.png', 0)
    postprocessed_image = postprocess_segmented_image(segmented_image)
    cv2.imwrite('postprocessed_segmented_image.png', postprocessed_image)