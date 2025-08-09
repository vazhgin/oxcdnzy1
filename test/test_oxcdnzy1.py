import pytest

@pytest.fixture()
def before_after():
    print("before test")
    yield
    print("\nafter test")




def test1():
    assert 1==1

def test2(before_after):
    assert 2==1