import sys as sys
from ft_filter import ft_filter


def main():
    """
    Program that takes a string and a number as arguments,
    and then prints out the list of strings whose lengths are larger than the
    numbr passed in as argument.
    """
    assert (len(sys.argv) == 3 and
            sys.argv[2].isdigit()), "the arguments are bad"

    print([item for item in ft_filter(lambda x: len(x) > int(sys.argv[2]),
                                      sys.argv[1].split(" "))])


if __name__ == "__main__":
    main()
