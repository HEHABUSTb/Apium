import pytest


@pytest.fixture()
def beforeMethod():
    print('\n Before method')
    yield
    print('\n After method')

@pytest.fixture(scope='module')
def beforeClass():
    print('Before a Class')
    yield
    print('After a Class')

@pytest.mark.usefixtures('beforeClass')
@pytest.mark.All
class TestExample:


    def test_method_A(self, beforeMethod):
        print('This is method A')

    def test_method_B(self, beforeMethod):
        print('This is method B')
        print('1111111')


