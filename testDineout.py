import pytest
from Dineout import Dineout

@pytest.fixture()
def dineout():
    dineout = Dineout()
    dineout.addFoodPrice("a", 1)
    dineout.addFoodPrice("b", 2)
    return dineout

def test_CanCalculateTotal(dineout):
    dineout.addFood("a")
    assert dineout.calculateTotal() == 1

def test_GetCorrectTotalWithMultipleFoods(dineout):
    dineout.addFood("a")
    dineout.addFood("b")
    assert dineout.calculateTotal() == 3

def test_canAddDiscountRule(dineout):
    dineout.addDiscount("a", 3, 2)

def test_canApplyDiscountRule(dineout):
    dineout.addDiscount("a", 3, 2)
    dineout.addFood("a")
    dineout.addFood("a")
    dineout.addFood("a")
    assert dineout.calculateTotal() == 2

def test_ExceptionWithBadFood(dineout):
    with pytest.raises(Exception):
        dineout.addFood("c")














