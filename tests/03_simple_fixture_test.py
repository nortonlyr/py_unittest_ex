import pytest


def test_with_local_fixture(local_fixture):
    """
    Fixtures can be invoked simple by having a positional arg
    :param local_fixture:
    :return:
    """
    print("Running test_with_local_fixture...")
    assert True

@pytest.fixture
def local_fixture():
    """
    Fixtures are callables decorated with @fixture
    :return:
    """
    print("\n(Doing local fixture setup stuff!)")

def test_with_global_fixture(global_fixture):
    """"
    Fixtures can also be shared across test files (see confest.py)
    """
    print("Running test_with_global_fixture...")