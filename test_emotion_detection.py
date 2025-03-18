import unittest
from emotion_detection import emotion_detector

cases = {
    "joy": "I am glad this happened",
    "anger": "I am really mad about this",
    "disgust": "I feel disgusted just hearing about this",
    "sadness": "I am so sad about this",
    "fear": "I am really afraid that this will happen"
}

class TestDominantEmotion(unittest.TestCase):
    def test_emotion_detection(self):
        for emotion, text in cases.items():
            self.assertEqual(emotion_detector(text)["dominant_emotion"], emotion)

if __name__ == "__main__":
    unittest.main()
