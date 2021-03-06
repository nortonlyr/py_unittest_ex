import pytest


@pytest.fixture(params=["a", "b", "c", "d"])
def letters_fixture(request):
    """
    Fixtures can cause tests
    :param request:
    :return:
    """
    yield request.param


@pytest.fixture(params=[1,2,3,4])
def numbers_fixture(request):
    """
    Fixtures can invoke each other (producing cartesian products of parameters)
    :param request:
    :return:
    """
    yield request.param


def test_fixtureception(letters_fixture, numbers_fixture):
    """
    Print out our combined fixture "product"
    :param letters_fixture:
    :param number_fixture:
    :return:
    """
    coordinate = letters_fixture + str(numbers_fixture)

    print('\nRunning test_fixtureception with "{}"'.format(coordinate))