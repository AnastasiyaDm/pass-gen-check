from unittest import TestCase
import password_checker


class TestPasswordChecker(TestCase):
    def test_case_check(self):
        password_lower_only = 'admin'
        error_text = password_checker.ERRORS_DICT.get('case_check_error')
        result = password_checker.case_check(password_lower_only)
        self.assertEqual(result, error_text)

        password_upper_only = 'USER1'
        result = password_checker.case_check(password_upper_only)
        self.assertEqual(result, error_text)

        password_lower_upper = 'USERadmin'
        result = password_checker.case_check(password_lower_upper)
        self.assertTrue(result)

    def test_digit_check(self):
        password_digit_only = '453'
        error_text = password_checker.ERRORS_DICT.get('digit_check_error')
        result = password_checker.digit_check(password_digit_only)
        self.assertTrue(result)

        password_no_digit = 'USERadmin'
        result = password_checker.digit_check(password_no_digit)
        self.assertEqual(result, error_text)

        password_alphanumeric = 'User123'
        result = password_checker.digit_check(password_alphanumeric)
        self.assertTrue(result)

    def test_length_check(self):
        password_too_short = 'admin'
        error_text = password_checker.ERRORS_DICT.get('length_check_error')
        result = password_checker.length_check(password_too_short)
        self.assertEqual(result, error_text)

        password_valid = 'hdtfYbck765b!njhnb'
        result = password_checker.length_check(password_valid)
        self.assertTrue(result)

    def test_punctuation_check(self):
        password_invalid = 'djgkfdm8776fdgRbd'
        error_text = password_checker.ERRORS_DICT.get('punctuation_check_error')
        result = password_checker.punctuation_check(password_invalid)
        self.assertEqual(result, error_text)

        password_valid = 'djgkfd#m8776fdgRbd'
        result = password_checker.punctuation_check(password_valid)
        self.assertTrue(result)

    def test_validate_password(self):
        password_no_upper = 'djgkfd#m8776fdgbd'
        error_text = password_checker.ERRORS_DICT.get('case_check_error')
        result = password_checker.validate_password(password_no_upper)
        self.assertEqual(len(result), 1)
        self.assertIn(error_text, result)

        password_all_violations = 'admin'
        error_dict = list(password_checker.ERRORS_DICT.values())
        result = password_checker.validate_password(password_all_violations)
        self.assertEqual(len(result), len(error_dict))
        self.assertListEqual(result, error_dict)

        password_correct = 'My $tron9 pa$$word'
        result = password_checker.validate_password(password_correct)
        self.assertEqual(len(result), 0)


