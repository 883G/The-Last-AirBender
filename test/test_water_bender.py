#!/usr/bin/env python3

import io
import sys

from tlab.water_bender import WaterBender


class TestWaterBender:
    def test_has_skill_and_power(self) -> None:
        katara = WaterBender("Katara", 80)
        assert katara.skill == "Waterbending"
        assert katara.power == 80

    def test_requires_int_power(self) -> None:
        katara = WaterBender("Katara", 80)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        katara.power = "not an integer"
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Power level must be an integer\n"

    def test_can_use_waterbending(self) -> None:
        katara = WaterBender("Katara", 80)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        katara.use_waterbending()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Katara is using her waterbending skill!\n"

    def test_boost_power(self) -> None:
        katara = WaterBender("Katara", 80)
        katara.boost_power(20)
        assert katara.power == 100

    def test_freeze_enemy(self) -> None:
        katara = WaterBender("Katara", 80)
        enemy = "Fire Nation Soldier"
        frozen_enemy = katara.freeze_enemy(enemy)
        assert frozen_enemy == "Fire Nation Soldier (Frozen)"

    def test_heal_self(self) -> None:
        katara = WaterBender("Katara", 80)
        initial_health = katara.health
        katara.heal_self(30)
        assert katara.health == initial_health + 30
