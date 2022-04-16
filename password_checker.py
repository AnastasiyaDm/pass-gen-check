import string
import sys


ERRORS_DICT = {'length_check_error': '- The password must be at least 14 characters long',
               'case_check_error': '- The password must contain both lowercase and uppercase characters',
               'digit_check_error': '- The password must contain at least one digit',
               'punctuation_check_error': f'- The password must contain at least one punctuation '
                                          f'character ({string.punctuation})'}


def case_check(password):
    lower_check = any(letter.islower() for letter in password)
    upper_check = any(letter.isupper() for letter in password)
    return True if lower_check and upper_check \
        else ERRORS_DICT.get('case_check_error')


def digit_check(password):
    number_check = any(number.isdigit() for number in password)
    return True if number_check else ERRORS_DICT.get('digit_check_error')


def length_check(password):
    return True if len(password) >= 14 else ERRORS_DICT.get('length_check_error')


def punctuation_check(password):
    check_punctuation = any(symbol in string.punctuation for symbol in password)
    return True if check_punctuation else ERRORS_DICT.get('punctuation_check_error')


def validate_password(password):
    check_list = [length_check(password),
                  case_check(password),
                  digit_check(password),
                  punctuation_check(password)]
    check_result_list = [check for check in check_list if check is not True]
    return check_result_list


if __name__ == '__main__':
    if len(sys.argv) == 2:
        password = sys.argv[1]
        result = validate_password(password)
        if not result:
            print('Strong password')
        else:
            print('Weak password:')
            print(*result, sep='\n')
    elif len(sys.argv) > 2:
        print('Password contains whitespaces so it must be wrapped with quotes!')
    else:
        print('Password must be not empty!')
        print(*ERRORS_DICT.values(), sep='\n')
