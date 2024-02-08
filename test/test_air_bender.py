import io
import sys

from tlab.air_bender import AirBender


class TestAirBender:
    def test_has_skill_and_power(self) -> None:
        aang = AirBender("Aang", 90)
        assert aang.skill == "Airbending"
        assert aang.power == 90

    def test_requires_int_power(self) -> None:
        aang = AirBender("Aang", 90)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        aang.power = "not an integer"
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Power level must be an integer\n"

    def test_can_use_airbending(self) -> None:
        aang = AirBender("Aang", 90)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        aang.use_airbending()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Aang is using his airbending skill!\n"
