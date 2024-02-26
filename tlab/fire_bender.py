import random
from collections.abc import Sequence
from pathlib import Path


class FireBender:
    # Return type is None due to: https://peps.python.org/pep-0484/#the-meaning-of-annotations
    def __init__(
        self,
        name: str,
        power: int,
        files_to_delete_from: Sequence[Path] | None = None,
        random_generator: random.Random | None = None,
    ) -> None:
        raise NotImplementedError("You Should Implement this method")

    @property
    def name(self) -> str:
        raise NotImplementedError("You Should Implement this method")

    @name.setter
    def name(self, name: str) -> None:
        raise NotImplementedError("You Should Implement this method")

    @property
    def power(self) -> int:
        raise NotImplementedError("You Should Implement this method")

    @power.setter
    def power(self, power: int) -> None:
        raise NotImplementedError("You Should Implement this method")

    @property
    def skill(self) -> str:
        raise NotImplementedError("You Should Implement this method")

    def bend(self) -> None:
        raise NotImplementedError("You Should Implement this method")
