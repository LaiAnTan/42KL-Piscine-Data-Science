from abc import ABC, abstractmethod


class Character(ABC):

    """Abstract Character Class"""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """
        Abstract class constructor, cannot be called directly.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Die abstract method.
        """
        pass


class Stark(Character):

    """Stark Child Class"""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """
        Stark class Constructor.
        Initializes first_name and is_alive instance variables.

        @return None
        """
        super().__init__(first_name, is_alive)

    def die(self) -> None:
        """
        Makes a character die by setting the is_alive to False.

        @return None
        """
        self.is_alive = False
