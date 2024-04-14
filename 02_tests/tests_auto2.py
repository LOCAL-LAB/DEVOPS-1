import unittest

class MySecondTestCase2(unittest.TestCase):
    def test_one(self):
        pass
    
    def test_main(self):
        wynik = addition(3, 2)
        self.assertEqual(wynik, 4)

def addition(*args):
    return sum(args)
    
def main():
    import sys
    if len(sys.argv) > 2:
        a1 = int(sys.argv[1])
        a2 = int(sys.argv[2])
        print(addition(a1, a2))
    else:
        print("")

if __name__ == '__main__':
    unittest.main()
