import unittest
from models.object_identification import identify_objects
import cv2

class TestIdentification(unittest.TestCase):
    def test_identification(self):
        objects = [cv2.imread('path_to_test_object_image.png')]
        identified_objects = identify_objects(objects)
        self.assertGreater(len(identified_objects), 0)

if __name__ == "__main__":
    unittest.main()