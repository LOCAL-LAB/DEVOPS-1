import unittest

class MyTestCase2(unittest.TestCase):
    def test_one(self):
        result = "do_something"
    
    def notest(self):
        assert result == 'do_something'

class MySecondTestCase2(unittest.TestCase):
    def test_one(self):
        pass
    
    def test_main(self):
        wynik = addition(3,2)
        assert wynik == 4

def addition(*args):
    a1,a2 = args
    return a1 + a2
    
def main():
    import sys
    print(addition(a1,a2))

if __name__ == '__main__':
    # unittest.main()
    main()