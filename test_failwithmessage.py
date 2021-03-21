import unittest

class FailureMessageTest(unittest.TestCase):

    def test_true(self):
        self.assertTrue(True, 'true message goes here')

    def test_fail(self):
        self.assertFalse(False, 'failure message goes here')

if __name__ == '__main__':
    unittest.main()