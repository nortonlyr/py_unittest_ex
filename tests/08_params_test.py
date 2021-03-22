import pytest


def test_parameterization(letter):
    print("\n  Running test_parameterization with {}".format(letter))

def test_modes(mode):
    print("\n  Runing test_modes with {}".format(mode))


@pytest.fixture(params=["a", "b", "c", "d", "y"])
def letter(request):
    """
    Fixtures with parameters will run once per param
    (Your can assess the current param via request fixture)
    :param request:
    :return:
    """
    yield request.param

@pytest.fixture(params=[1, 2, 6], ids=['foo', 'bar', 'baz'])
def mode(request):
    """
    Fixtures with parameters will run once per param
    (You can access the current param via the request fixture)
    :param request:
    :return:
    """
    yield request.param