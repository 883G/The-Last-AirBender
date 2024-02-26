import random
from decimal import Decimal
from pathlib import Path
from typing import TYPE_CHECKING
from unittest.mock import Mock, patch

import pytest
from hypothesis import example, given
from hypothesis import strategies as st

from tlab.exceptions import InvalidPowerTypeError, InvalidPowerValueError
from tlab.fire_bender import FireBender

from .conftest import NEGETIVE_INTEGERS, POSITIVE_INTEGERS

if TYPE_CHECKING:
    from collections.abc import Sequence


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


@given(
    st.sampled_from(
        [
            Path(".gitignore"),
            Path("README.md"),
            Path("My-File"),
        ],
    ),
)
def test_can_use_firebending_on_normal_condition(
    expected_file_to_be_deleted: Path,
) -> None:
    # Arrange.
    dummy_file_iterable: Sequence[Path] = (expected_file_to_be_deleted,)
    mock_random = Mock(
        name="mock_random",
        spec_set=random.Random,
    )
    mock_random.choice.return_value = expected_file_to_be_deleted
    unlink = patch.object(
        Path,
        "unlink",
        # Thanks to: https://stackoverflow.com/a/20258218/14030123
        autospec=True,
    )

    zuko = FireBender(
        "Zuko",
        90,
        dummy_file_iterable,
        mock_random,
    )

    # Act.
    with unlink as mock_unlink:
        zuko.bend()

    # Assert.
    mock_random.choice.assert_called_once_with(
        dummy_file_iterable,
    )
    mock_unlink.assert_called_once_with(
        expected_file_to_be_deleted,
    )
