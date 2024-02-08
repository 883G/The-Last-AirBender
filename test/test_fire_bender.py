#!/usr/bin/env python3

import io
import sys

from tlab.fire_bender import FireBender


class TestFireBender:
    def test_has_skill_and_power(self) -> None:
        ozai = FireBender("Ozai", 100)
        assert ozai.skill == "Firebending"
        assert ozai.power == 100

    def test_requires_int_power(self) -> None:
        ozai = FireBender("Ozai", 100)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        ozai.power = "not an integer"
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Power level must be an integer\n"

    def test_can_use_firebending(self) -> None:
        ozai = FireBender("Ozai", 100)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        ozai.use_firebending()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Ozai is using his firebending skill!\n"

    def test_inferno_attack(self) -> None:
        ozai = FireBender("Ozai", 100)
        enemy = "Aang"
        damage_dealt = ozai.inferno_attack(enemy)
        assert damage_dealt > 0

    def test_power_up(self) -> None:
        ozai = FireBender("Ozai", 100)
        initial_power = ozai.power
        ozai.power_up(30)
        assert ozai.power == initial_power + 30

    def test_roaring_flames(self) -> None:
        ozai = FireBender("Ozai", 100)
        enemy = "Zuko"
        defeated = ozai.roaring_flames(enemy)
        assert defeated
