import unittest
from models.summarization_model import summarize_attributes

class TestSummarization(unittest.TestCase):
    def test_summarization(self):
        identified_objects = [{'label': 'object1', 'confidence': 0.9}]
        summaries = summarize_attributes(identified_objects)
        self.assertGreater(len(summaries), 0)

if __name__ == "__main__":
    unittest.main()