# reference : https://www.cnblogs.com/linuxchao/p/linuxchao-pytest-parametrize.html
import pytest

data_1 = [
    (1, 2, 3),
    (4, 5, 9)
]

def add(a, b):
    return a + b

@pytest.mark.parametrize('a, b, expect', data_1)
class Test_parametrize(object):

    def test_parametrize_1(self, a, b, expect):
        print('\n測試函數1測試數據為\n{}-{}'.format(a, b))
        assert add(a, b) == expect

    def test_parametrize_2(self, a, b, expect):
        print('\n測試函數2測試數據為\n{}-{}'.format(a, b))


if __name__ == '__main__':
    pytest.main(['-sv'])