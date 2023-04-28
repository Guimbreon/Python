# Binary Translator in Python

This project contains two Python scripts for translating text to binary and vice versa.

## Usage

### Binary to Text Translator

1. Navigate to the `Binary` folder in your terminal or command prompt.
2. Run the `binary_to_text.py` script using the command `python binary_to_text.py`.
3. Enter the binary code you want to translate.
4. The translated text will be displayed in the console.

### Text to Binary Translator

1. Navigate to the `Binary` folder in your terminal or command prompt.
2. Run the `text_to_binary.py` script using the command `python text_to_binary.py`.
3. Enter the text you want to translate.
4. The translated binary code will be displayed in the console.

## Files

### `binary_to_text.py`

This file contains the Python script for translating binary code to text. The script first reads the translation library from the `Keys` file, where each line is formatted as `character:binary_code`. The binary code is then read from the user, and translated into text using the translation library.

### `text_to_binary.py`

This file contains the Python script for translating text to binary code. The script reads the translation library from the `Keys` file, where each line is formatted as `character:binary_code`. The text is then read from the user, and translated into binary code using the translation library.

### `Keys`

This file contains the translation library used by the Python scripts. Each line in the file is formatted as `character:binary_code`, with one entry per line. The `binary_to_text.py` script uses the `character` as a key to translate binary code to text, while the `text_to_binary.py` script uses the `binary_code` as a key to translate text to binary code.

## Contributions

Contributions to this project are welcome. If you have any ideas for improving the project or find any issues, please submit an issue or pull request on the GitHub repository.

## License

These projects are licensed under the GNU General Public License. See the `LICENSE` file in the start of the repositor.
