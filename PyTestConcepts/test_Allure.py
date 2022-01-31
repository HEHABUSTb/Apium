import pytest
import allure


def test_method_a():
    allure_step('Launching app')
    allure_step('Step-1')
    print('Method A')


def test_method_b():
    print('Method B')


@pytest.mark.skip
def test_method_c():
    print('This is method C')


def test_method_d():
    print('This is method D')


def allure_step(text):
    with allure.step(text):
        pass
