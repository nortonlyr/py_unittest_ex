import pytest

dev_v3_credentials = None


@pytest.mark.skip
def test_broken_feature():
    #Always skipped
    assert False

@pytest.mark.skipif(not dev_v3_credentials, reason="S3 creds not found!")
def test_s3_api():
    # skipped if a certain condition is met
    assert True

@pytest.mark.xfail
def test_where_failure_is_acceptable():
    # Allow failed assertions (returns "XPASS" if there are no failures)
    assert True