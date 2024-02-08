import io
import sys
from decimal import Decimal

import pytest
from hypothesis import given
from hypothesis import strategies as st

from tlab.air_bender import AirBender
from tlab.exceptions import InvalidPowerType, InvalidPowerValue

from .conftest import NEGETIVE_INTEGERS, POSITIVE_INTEGERS


class TestAirBender:
    @given(
        name=st.text(),
        power=POSITIVE_INTEGERS,
    )
    def test_ctor_sets_properties_on_valid_values(
        self,
        name: str,
        power: int,
    ) -> None:
        # Act.
        aang = AirBender(name, power)

        # Assert.
        assert aang.skill == "Airbending"
        assert aang.name == name
        assert aang.power == power

    @given(
        power=NEGETIVE_INTEGERS,
    )
    def test_ctor_requires_power_of_positive_int_and_fails_on_negetive_int(
        self,
        power: int,
    ) -> None:
        # Act & Assert.
        with pytest.raises(
            InvalidPowerValue,
            match="Power level must be a positive integer",
        ):
            AirBender("Aang", power)

    @given(
        power=st.one_of(
            st.booleans(),
            st.floats(),
            st.decimals(),
            st.text(),
        ),
    )
    def test_ctor_requires_power_of_positive_int_and_failes_on_non_int(
        self,
        power: str | bool | float | Decimal,
    ) -> None:
        # Act & Assert.
        with pytest.raises(
            InvalidPowerType,
            match="Power level must be a positive integer",
        ):
            AirBender("Aang", power)

    def test_can_use_airbending(self) -> None:
        aang = AirBender("Aang", 90)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        aang.bend()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Aang is using his airbending skill!\n"
