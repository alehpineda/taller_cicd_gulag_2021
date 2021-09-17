import pytest

from main import suma

def test_suma_correcta():
    assert suma(1,1) == 2
