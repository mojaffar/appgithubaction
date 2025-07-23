from src.math_operations import add, sub
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_sub():
    assert sub(5, 3) == 2
    assert sub(0, 0) == 0
    assert sub(10, 5) == 5
    assert sub(3, 5) == -2

def test_sub_negative():
    assert sub(-5, -3) == -2
    assert sub(-3, -5) == 2
    assert sub(-1, 1) == -2
    assert sub(1, -1) == 2

def test_add_negative():
    assert add(-5, -3) == -8
    assert add(-3, -5) == -8
    assert add(-1, 1) == 0
    assert add(1, -1) == 0

def test_add_zero():
    assert add(0, 5) == 5
    assert add(5, 0) == 5
    assert add(0, -5) == -5
    assert add(-5, 0) == -5

def test_sub_zero():
    assert sub(0, 5) == -5
    assert sub(5, 0) == 5
    assert sub(0, -5) == 5
    assert sub(-5, 0) == -5

def test_add_large_numbers():
    assert add(1000000, 2000000) == 3000000
    assert add(-1000000, -2000000) == -3000000
    assert add(1000000, -1000000) == 0
    assert add(-1000000, 1000000) == 0

def test_sub_large_numbers():
    assert sub(2000000, 1000000) == 1000000
    assert sub(-2000000, -1000000) == -1000000
    assert sub(1000000, -1000000) == 2000000
    assert sub(-1000000, 1000000) == -2000000
      