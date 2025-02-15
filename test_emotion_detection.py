from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case for joy
        statement1 = emotion_detector("I am glad this happened")
        self.assertEqual(statement1['dominant_emotion'], 'joy')

        # Test case for anger
        statement2 = emotion_detector("I am really mad about this")
        self.assertEqual(statement2['dominant_emotion'], 'anger')

        # Test case for disgust
        statement3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(statement3['dominant_emotion'], 'disgust')

        # Test case for sadness
        statement4 = emotion_detector("I am so sad about this")
        self.assertEqual(statement4['dominant_emotion'], 'sadness')

        # Test case for fear
        statement5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(statement5['dominant_emotion'], 'fear')
unittest.main()


