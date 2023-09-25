from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):

    """King class that inherits from both Baratheon and Lannister"""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """
        Constructor for King class.

        Initializes a King object.

        @return None
        """
        super().__init__(first_name, is_alive)

    """
    Getters
    """

    def get_eyes(self) -> str:
        return self.eyes

    def get_hairs(self) -> str:
        return self.hairs

    """
    Setters
    """

    def set_eyes(self, eyes: str) -> None:
        self.eyes = eyes

    def set_hairs(self, hairs: str) -> None:
        self.hairs = hairs
