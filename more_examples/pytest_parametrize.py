# reference : https://www.cnblogs.com/linuxchao/p/linuxchao-pytest-parametrize.html
import pytest

import pytest

data = [1, 2]


@pytest.mark.parametrize('a', data)
def test_parametrize(a):
    print('\n被加载测试数据为\n{}'.format(a))


if __name__ == '__main__':
    pytest.main(['-s'])