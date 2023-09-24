def square(x: int | float) -> int | float:
    return x ** 2


def pow(x: int | float) -> int | float:
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Outer function.

    @param x: an integer to apply the function on
    @param function: a function
    @return inner: function object that when called executes function(x)
    """
    count = 0

    def inner() -> float:
        """
        Inner function
        
        @return res: result when function(save) is called count times.
        """
        nonlocal count # to change outer variables nonlocal is required
        count += 1
        res = x # get original value
        for _ in range(count):
            res = function(res)
        return res

    return inner