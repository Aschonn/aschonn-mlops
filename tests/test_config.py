#has to start with test
#Creates a function to test a specific feature
import pytest
class NotInRange(Exception):
    def __init__(self, message = "Value not in range"):
        self.message = message
        super().__init__(self.message)

def test_whatever():
    a = 2
    with pytest.raises(NotInRange):
        if a not in range(10,20):
            raise NotInRange

def test_something():
    a = 2
    b = 3
    assert a != b


def test_something_AGAIN():
    a = 2
    b = 3
    assert a != b