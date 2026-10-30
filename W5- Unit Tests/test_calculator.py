#Testing the square function with pytest
import pytest
from calculator import square

#Checking positive numbers, zero, and negative numbers
def test_square():
    assert square(3) == 9
    assert square(2) == 4
    assert square(0) == 0
    assert square(-2) == 4
    assert square(-3) == 9

#Checking that a string raises a TypeError
def test_str():
    with pytest.raises(TypeError):
        square("cat")
