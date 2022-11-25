from morse_code import morse_code
code = morse_code

print("Hello there. This program was created in order to help you to convert the phrases into the morse code.\n")

phrase = input("Therefore, please insert your phrase below and press Enter: ")

phrase = phrase.upper()


def convert(text):
    global code
    converted_text = ""

    for char in text:
        if char in code:
            converted_text += code[char] + " "

    return converted_text


print(f"\nThe converted string is: {convert(phrase)}")



