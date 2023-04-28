# Random Password Generator and Password Strength Checker

This is a Python project that consists of two programs: a random password generator and a password strength checker.

## Random Password Generator

The `password_generator.py` file generates a random password consisting of numbers, uppercase letters, lowercase letters, and special characters. The password is generated using the `random` module in Python, and the length of the password is fixed to 16 characters.

To run the program, simply execute the `password_generator.py` file. The program will generate a new password each time it is executed.

## Password Strength Checker

The `password_strength_checker.py` file checks the strength of a given password. The program tests the password against the following criteria:

- The password must be at least 8 characters long
- The password must contain at least one uppercase letter
- The password must contain at least one number
- The password must contain at least one special character (e.g., ~!@#$%^&*()_+-=[]{}|\:;"',.<>/?)

To run the program, execute the `password_strength_checker.py` file and enter the password when prompted. The program will then evaluate the password and output its strength.

## Platform-specific Notes

The `password_strength_checker.py` file uses the `os` module to clear the console screen. The program has been tested on Linux, macOS, and Windows platforms, and the appropriate clear command will be executed depending on the platform.

## Disclaimer

Please note that the password generator and password strength checker programs provided here are for personal use! Do NOT give your password to anyone and use unique passowrds for all of your accounts!

## License

These projects are licensed under the GNU General Public License. See the `LICENSE` file in the start of the repositor.
