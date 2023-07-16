from p001 import *

def test_even():
    assert solution(50) == '50 is even'

def test_odd():
    assert solution(11) == '11 is odd'

def test_zero():
    assert solution(0) == '0 is even'

def test_large_number():
    assert solution(10003203) == '10003203 is odd'


def test_1000():
    assert solution(1000) == '1000 is even'