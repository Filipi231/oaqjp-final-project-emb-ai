"""Testes unitários para emotion_detector."""
import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Verifica a emoção dominante para cada caso."""

    def check(self, text, expected):
        """Confere a emoção dominante de um texto."""
        self.assertEqual(emotion_detector(text)["dominant_emotion"], expected)

    def test_joy(self):
        """Alegria."""
        self.check("I am glad this happened", "joy")

    def test_anger(self):
        """Raiva."""
        self.check("I am really mad about this", "anger")

    def test_disgust(self):
        """Nojo."""
        self.check("I feel disgusted just hearing about this", "disgust")

    def test_sadness(self):
        """Tristeza."""
        self.check("I am so sad about this", "sadness")

    def test_fear(self):
        """Medo."""
        self.check("I am really afraid that this will happen", "fear")

    def test_empty(self):
        """Texto vazio retorna erro 400."""
        result = emotion_detector("")
        self.assertEqual(result["status_code"], 400)
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
