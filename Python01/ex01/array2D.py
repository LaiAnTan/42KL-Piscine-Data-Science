import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    """
    Function that prints the shape of a 2d array, and then truncates it
    based on the start and end agruments.

    @param family: list to slice
    @param start: start of slice
    @param end: end of slice
    @return list(np_sliced): the sliced list
    """
    assert isinstance(family, list) and all([isinstance(elem, list) for elem in family]), "family parameter must be a 2d list"
    assert len(family) == [len(elem) for elem in family].count(len(family[0])), "inner lists not same size"

    
    np_family = np.array(family)
    # numpy slicing
    np_sliced = np_family[start:end]

    # get shape using .shape
    print(f"My shape is : {np_family.shape}")
    print(f"My new shape is : {np_sliced.shape}")

    # use .tolist to convert back to list
    return np_sliced.tolist()