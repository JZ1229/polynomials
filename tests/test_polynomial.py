import pytest
from polynomials import Polynomial

def test_print():

    p = Polynomial((2,1,0,3))

    assert str(p) == "3x^3+x+2"

def test_equality():

    assert Polynomial((1,0))==Polynomial((1,0))

@pytest.mark.parametrize(
    "a,b,sum",
    (((0,),(0,1),(0,1)),
     ((2,0,3),(1,2),(3,2,3)),
     ((4,2),(10,2,4),(14,4,4)))
    )
def test_add(a ,b , sum):
    assert Polynomial(a) + Polynomial(b) == Polynomial(sum)


def test_add_scalar():
    assert Polynomial((2, 1)) + 3  == Polynomial((5 ,1))


def test_reverse_add_scalar():
    assert 3 + Polynomial((2,1)) == Polynomial((5 ,1))

def test_add_unknown():
    with pytest.raises(TypeError):
        Polynomial((1,)) + "frog"

def test_sub_scalar():
    assert Polynomial((0, )) - Polynomial((1, 2))  == Polynomial((-1 , -2))

def test_scalar_minus_poly():
    assert 3 - Polynomial((2, 1)) == Polynomial((1, -1))

def test_poly_mul_scalar():
    assert Polynomial((2, 1)) * 3 == Polynomial((6, 3))

def test_poly_mul_poly():
    assert Polynomial((2, 1)) * Polynomial((1,2)) == Polynomial((2,5,2))

def test_poly_mul_poly2():
    assert Polynomial((2, 1, 4)) * Polynomial((1,2)) == Polynomial((2,5,6,8))

def test_scal_mul_poly():
    assert 3 * Polynomial((2, 1)) == Polynomial((6, 3))

def test_pow_poly():
    assert Polynomial((2, 1)) ** 3 == Polynomial((8,12,6,1))

def test_call():
    assert Polynomial((2, 1))(2) == 4

