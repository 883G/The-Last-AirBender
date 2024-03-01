from webbrowser import BaseBrowser


class WaterBender:
    # Return type is None due to: https://peps.python.org/pep-0484/#the-meaning-of-annotations
    def __init__(
        self,
        name: str,
        power: int,
        browser: BaseBrowser | None = None
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
