import sys as sys


def main():

    assert len(sys.argv) == 2, "more than one argument is provided"

    assert isinstance(sys.argv[1], int) is False, "argument is not an integer"

    print("Im Even!" if abs(int(sys.argv[1]) % 2 == 0) else "Im Odd!")


if __name__ == "__main__":
    main()
