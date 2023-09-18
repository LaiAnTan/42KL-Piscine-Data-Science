import sys as sys


def main():
    """
    Program that prints out the numbers of types of characters in a string
    provided as input.
    """
    assert len(sys.argv) < 3, "more than one argument is provided"

    if len(sys.argv) == 1:
        print("What is the text to count?")
        s = sys.stdin.readline()
    else:
        s = sys.argv[1]

    print(repr(s))
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    space_count = sum(1 for char in s if char.isspace())
    digit_count = sum(1 for char in s if char.isdigit())
    punct_count = (
        len(s) - upper_count - lower_count - space_count - digit_count
    )
    print(f"""The text contains {len(s)} characters:
{upper_count} upper letters
{lower_count} lower letters
{punct_count} punctuation marks
{space_count} spaces
{digit_count} digits""")


if __name__ == "__main__":
    main()
