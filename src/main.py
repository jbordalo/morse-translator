import morse

morse_code = ''
natural_language = ''


# Show output
def show(morse_sentence, natural_sentence):
    print("\nMorse code: {}".format(morse_sentence))
    print("Natural language: {}\n".format(natural_sentence))


def main():
    sentence = input("Input a string: ").strip()

    try:
        # Sentence is in morse code (cheap solution)
        if (sentence[0] == '.' or sentence[0] == '-'):
            morse_code = sentence
            natural_language = morse.translateToNatural(sentence)
        # Sentence is in natural language
        else:
            natural_language = sentence
            morse_code = morse.translateToMorse(sentence)
    except:
        # We got a parsing error
        print("There was an error with your input\n")
        exit(1)

    # Show the output
    show(morse_code, natural_language)

    return 0


while (1):
    main()
