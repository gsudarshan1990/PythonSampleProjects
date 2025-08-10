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

    def test_empty_string(self):
        """Test behavior with empty string"""
        text = ''
        result_cap = cap.cap_text(text)
        result_multiple = cap.cap_multiple(text)
        self.assertEqual(result_cap, '')
        self.assertEqual(result_multiple, '')

    def test_already_capitalized(self):
        """Test behavior when text is already capitalized"""
        text = 'Python Programming'
        result_cap = cap.cap_text(text)
        result_multiple = cap.cap_multiple(text)
        self.assertEqual(result_cap, 'Python programming')  # capitalize() lowercases the rest
        self.assertEqual(result_multiple, 'Python Programming')

    def test_mixed_case_input(self):
        """Test behavior with mixed case input"""
        text = 'hELLo WoRLd'
        result_cap = cap.cap_text(text)
        result_multiple = cap.cap_multiple(text)
        self.assertEqual(result_cap, 'Hello world')
        self.assertEqual(result_multiple, 'Hello World')

    def test_numbers_and_special_characters(self):
        """Test behavior with numbers and special characters"""
        text = 'hello world123 test-case'
        result_cap = cap.cap_text(text)
        result_multiple = cap.cap_multiple(text)
        self.assertEqual(result_cap, 'Hello world123 test-case')
        self.assertEqual(result_multiple, 'Hello World123 Test-Case')


if __name__=='__main__':
    unittest.main()
