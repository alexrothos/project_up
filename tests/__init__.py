import os
import unittest

def run_tests():
    test_suite = unittest.defaultTestLoader.discover(os.path.dirname(__file__), pattern='test_*.py')
    unittest.TextTestRunner().run(test_suite)

if __name__ == '__main__':
    from test import run_tests
    run_tests()
