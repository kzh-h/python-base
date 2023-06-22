"""Test calculation.py."""
from src.calclation import add_two_numbers


def test_add_two_numbers():
    """test."""
    assert add_two_numbers(augend=1, addend=2) == 3
