from decimal import Decimal
from logging import INFO, LogRecord

import pytest
from hypothesis import example, given
from hypothesis import strategies as st

from tlab.air_bender import AirBender
from tlab.exceptions import InvalidPowerTypeError, InvalidPowerValueError

from .conftest import NEGETIVE_INTEGERS, POSITIVE_INTEGERS


@given(
    name=st.text(),
    power=POSITIVE_INTEGERS,
)
@example(name="Aang", power=1)
@example(name="Aang", power=0)
def test_ctor_sets_properties_on_valid_values(
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
    power: int,
) -> None:
    # Act & Assert.
    with pytest.raises(
        InvalidPowerValueError,
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
@example(power=True)
@example(power=False)
def test_ctor_requires_power_of_positive_int_and_failes_on_non_int(
    power: str | bool | float | Decimal,
) -> None:
    # Act & Assert.
    with pytest.raises(
        InvalidPowerTypeError,
        match="Power level must be a positive integer",
    ):
        AirBender("Aang", power)


@given(
    new_name=st.text(),
)
def test_name_setter_on_valid_value(
    new_name: str,
) -> None:
    # Arrange.
    aang = AirBender("Aang", 90)

    # Act.
    aang.name = new_name

    # Assert.
    assert aang.name == new_name


@given(
    new_power=POSITIVE_INTEGERS,
)
@example(new_power=1)
@example(new_power=0)
def test_power_setter_on_valid_value(
    new_power: int,
) -> None:
    # Arrange.
    aang = AirBender("Aang", 90)

    # Act.
    aang.power = new_power

    # Assert.
    assert aang.power == new_power


@given(
    new_power=NEGETIVE_INTEGERS,
)
def test_power_setter_failes_on_invalid_value(
    new_power: int,
) -> None:
    # Arrange.
    aang = AirBender("Aang", 90)

    # Act & assert.
    with pytest.raises(
        InvalidPowerValueError,
        match="Power level must be a positive integer",
    ):
        aang.power = new_power


@given(
    new_power=st.one_of(
        st.booleans(),
        st.floats(),
        st.decimals(),
        st.text(),
    ),
)
@example(new_power=True)
@example(new_power=False)
def test_power_setter_failes_on_invalid_type(
    new_power: str | bool | float | Decimal,
) -> None:
    # Arrange.
    aang = AirBender("Aang", 90)

    # Act & assert.
    with pytest.raises(
        InvalidPowerTypeError,
        match="Power level must be a positive integer",
    ):
        aang.power = new_power


def test_can_use_airbending(
    caplog: pytest.LogCaptureFixture,
) -> None:
    # Arrange.
    caplog.clear()
    caplog.set_level(INFO)
    aang = AirBender("Aang", 90)

    # Act.
    aang.bend()

    # Assert.
    assert len(caplog.records) == 1
    log_record: LogRecord = caplog.records[0]
    assert log_record.levelno == INFO
    assert log_record.message == "Aang is using his airbending skill!"
