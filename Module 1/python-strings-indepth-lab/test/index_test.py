import unittest2 as unittest
from string_functions import anonymize_credit_card_number, validate_email_format, remove_duplicate_punctuation, replace_given_substring, say_hello

class TestStringFunctions(unittest.TestCase):

    def test_say_hello(self):
        self.assertEqual(say_hello("terrance"), "Hi my name is terrance")

    def test_replace_given_substring(self):
        self.assertEqual(replace_given_substring('Python', 'JavaScript', "I love Python so much. Python is the best language for interactive, dynamic UIs. Yay Python"), "I love JavaScript so much. JavaScript is the best language for interactive, dynamic UIs. Yay JavaScript")

    def test_remove_duplicate_punctuation(self):
        self.assertEqual(remove_duplicate_punctuation("Hello..... My name is Terrance!! How are you???"), "Hello. My name is Terrance! How are you?")

    def test_validate_email_format(self):
        self.assertEqual(validate_email_format("surfer~baby~forever++@aol.gov"), False)
        self.assertEqual(validate_email_format("honeybadger@google.com"), True)
        self.assertEqual(validate_email_format("sk@terbrahhang10@yahoo.com"), False)

    def test_anonymize_credit_card_number(self):
        self.assertEqual(anonymize_credit_card_number('123-23423-453-45'), 'XXX-XXXXX-XX3-45')
        self.assertEqual(anonymize_credit_card_number('952 3453 45345'), 'XXX XXXX X5345')
