import unittest

class MyTestCase(unittest.TestCase):
    def test_one(self):
        pass
    
    def notest(self):
        pass

class MySecondTestCase(unittest.TestCase):
    def test_one(self):
        pass
    
    def notest(self):
        pass

if __name__ == '__main__':
    unittest.main()