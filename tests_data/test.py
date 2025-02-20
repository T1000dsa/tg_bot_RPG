# python -m pytest -v -s tests_data/test.py
# python -m pytest -v
import pytest
from services_data.init import RPG

data = RPG()
new_data = RPG()

class TestUM:
    def test_new(self):
        assert new_data.GAME_DATA== RPG.GAME_DATA
    def test_race(self):
        data.race_choice('human')
        new_data.race_choice('elf')
        print(data.data, new_data.data)
        assert data.data != new_data.data