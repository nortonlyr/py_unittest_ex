import logging
from unittest.mock import Mock

logging.basicConfig(level=logging.DEBUG)


# code
class ASpecificException(Exception):
    pass

def foo():
    pass

def bar():
    try:
        logging.info("enter function <foo> now")
        foo()
    except ASpecificException:
        logging.exception("we caught a specfic exception")


# unittest
def test_foo():
    foo = Mock(side_effect=ASpecificException())

    logging.info("enter function <bar> now")
    bar()
    logging.info("everything just be fine")

if __name__ == "__main__":
    test_foo()