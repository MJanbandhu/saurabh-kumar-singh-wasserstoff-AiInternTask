import unittest
from models.object_extraction import extract_objects
import cv2

class TestExtraction(unittest.TestCase):
    def test_extraction(self):
        segmented_image = cv2.imread('path_to_test_segmented_image.png', 0)
        objects = extract_objects(segmented_image)
        self.assertGreater(len(objects), 0)

if __name__ == "__main__":
    unittest.main()