
def count_in_list(lst: list[str], s: str) -> int:
    """
    A function that returns the number of occurences of a string in a list
    of strings.

    @param lst: list of strings
    @param s: string to match
    @return count: number of occurences of s in lst
    """
    return sum(1 for elem in lst if elem == s)


if __name__ == "__main__":
    assert count_in_list([], "Hello") == 0
    assert count_in_list([], "") == 0
    assert count_in_list(["test", "test", "test"], "test") == 3
    assert count_in_list(["baba", "bobo", "bubu"], "bebe") == 0
    assert count_in_list(["foo", "bar", "baz"], "foo") == 1
