import pytest

data = [
    [1, 2, 3],
    [4, 5, 9]
]

@pytest.mark.parametrize('a, b, expect', data)
def test_parametrize_1(a, b, expect):
    print('\n測試數據為\n{}, {}, {}'.format(a, b, expect))
    actual = a + b
    assert actual == expect


@pytest.mark.parametrize('value', data)
def test_parametrize_2(value):
    print('\n測試數據為\n{}'.format(value))
    actual = value[0] + value[1]
    assert actual == value[2]


if __name__ == '__main__':
    pytest.main(['-s'])