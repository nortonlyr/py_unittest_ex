import pytest
def test_div_zero_exception():
    """
    pytest.raises can assert that exceptions are raised (catching them)
    """
    with pytest.raises(ZeroDivisionError):
        x = 1 / 0
        print("1/0={}".format(x))

def test_keyerror_details():
    """
    The raised exception can be referenced, and further inspected (or asserted)
    """
    my_map = {"foo":"bar"}

    with pytest.raises(KeyError) as ke:
        baz = my_map["baz"]
        print("Found Baz: {}".format(baz))