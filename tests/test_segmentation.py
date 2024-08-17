import unittest
from models.segmentation_model import segment_image
import cv2

class TestSegmentation(unittest.TestCase):
    def test_segmentation(self):
        image = cv2.imread('path_to_test_image.jpg')
        segmented = segment_image(image)
        self.assertIsNotNone(segmented)

if __name__ == "__main__":
    unittest.main()