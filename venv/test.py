import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_get_length_is_1(self):
        result = get_length(1)
        self.assertEqual(result, 1)

    def test_get_length_is_4(self):
        result = get_length(1, 2, 3, 4)
        self.assertEqual(result, 4)

    def test_get_length_is_7(self):
        result = get_length(2,3,4,5,6,7,8)
        self.assertEqual(result, 7)

    def test_get_sum_is_4(self):
         result = get_sum(1,2,1)
         self.assertEqual(result, 4)

    def test_get_mean_is(self):
        result = get_mean(1)
        self.assertEqual(result, 1)



if __name__ == '__main__':
    unittest.main()
