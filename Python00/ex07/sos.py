import sys as sys


def main():
    """
    Program that encodes a string into morse code.
    """
    NESTED_MORSE = {
        ' ': '/',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----',
        }

    assert (len(sys.argv) == 2 and
            all(char.isalnum() or char == ' ' for char in sys.argv[1]) is True
            ), "the arguments are bad"

    print(" ".join([NESTED_MORSE[char] for char in sys.argv[1].upper()]))


if __name__ == "__main__":
    main()
