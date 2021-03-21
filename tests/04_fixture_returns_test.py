import pytest


def test_with_data_fixture(one_fixture):
    """
    PyTest finds the fixture whose name matches the argument,
    calls it, and passes that return value into our test case:
    :param one_fixture:
    :return:
    """
    print("\nRunning test_with_data_fixture: {}".format(one_fixture))
    assert one_fixture == 1
    assert one_fixture != 2

@pytest.fixture
def one_fixture():
    """
    Beyond just "doing stuff", fixtures can return data, which PyTest will pass to the test cases that refer to it...
    :return:
    """
    print("\n(Returning 1 from data_fixture)")
    return 1