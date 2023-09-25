

class calculator:

    """
    Calculator class that allows for vector - scalar operations.
    """

    def __init__(self, lst: list[int | float]) -> None:
        """
        Calculator class constructor.

        Initialises the class with a vector.

        @param lst: a vector
        @return None
        """
        self.vector = lst

    def __add__(self, object) -> None:
        """
        Adds a vector with a scalar.

        @return None
        """
        for i in range(len(self.vector)):
            self.vector[i] += object
        print(self.vector)

    def __mul__(self, object) -> None:
        """
        Multiplies a vector with a scalar.

        @param object: scalar in the form of int or float
        @return None
        """
        for i in range(len(self.vector)):
            self.vector[i] *= object
        print(self.vector)

    def __sub__(self, object) -> None:
        """
        Subtracts a vector by a scalar.

        @param object: scalar in the form of int or float
        @return None
        """
        for i in range(len(self.vector)):
            self.vector[i] -= object
        print(self.vector)

    def __truediv__(self, object) -> None:
        """
        Divides a vector by a scalar.

        @param object: scalar in the form of int or float
        @return None
        @raise AssertionError: when dividing by zero
        """
        assert object != 0, "Cannot divide by zero"
        for i in range(len(self.vector)):
            self.vector[i] /= object
        print(self.vector)
