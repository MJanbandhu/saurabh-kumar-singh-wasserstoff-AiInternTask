import unittest
from models.text_extraction_model import extract_text
import cv2

class TestTextExtraction(unittest.TestCase):
    def test_text_extraction(self):
        image = cv2.imread('path_to_test_object_image.png')
        text = extract_text(image)
        self.assertIsNotNone(text)

if __name__ == "__main__":
    unittest.main()