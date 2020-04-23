from main import add


def test_add():
    assert add(0, 0) == 0
    assert add(1, 3) == 4
    assert add(5, 12) == 17
    assert add(3, -4) == -1
    assert add(0, -1) == -1
