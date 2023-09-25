import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Generates a random id.

    @return id
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


# a dataclass is kinda like a struct in c, storing state over logic
# (more attributes / variables in the class)
@dataclass
class Student:

    """Student Dataclass."""

    # init args
    name: str
    surname: str
    # default value args
    active: bool = True
    # non-init args
    # field(init=False) makes it so that login and id cannot be initialized
    login: str = field(init=False)
    id: str = field(init=False)

    # __post_init__ magic method is the last thing called by __init__
    # used to handle logic after initializing all the necessary attr in
    # a dataclass
    def __post_init__(self) -> None:
        """
        Magic method for handling post initialization logic.

        @return None
        """
        self.login = self.name[0].upper() + self.surname
        self.id = generate_id()
