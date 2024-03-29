import random
from typing import Self


class FireBender:
    # Return type is None due to: https://peps.python.org/pep-0484/#the-meaning-of-annotations
    def __init__(
        self: Self,
        name: str,
        power: int,
        random_generator: random.Random = random,
    ) -> None:
        raise NotImplementedError("You Should Implement this method")

    @property
    def name(
        self: Self,
    ) -> str:
        raise NotImplementedError("You Should Implement this method")

    @name.setter
    def name(
        self: Self,
        name: str,
    ) -> None:
        raise NotImplementedError("You Should Implement this method")

    @property
    def power(
        self: Self,
    ) -> int:
        raise NotImplementedError("You Should Implement this method")

    @power.setter
    def power(
        self: Self,
        power: int,
    ) -> None:
        raise NotImplementedError("You Should Implement this method")

    @property
    def skill(
        self: Self,
    ) -> str:
        raise NotImplementedError("You Should Implement this method")

    def bend(
        self: Self,
    ) -> None:
        raise NotImplementedError("You Should Implement this method")
