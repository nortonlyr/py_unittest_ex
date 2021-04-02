import pytest

data_1 = [1,2]
data_2 = [3,4]

@pytest.mark.parametrize('a', data_1)
@pytest.mark.parametrize('b', data_2)

def test_parametrize_1(a, b):
    print('\n測試數據為\n{}, {}'.format(a, b))


if __name__ == '__main__':
    pytest.main(['-s'])