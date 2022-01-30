import pytest

"""
use packages pytest-ordering
"""


class TestOrdering:
    @pytest.mark.run(order=4)
    def test_method_a(self):
        print('Method A')

    @pytest.mark.run(order=3)
    def test_method_b(self):
        print('Method B')

    @pytest.mark.run(order=1)
    def test_method_c(self):
        print('Method C')

    @pytest.mark.run(order=2)
    def test_method_d(self):
        print('Method D')
