import unittest
import Dwight_Kappl_hw1

class TestLeapYear(unittest.TestCase):
    
    def test_years(self):
        self.assertEqual(Dwight_Kappl_hw1.leap(2021), False)
        self.assertEqual(Dwight_Kappl_hw1.leap(2020), True)
        self.assertEqual(Dwight_Kappl_hw1.leap(1983), False)

if __name__ == '__main__':
    unittest.main()