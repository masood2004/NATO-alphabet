import pandas as pd

# Load the NATO phonetic alphabet from CSV
phonetic_df = pd.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary to map each letter to its phonetic code
phonetic_dict = {row['letter']: row['code']
                 for index, row in phonetic_df.iterrows()}


def get_phonetic_spelling(word):
    """
    Given a word, returns its phonetic spelling using the NATO phonetic alphabet.
    Non-alphabetic characters are ignored.
    """
    # Convert the word to uppercase to match the dictionary keys
    word = word.upper()

    # List to store the phonetic codes for each letter
    phonetic_spelling = []

    # Loop through each letter in the word
    for letter in word:
        # Ignore non-alphabetic characters
        if letter.isalpha():
            # Using get() to avoid KeyErrors
            phonetic_spelling.append(phonetic_dict.get(letter, f"[{letter}]"))
        else:
            # Show non-alphabet characters as is
            phonetic_spelling.append(f"[{letter}]")

    return phonetic_spelling


def main():
    """
    Main function that handles user interaction, providing an option to enter words and displaying their phonetic spelling.
    """
    print("Welcome to the NATO Phonetic Alphabet Converter!")
    print("Enter a word or phrase, and I will show you its phonetic spelling.")
    print("Type 'exit' to quit the program.")

    while True:
        # Get user input
        word = input("\nEnter a word or phrase: ")

        # Check if the user wants to exit
        if word.lower() == 'exit':
            print("Goodbye!")
            break

        # Get the phonetic spelling of the word
        phonetic_spelling = get_phonetic_spelling(word)

        # Display the result
        print("\nPhonetic Spelling:")
        print(" ".join(phonetic_spelling))


if __name__ == "__main__":
    main()
