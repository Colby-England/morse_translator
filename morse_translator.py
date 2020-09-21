import csv


def get_dictionary(language):
    with open("morse.csv") as csvfile:
        reader = csv.reader(csvfile)
        english_to_morse = dict(reader)

    morse_to_english = dict((value, key) for key, value in english_to_morse.items())

    if language == "English":
        return english_to_morse
    else:
        return morse_to_english


def engl_to_morse(english_phrase):
    translating_dictionary = get_dictionary("English")
    translation = ""

    for char in english_phrase:
        if char == " ":
            translation += "/"
        else:
            translation += translating_dictionary[char.upper()]
        translation += " "
    return translation


def morse_to_engl(morse_pharse):
    translating_dictionary = get_dictionary("Morse")
    translation = ""
    morse_words = morse_pharse.split(" / ")

    for morse_word in morse_words:
        letters = morse_word.split(" ")
        for letter in letters:
            translation += translating_dictionary[letter]
        translation += " "
    return translation
