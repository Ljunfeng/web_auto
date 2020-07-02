import allure
import pytest
from pytest import assume


def test_x():
    '''__doc__'''
    with allure.step("步骤1"):
        print("1111111111")
        # pytest.assume(1==2)
        with assume: assert 1==2

    with allure.step("步骤2"):
        print("22222222222")
        # pytest.assume(2==2)
        with assume: assert 2==2

    with allure.step("步骤3"):
        print("333333333333")
        # pytest.assume(3==3)
        with assume: assert 3==3