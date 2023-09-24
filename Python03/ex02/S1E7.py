from S1E9 import Character


class Baratheon(Character):

    """Representing the Baratheon Family."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """
        Constructor for Baratheon class.

        Initializes a Baratheon object.

        @return None
        """
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self) -> None:
        """
        Makes a character die by setting the is_alive to False.

        @return None
        """
        self.is_alive = False

    def __str__(self) -> str:
        """
        __str__ magic method.

        @return str
        """
        return f"{self.first_name} {self.family_name} is \
{'alive' if self.is_alive is True else 'dead'} with \
{self.eyes} eyes and {self.hairs} hair."

    def __repr__(self) -> str:
        """
        __repr__ magic method.

        @return str
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):

    """Representing the Lannister Family."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """
        Constructor for Lannister class.

        Initializes a Lannister object.

        @return None
        """
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    @classmethod
    def create_lannister(self, first_name: str, is_alive: bool = True):
        """
        Creates a new instance of Lannister class.

        @return Lannister(): new Lannister object
        """
        return Lannister(first_name, is_alive)

    def die(self) -> None:
        """
        Makes a character die by setting the is_alive to False.

        @return None
        """
        self.is_alive = False

    def __str__(self) -> str:
        """
        __str__ magic method.

        @return str
        """
        return f"{self.first_name} {self.family_name} is \
{'alive' if self.is_alive is True else 'dead'} with \
{self.eyes} eyes and {self.hairs} hair."

    def __repr__(self) -> str:
        """
        __repr__ magic method.

        @return str
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
