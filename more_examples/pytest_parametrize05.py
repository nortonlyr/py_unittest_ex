import pytest

data_1 = (
    {
        'user': 1,
        'pwd': 2
    },
    {
        'user': 3,
        'pwd': 4
    }
)

@pytest.mark.parametrize('dic', data_1)
def test_parametrize_1(dic):
    print('\n測試數據為\n{}'.format(dic))


if __name__ == '__main__':
    pytest.main(['-s'])