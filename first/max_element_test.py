import unittest
from max_element import MaxElementObserver, MaxElementFinder

class MaxElementObserverTest(unittest.TestCase):
    def test_update(self):
        observer = MaxElementObserver()
        data = [35, 56, 234, 46, 1, 9]
        observer.update(data)

class MaxElementFinderTest(unittest.TestCase):
    def test_find_max_element(self):
        finder = MaxElementFinder()
        observer1 = MaxElementObserver()
        observer2 = MaxElementObserver()
        finder.attach(observer1)
        finder.attach(observer2)
        data = [35, 56, 234, 46, 1, 9]
        finder.find_max_element(data)
        finder.detach(observer2)
        data = [5, 2, 7, 1, 8]
        finder.find_max_element(data)

if __name__ == '__main__':
    unittest.main()