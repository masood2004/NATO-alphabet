# NATO Phonetic Alphabet Converter

A simple Python program that converts words or phrases into their corresponding NATO phonetic alphabet spelling. The NATO phonetic alphabet is commonly used in aviation, military, and other fields to clarify spelling over radio or telephone.

## Features

- Converts input words or phrases into their NATO phonetic equivalents.
- Handles non-alphabetic characters and displays them as they are.
- User-friendly interface with error handling for unknown characters.
- Allows exiting the program via a simple command (`exit`).
- Outputs a clean and readable format for phonetic spelling.

## Requirements

- Python 3.x
- `pandas` library (used for reading the CSV file)

## Installation

To run this program, follow the steps below:

### Step 1: Clone the Repository

Clone this repository to your local machine using Git:

```bash
git clone https://github.com/masood2004/NATO-alphabet.git
```

### Step 2: Install Dependencies

Make sure you have Python 3 installed on your machine. Then, install the required dependencies using `pip`:

```bash
pip install pandas
```

### Step 3: Download the CSV File

The program requires the CSV file that contains the NATO phonetic alphabet. Make sure you have the file `nato_phonetic_alphabet.csv` in the root directory of the project. If the file is not available, you can download it from [this link](insert-link-here).

Alternatively, if you want to manually create the CSV, it should have the following structure:

```csv
letter,code
A,Alpha
B,Beta
C,Charlie
...
Z,Zulu
```

### Step 4: Run the Program

You can now run the program by executing the following command:

```bash
python phonetic_converter.py
```

The program will prompt you to enter a word or phrase. Enter your input, and it will return the phonetic spelling.

## Example Usage

Here is an example of how the program works:

```bash
Welcome to the NATO Phonetic Alphabet Converter!
Enter a word or phrase, and I will show you its phonetic spelling.
Type 'exit' to quit the program.

Enter a word or phrase: Hello World!
Phonetic Spelling:
Hotel Echo Lima Lima Oscar Whiskey Oscar Romeo Lima Delta !
```

### Handling Non-Alphabetic Characters

Non-alphabetic characters (such as punctuation or numbers) are ignored in the phonetic spelling but are displayed in square brackets. For example:

```bash
Enter a word or phrase: Hello, World!
Phonetic Spelling:
Hotel Echo Lima Lima Oscar , Whiskey Oscar Romeo Lima Delta !
```

## Functionality Breakdown

### `get_phonetic_spelling(word)`

This function takes a word or phrase as input and returns its phonetic spelling using the NATO phonetic alphabet. It handles:
- Converting the input to uppercase to match the phonetic dictionary.
- Ignoring non-alphabetic characters.
- Returning a list of phonetic codes for each letter.

### `main()`

The `main` function manages user interaction. It:
- Displays a welcome message and instructions.
- Prompts the user to input a word or phrase.
- Calls `get_phonetic_spelling()` and prints the phonetic spelling.
- Allows the user to exit the program by typing `exit`.

## Contributing

Feel free to fork this repository and submit pull requests for bug fixes, features, or improvements. Please ensure that your code adheres to Python's PEP 8 style guide and includes appropriate comments for clarity.

## License

This project is open-source and available under the MIT License.
