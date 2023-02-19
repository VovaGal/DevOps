# test for quadratic
import pytest

from lab2_calc import quad,a,b,c, add_fn, sub_fn, mult_fn, div_fn

# quadratic
def test_quad():
    true_statement = a == 1 and b == 2 and c == 1 and quad == "The solutions are (-1+0j) and (-1+0j)"
    assert true_statement

# addition
def test_add_fn():
    assert add_fn(1,1) == 2
    assert add_fn(2,2) == 4
    assert add_fn(4,4) == 8
    assert add_fn(8,8) == 16
# subtraction
def test_sub_fn():
    assert sub_fn(1,0) == 1
    assert sub_fn(2,1) == 1
    assert sub_fn(4,2) == 2
    assert sub_fn(8,3) == 5

# multiplication
def test_add_fn():
    assert mult_fn(1,1) == 1
    assert mult_fn(2,2) == 4
    assert mult_fn(4,4) == 16
    assert mult_fn(8,8) == 64

# division
def test_add_fn():
    assert div_fn(1,1) == 1
    assert div_fn(2,2) == 1
    assert div_fn(4,3) == 4/3
    assert div_fn(8,4) == 2
