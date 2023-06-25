import unittest
from min_element import MinElementBuilder, MinElementDirector

class MinElementBuilderTest(unittest.TestCase):
    def test_find_min_element(self):
        builder = MinElementBuilder()
        data = [593, 234, 23, 67, 43, 56]
        builder.set_data(data)
        builder.find_min_element()

class MinElementDirectorTest(unittest.TestCase):
    def test_construct(self):
        builder = MinElementBuilder()
        director = MinElementDirector(builder)
        data = [593, 234, 23, 67, 43, 56]
        director.construct(data)

if __name__ == '__main__':
    unittest.main()