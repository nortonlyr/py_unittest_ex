# reference: https://www.caodanle.com/archives/12014
import pytest

data_1 = [
    (1, 2, 3),
    (4, 5, 9)
]


def add(a, b):
    return a + b

@pytest.mark.parametrize('a, b , expect', data_1)
class TestParametric(object):

    def test_parametrize_1(self, a, b, expect):
        print('\n测试函数1测试数据为\n{}-{}'.format(a, b))
        assert add(a, b) == expect

    def test_parametrize_2(self, a, b, expect):
        print('\n测试函数2测试数据为\n{}-{}'.format(a, b))
        assert add(a, b) == expect


if __name__ == '__main__':
    pytest.main(['-sv'])

