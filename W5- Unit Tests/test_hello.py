#Testing the hello function with pytest
from hello import hello

#Checking a given name and the default value
def test_hello():
    assert hello("Mahir") == "Hello, Mahir"
    assert hello() == "Hello, world"
