from other_code.services import count_service
from pytest import fixture


@fixture
def test_simple_mocking(mocker):
    """
    pytest-mock provides a fixture for easy, self-cleaning mocking
    :param mocker:
    :return:
    """
    mock_db_service = mocker.patch("other_code.services.db_service", autospec=True)
    mock_data = [(0, "fake row", 0.0)]
    mock_db_service.return_value = mock_data

    print("\n(Calling countservice with the DB mocked out...)")

    c = count_service('foo')

    mock_db_service.assert_called_with('foo')

    assert c == 1