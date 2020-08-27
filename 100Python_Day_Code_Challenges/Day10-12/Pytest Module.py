import pytest

def func(x, b):
    return x + b

def testfunc():
    assert func(12,33) == 12 +3
