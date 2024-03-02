from typing import Self
from webbrowser import BaseBrowser


class WaterBender:
    # Return type is None due to: https://peps.python.org/pep-0484/#the-meaning-of-annotations
    def __init__(
        self: Self,
        name: str,
        power: int,
        browser: BaseBrowser | None = None,
    ) -> None:
        raise NotImplementedError("You Should Implement this method")

    @property
    def name(self: Self) -> str:
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

    @power.setter
    def power(
        self: Self,
        power: int,
    ) -> None:

    @property
    def skill(
        self: Self,
    ) -> str:
    def bend(
        self: Self,
    ) -> None:
