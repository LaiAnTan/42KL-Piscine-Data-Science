def ft_filter(function, iterable):
    """ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function is None:
        return [val for val in iterable if val is True]
    return iter([val for val in iterable if function(val) is True])
