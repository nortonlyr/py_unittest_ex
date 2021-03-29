import pytest

data = [1, 2]


@pytest.mark.parametrize('a', data)
def test_parametrize(a):
    print('\n被加載測試數據為\n{}'.format(a))


if __name__ == '__main__':
    pytest.main(['-s'])