import os
from decimal import Decimal
from unittest.mock import Mock, patch
from webbrowser import BaseBrowser

import pytest
from hypothesis import example, given
from hypothesis import strategies as st

from tlab.exceptions import InvalidPowerTypeError, InvalidPowerValueError
from tlab.water_bender import WaterBender

from .conftest import NEGETIVE_INTEGERS, POSITIVE_INTEGERS


@given(
    name=st.text(),
    power=POSITIVE_INTEGERS,
)
@example(name="Katara", power=1)
@example(name="Katara", power=0)
def test_ctor_sets_properties_on_valid_values(
    name: str,
    power: int,
) -> None:
    # Act.
    katara = WaterBender(name, power)

    # Assert.

    assert katara.skill == "Waterbending"
    assert katara.name == name
    assert katara.power == power


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
        WaterBender("Katara", power)


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
        WaterBender("Katara", power)


@given(
    new_name=st.text(),
)
def test_name_setter_on_valid_value(
    new_name: str,
) -> None:
    # Arrange.
    katara = WaterBender("Katara", 90)

    # Act.
    katara.name = new_name

    # Assert.
    assert katara.name == new_name


@given(
    new_power=POSITIVE_INTEGERS,
)
@example(new_power=1)
@example(new_power=0)
def test_power_setter_on_valid_value(
    new_power: int,
) -> None:
    # Arrange.
    katara = WaterBender("Katara", 90)

    # Act.
    katara.power = new_power

    # Assert.
    assert katara.power == new_power


@given(
    new_power=NEGETIVE_INTEGERS,
)
def test_power_setter_failes_on_invalid_value(
    new_power: int,
) -> None:
    # Arrange.
    katara = WaterBender("Katara", 90)

    # Act & assert.
    with pytest.raises(
        InvalidPowerValueError,
        match="Power level must be a positive integer",
    ):
        katara.power = new_power


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
    katara = WaterBender("Katara", 90)

    # Act & assert.
    with pytest.raises(
        InvalidPowerTypeError,
        match="Power level must be a positive integer",
    ):
        katara.power = new_power


@given(
    power=POSITIVE_INTEGERS,
)
def test_can_use_waterbending_on_regular_day(power: int) -> None:
    # Arrange.
    mock_browser = Mock(
        name="mock_browser",
        spec_set=BaseBrowser,
    )
    env_mock = patch.dict(
        os.environ,
        {},
        clear=True,
    )
    katara = WaterBender(
        "Katara",
        power,
        mock_browser,
    )

    # Act.
    with env_mock:
        katara.bend()

    # Assert.
    mock_browser.open_new.assert_called_once_with(
        f"https://youtu.be/gk-aCL6eyGc?si=XX45XZzc3a8uCN0o&t={power}",
    )


def test_can_use_waterbending_on_full_moon() -> None:
    # Arrange.
    mock_browser = Mock(
        name="mock_browser",
        spec_set=BaseBrowser,
    )
    env_mock = patch.dict(
        os.environ,
        {
            "MOON": "FULL",
        },
        clear=True,
    )
    katara = WaterBender(
        "Katara",
        90,
        mock_browser,
    )

    # Act.
    with env_mock:
        katara.bend()

    # Assert.
    mock_browser.open_new.assert_called_once_with(
        "https://www.wikiwand.com/en/6",
    )

# TODO: create env string strategy.
@given(moon_env_value=st.text())
def test_can_use_waterbending_on_no_moon(
    moon_env_value: str,
) -> None:
    # Arrange.
    mock_browser = Mock(
        name="mock_browser",
        spec_set=BaseBrowser,
    )
    env_mock = patch.dict(
        os.environ,
        {
            "MOON": moon_env_value,
        },
        clear=True,
    )
    katara = WaterBender(
        "Katara",
        90,
        mock_browser,
    )

    # Act.
    with env_mock:
        katara.bend()

    # Assert.
    mock_browser.open_new.assert_called_once_with(
        "https://youtu.be/weZKm1kTrpc?si=_Unblsn5tPvzwfs7",
    )


@given(
    power=st.integers(
        min_value=1,
    ),
)
def test_can_use_waterbending_on_no_webbrowser_and_non_zero_power(power: int) -> None:
    # Arrange.
    katara = WaterBender(
        "Katara",
        power,
        None,
    )

    # Act.
    katara.bend()

    # Assert.
    assert katara.power == power - 1


def test_can_use_waterbending_on_no_webbrowser_and_zero_power() -> None:
    # Arrange.
    start_power: int = 0
    katara = WaterBender(
        "Katara",
        start_power,
        None,
    )

    # Act.
    katara.bend()

    # Assert.
    assert katara.power == start_power
