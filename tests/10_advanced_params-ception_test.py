import pytest


@pytest.fixture(params=[1,2,3,4])
def numbers_fixture(request):
    """
    Fixtures can cause tests to be run multiple time (once per parameter)
    :param request:
    :return:
    """
    yield request.param

@pytest.fixture(params=["a", "b", "c", "d"])
def coordinates_fixture(request, numbers_fixture):
    """
    Fixture can invoke each other (producing cartesian products of params
    :param request:
    :param numbers_fixture:
    :return:
    """
    coordinate = request.param + str(numbers_fixture)
    yield coordinate


def test_advanced_fixtureception(coordinates_fixture):
    print(
        "\nRunning test_advanced_fixtureception with '{}'".format(coordinates_fixture)
    )