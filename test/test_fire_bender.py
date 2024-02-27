import random
from decimal import Decimal
from unittest.mock import Mock

import pytest
from hypothesis import example, given
from hypothesis import strategies as st

from tlab.exceptions import InvalidPowerTypeError, InvalidPowerValueError
from tlab.fire_bender import FireBender

from .conftest import NEGETIVE_INTEGERS, POSITIVE_INTEGERS


@given(
    name=st.text(),
    power=POSITIVE_INTEGERS,
)
@example(name="Zuko", power=1)
@example(name="Zuko", power=0)
def test_ctor_sets_properties_on_valid_values(
    name: str,
    power: int,
) -> None:
    # Act.
    zuko = FireBender(name, power)

    # Assert.

    assert zuko.skill == "Firebending"
    assert zuko.name == name
    assert zuko.power == power


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
        FireBender("Zuko", power)


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
        FireBender("Zuko", power)


@given(
    new_name=st.text(),
)
def test_name_setter_on_valid_value(
    new_name: str,
) -> None:
    # Arrange.
    zuko = FireBender("Zuko", 90)

    # Act.
    zuko.name = new_name

    # Assert.
    assert zuko.name == new_name


@given(
    new_power=POSITIVE_INTEGERS,
)
@example(new_power=1)
@example(new_power=0)
def test_power_setter_on_valid_value(
    new_power: int,
) -> None:
    # Arrange.
    zuko = FireBender("Zuko", 90)

    # Act.
    zuko.power = new_power

    # Assert.
    assert zuko.power == new_power


@given(
    new_power=NEGETIVE_INTEGERS,
)
def test_power_setter_failes_on_invalid_value(
    new_power: int,
) -> None:
    # Arrange.
    zuko = FireBender("Zuko", 90)

    # Act & assert.
    with pytest.raises(
        InvalidPowerValueError,
        match="Power level must be a positive integer",
    ):
        zuko.power = new_power


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
    zuko = FireBender("Zuko", 90)

    # Act & assert.
    with pytest.raises(
        InvalidPowerTypeError,
        match="Power level must be a positive integer",
    ):
        zuko.power = new_power


def test_can_use_firebending_on_sozins_comet() -> None:
    # Arrange.
    expected_value = 6
    mock_random = Mock(
        name="mock_random",
        spec_set=random.Random,
    )
    mock_random.randint.return_value = expected_value
    zuko = FireBender(
        "Zuko",
        90,
        mock_random,
    )

    # Act.
    with pytest.raises(SystemExit) as exec_info:
        zuko.bend()

    # Assert.
    mock_random.randint.assert_called_once_with(
        0,
        6,
    )
    assert exec_info.value.code == expected_value


def test_can_use_firebending_on_eclipse() -> None:
    # Arrange.
    mock_random = Mock(
        name="mock_random",
        spec_set=random.Random,
    )
    mock_random.randint.return_value = 0
    zuko = FireBender(
        "Zuko",
        90,
        mock_random,
    )

    # Act.
    zuko.bend()

    # Assert.
    mock_random.randint.assert_called_once_with(
        0,
        6,
    )
    assert zuko.name == "dead"


@given(
    generated_value=st.integers(
        min_value=1,
        max_value=5,
    ),
)
def test_can_use_firebending_on_regular_day(generated_value: int) -> None:
    # Arrange.
    mock_random = Mock(
        name="mock_random",
        spec_set=random.Random,
    )
    mock_random.randint.return_value = generated_value
    zuko = FireBender(
        "Zuko",
        90,
        mock_random,
    )

    # Act.
    zuko.bend()

    # Assert.
    mock_random.randint.assert_called_once_with(
        0,
        6,
    )
