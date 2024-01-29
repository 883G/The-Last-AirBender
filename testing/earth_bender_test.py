#!/usr/bin/env python3

from earth_bender import EarthBender

import io
import sys

class TestEarthBender:
    
    def test_has_skill_and_power(self):
        toph = EarthBender("Toph", 95)
        assert(toph.skill == "Earthbending")
        assert(toph.power == 95)

    def test_requires_int_power(self):
        toph = EarthBender("Toph", 95)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        toph.power = "not an integer"
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Power level must be an integer\n"

    def test_can_use_earthbending(self):
        toph = EarthBender("Toph", 95)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        toph.use_earthbending()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Toph is using her earthbending skill!\n")

    def test_enhance_power(self):
        toph = EarthBender("Toph", 95)
        toph.enhance_power(20)  
        assert(toph.power == 115)  

    def test_special_ability(self):
        toph = EarthBender("Toph", 95)
        special_ability_result = toph.special_ability()
        assert(special_ability_result == "Toph uses seismic sense to detect hidden objects!")

