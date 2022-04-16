# pass-gen-check
Python CLI app to generate and validate passwords

# Password checker
Python console program validates password passed by the user as a command-line argument against a set of rules:
- The password contains both lowercase and uppercase characters 
- The password contains at least one digit
- The password contains at least one punctuation character
- The password is at least 14 characters long

To check your password run the command:
>python password_checker.py your_password

# Password generator
Python console program generates a strong random password with the following rules:
- Contains both lowercase and uppercase characters
- Contains at least one digit
- Contains at least one punctuation character (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
- Is at least 14 characters long

To generate new password run the command:
>python password_generator.py

# Requirements
Python version: 3.8 or higher