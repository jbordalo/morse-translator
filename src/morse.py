from dictionary import MORSE_TO_NATURAL as MORSE, NATURAL_TO_MORSE as NATURAL


# Translate from natural language to morse code
def translateToMorse(sentence):
    translation = ''

    for letter in sentence:
        translation += NATURAL[letter.upper()]
        # Add a space after each letter
        translation += ' '

    return translation


# Translate from morse code to natural language
def translateToNatural(sentence):
    translation = ''

    # Create array of morse 'letters'
    letters = sentence.split()

    for letter in letters:
        translation += MORSE[letter]

    return translation
