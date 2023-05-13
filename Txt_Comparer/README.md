# Txt Compare

This Python code analyzes two text files and calculates the percentage of words that differ between them.

## Getting Started

To run this code, follow the instructions below:

1. Clone the repository to your local machine.
2. Ensure that you have Python installed on your system.
3. Navigate to the directory containing the code file.

## Usage

To use this code, follow the instructions below:

1. Open the code file in a Python environment, such as Jupyter Notebook or Anaconda Prompt.
2. When prompted, enter the names of the two files you want to analyze. The files should be in text format.
3. The code will output the number of words that are the same in both files and the number of words that differ.
4. The code will also calculate the percentage of words that differ between the two files and output the results to the user.

## Code Description

The `Word_Counting` function takes a text file as input and returns a dictionary that contains the count of each word in the file. The function does the following:

1. Opens the text file in read mode using the `with` statement.
2. Reads each line of the file and removes any trailing newline characters.
3. Appends each line to the `Quotes` list if it is not empty.
4. Iterates through each quote in the `Quotes` list and splits it into words.
5. Appends each word to the `Word` list if it is not empty.
6. Creates a dictionary called `Count` to store the count of each word in the `Word` list.
7. Iterates through each word in the `Word` list and updates its count in the `Count` dictionary.

The `Sum_words_1` and `Sum_words_2` variables call the `Word_Counting` function on the two files specified by the user.

The code then iterates through the words in each file and compares their counts. The `same` variable tracks the number of words that are the same in both files, while the `different` variable tracks the number of words that differ. The code calculates the percentage of words that differ between the two files and outputs the results to the user.

## License

This repository is licensed under the GNU License. See the [LICENSE](LICENSE) file in the main pasta for more information.


