import main

def test_add():
    assert main.add(5,8) == 13
    assert main.add(12) == 14
    

def test_mult():
    assert main.mult(12,2) == 24
    assert main.mult(11) == 55