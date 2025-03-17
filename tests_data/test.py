# python -m pytest -v -s tests_data/test.py
# python -m pytest -v
# pytest tests_data/test.py
import pytest
from services_data.init import RPG


class TestUM(RPG):
    def test_data():
        assert 1==1