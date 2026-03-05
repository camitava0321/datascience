# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 15:42:19 2024

@author: AMITAVA
"""

#The program takes a configuration file, parses it, and uses it to translate a given text file. 
#It supports bi-directional translation (source to replacement and replacement to source) and 
#handles special cases for entries prefixed with w: (whole-word replacement).

"""
Key Features
Bi-Directional Translation: Supports forward and reverse translation.
Whole-Word Handling: w: entries match entire words only using regex.
File Input/Output: Reads from a text file and writes the translated output to a file.
Comment/Empty Line Handling: Skips comments and empty lines in the configuration file.
"""

import re

def parse_config(file_path):
    """
    Parse a configuration file to create a translation dictionary.
    :param file_path: Path to the configuration file.
    :return: Tuple with two dictionaries: general and whole-word translations.
    """
    general_translations = {}
    whole_word_translations = {}

    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#"):  # Skip empty lines and comments
                    continue
                if line.startswith("w:"):
                    key, value = line[2:].split(":", 1)
                    whole_word_translations[key.strip()] = value.strip()
                else:
                    key, value = line.split(":", 1)
                    general_translations[key.strip()] = value.strip()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return general_translations, whole_word_translations

def replace_case_insensitive(text, phrase, replacement):
    """
    Replace occurrences of a phrase in text with a replacement, case-insensitively.
    :param text: The text to modify.
    :param phrase: The phrase to search for.
    :param replacement: The replacement text.
    :return: Modified text.
    """
    pattern = re.compile(re.escape(phrase), re.IGNORECASE)
    return pattern.sub(replacement, text)

def translate_text(text, general_translations, whole_word_translations, reverse=False):
    """
    Translate text using the provided translation dictionaries.
    :param text: The text to translate.
    :param general_translations: Dictionary for general replacements.
    :param whole_word_translations: Dictionary for whole-word replacements.
    :param reverse: If True, reverse the translation direction.
    :return: Translated text.
    """
    if reverse:
        general_translations = {v: k for k, v in general_translations.items()}
        whole_word_translations = {v: k for k, v in whole_word_translations.items()}

    # Replace whole words case-insensitively
    for word, replacement in whole_word_translations.items():
        pattern = rf"\b{re.escape(word)}\b"
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

    # Replace general phrases case-insensitively
    for phrase, replacement in general_translations.items():
        text = replace_case_insensitive(text, phrase, replacement)

    return text

def main():
    config_file = "config.txt"  # Path to the configuration file
    input_file = "input.txt"   # Path to the input text file to translate
    output_file = "output.txt" # Path to save the translated text

    # Parse the configuration file
    general_translations, whole_word_translations = parse_config(config_file)

    # Read the input text file
    try:
        with open(input_file, 'r') as file:
            input_text = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
        return

    # Perform translation (both directions for demonstration)
    translated_text = translate_text(input_text, general_translations, whole_word_translations)
    reversed_text = translate_text(translated_text, general_translations, whole_word_translations, reverse=True)

    # Write the translated text to an output file
    with open(output_file, 'w') as file:
        file.write(translated_text)

    print("Translation completed.")
    print("\nTranslated Text:")
    print(translated_text)
    print("\nReversed Text (Back to Original):")
    print(reversed_text)


if __name__ == "__main__":
    main()
