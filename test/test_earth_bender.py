import io
import os
import re
import sys
from decimal import Decimal
from typing import AnyStr
from unittest.mock import patch

import pytest
from hypothesis import example, given
from hypothesis import strategies as st

from tlab.earth_bender import EarthBender
from tlab.exceptions import InvalidPowerTypeError, InvalidPowerValueError

from .conftest import NEGETIVE_INTEGERS, POSITIVE_INTEGERS

_ROCK_ATTACK_PATTERN: re.Pattern[AnyStr] = re.compile(
    r"rock ball",
    re.IGNORECASE,
)


@given(
    name=st.text(),
    power=POSITIVE_INTEGERS,
)
@example(name="Toph", power=1)
@example(name="Toph", power=0)
def test_ctor_sets_properties_on_valid_values(
    name: str,
    power: int,
) -> None:
    # Act.
    toph = EarthBender(name, power)

    # Assert.
    assert toph.skill == "Earthbending"
    assert toph.name == name
    assert toph.power == power


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
        EarthBender("Toph", power)


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
        EarthBender("Toph", power)


@given(
    new_name=st.text(),
)
def test_name_setter_on_valid_value(
    new_name: str,
) -> None:
    # Arrange.
    toph = EarthBender("Toph", 90)

    # Act.
    toph.name = new_name

    # Assert.
    assert toph.name == new_name


@given(
    new_power=POSITIVE_INTEGERS,
)
@example(new_power=1)
@example(new_power=0)
def test_power_setter_on_valid_value(
    new_power: int,
) -> None:
    # Arrange.
    toph = EarthBender("Toph", 90)

    # Act.
    toph.power = new_power

    # Assert.
    assert toph.power == new_power


@given(
    new_power=NEGETIVE_INTEGERS,
)
def test_power_setter_failes_on_invalid_value(
    new_power: int,
) -> None:
    # Arrange.
    toph = EarthBender("Toph", 90)

    # Act & assert.
    with pytest.raises(
        InvalidPowerValueError,
        match="Power level must be a positive integer",
    ):
        toph.power = new_power


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
    toph = EarthBender("Toph", 90)

    # Act & assert.
    with pytest.raises(
        InvalidPowerTypeError,
        match="Power level must be a positive integer",
    ):
        toph.power = new_power


@given(
    power=POSITIVE_INTEGERS,
    rock_ball_attack_str=st.from_regex(
        _ROCK_ATTACK_PATTERN,
        fullmatch=True,
    ),
)
def test_can_use_earthbending_rock_ball(
    rock_ball_attack_str: str,
    power: int,
) -> None:
    # Arrange.
    toph = EarthBender("Toph", power)
    env_mock = patch.dict(
        os.environ,
        {"EARTH_ATTACK": rock_ball_attack_str},
        clear=True,
    )
    stdout_mock = patch.object(
        sys,
        "stdout",
        new=io.StringIO(),
    )

    # Act.
    with env_mock, stdout_mock:
        toph.bend()

    # Assert.
    assert stdout_mock.new.getvalue() == f"rock ball with power: {power:^2}."


@given(
    earth_attack=st.text(
        alphabet=st.characters(
            codec="UTF",
            # Removed wierd categories to avoid wierd errors
            # when patching envs.
            exclude_categories={
                "Cc",
            },
        ),
    ).filter(
        lambda earth_attack: not re.fullmatch(
            _ROCK_ATTACK_PATTERN,
            earth_attack,
        ),
    ),
)
def test_can_use_earthbending_other_than_rock_ball(earth_attack: str) -> None:
    # Arrange.
    toph = EarthBender("Toph", 66)
    env_mock = patch.dict(
        os.environ,
        {"EARTH_ATTACK": earth_attack},
        clear=True,
    )

    # Act.
    with env_mock:
        toph.bend()
        result = os.environ["EARTH_ATTACK"]

    # Assert.
    assert result == "No Rock Ball :("
