import unittest
import cap


class UnitTestExample(unittest.TestCase):

    def test_first_letter_capital(self):
        text='python'
        result=cap.cap_text(text)
        self.assertEqual(result,'Python')

    def test_multiple_words(self):
        text='sudarshan python'
        result = cap.cap_multiple(text)
        self.assertEqual(result, 'Sudarshan Python')

if __name__=='__main__':
    unittest.main()
