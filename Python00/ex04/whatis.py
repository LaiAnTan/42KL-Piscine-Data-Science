import sys as sys


def isNumber(s: str) -> str:
    try:
        int(s)
        return True
    except ValueError:
        return False


def main():

    if len(sys.argv) < 2:
        return

    try:
        assert len(sys.argv) == 2, "more than one argument is provided"
        assert isNumber(sys.argv[1]), "argument is not an integer"
    except AssertionError as err:
        print("AssertionError: " + err.args[0])
        return

    print("Im Even!" if abs(int(sys.argv[1]) % 2 == 0) else "Im Odd!")


if __name__ == "__main__":
    main()
