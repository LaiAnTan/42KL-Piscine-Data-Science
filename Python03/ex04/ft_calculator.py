
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

        @param object: scalar in the form of int or float
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

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Static method to calculate the dot product between two vectors.

        @param V1: first vector
        @param V2: second vector
        @return None
        """
        dp = sum([(elem1 * elem2) for elem1, elem2 in zip(V1, V2)])
        print(f"Dot product is : {dp}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Static method to calculate the addition of two vectors.

        @param V1: first vector
        @param V2: second vector
        @return None
        """
        res = [float(elem1 + elem2) for elem1, elem2 in zip(V1, V2)]
        print(f"Add Vector is : {res}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Static method to calculate the subtraction of two vectors.

        @param V1: first vector
        @param V2: second vector
        @return None
        """
        res = [float(elem1 - elem2) for elem1, elem2 in zip(V1, V2)]
        print(f"Sous Vector is : {res}")
