from src.math_operations import add, substract, dotfun

def test_add():
    assert add(2,5)==7
    assert substract(10,2)==8
    assert dotfun(2,6)==12

