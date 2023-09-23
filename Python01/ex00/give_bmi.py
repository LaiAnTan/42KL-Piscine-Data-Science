import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Function that computes a list of bmi values based on lists of heights and
    weights.

    @param height: list of heights
    @param weight: list of weights
    @return np_bmi.tolist(): list of bmis
    @raise AssertionError: if lists are different sizes
    @raise AssertionError: if elements in lists are not int or float
    """

    assert len(height) == len(weight), "lists are different sizes"
    # used set union because it was the only way to combine both lists
    # and return it
    assert (all(isinstance(elem, (int, float)) for elem in
            set(height).union(weight))), "elements in list must be int \
or float"

    np_height = np.array(height)
    np_weight = np.array(weight)

    # broadcasting in numpy allows element-wise operations (scalar / matrix)
    # eg. each element in np_heights is squared
    # eg2. each element in np_weights is divided by an element with
    # the coresponding position in the squared np_heights
    np_bmi = np_weight / (np_height ** 2)
    return np_bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Function that returns a list of booleans on whether a number in the list
    is larger than the limit.

    @param bmi: list of bmis
    @param limit: limit
    @return np_bool.tolist(): boolean list
    @raise AssertionError: if elements in lists are not int or float
    """

    assert all(isinstance(elem, (int, float)) for elem in bmi), \
        "elements in list must be int or float"

    np_bmi = np.array(bmi)

    # broadcasting also allows element-wise comparisons
    np_bool = np_bmi > limit
    return np_bool.tolist()
