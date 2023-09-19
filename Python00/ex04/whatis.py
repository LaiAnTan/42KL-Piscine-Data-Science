import sys as sys


def main():

    if len(sys.argv) < 2:
        return

    try:
        assert len(sys.argv) == 2, "more than one argument is provided"
        assert sys.argv[1].isdigit() is True, "argument is not an integer"
    except AssertionError as err:
        print("AssertionError: " + err.args[0])
        return

    print("Im Even!" if abs(int(sys.argv[1]) % 2 == 0) else "Im Odd!")


if __name__ == "__main__":
    main()
