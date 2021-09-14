import unittest

def dayOfProgrammer(year):
    gregorian = 1918 < year <= 2700
    julian = 1700 <= year < 1918
    gregorian_leap_year = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
    julian_leap_year = year % 4 == 0
    
    if (gregorian and gregorian_leap_year) or (julian and julian_leap_year):
        day = 12
    elif (gregorian and not gregorian_leap_year) or (julian and not julian_leap_year):
        day = 13
    else:
        day = 26
        
    return str(day) + ".09." + str(year)

class test(unittest.TestCase):
    def test_one(self):
        self.assertEqual("13.09.2017", dayOfProgrammer(2017))
        
    def test_two(self):
        self.assertEqual("12.09.2016", dayOfProgrammer(2016))
        
    def test_three(self):
        self.assertEqual("12.09.1800", dayOfProgrammer(1800))
        
    def test_four(self):
        self.assertEqual("26.09.2701", dayOfProgrammer(2701))
        
    def test_five(self):
        self.assertEqual("13.09.2013", dayOfProgrammer(2013))
        
    def test_six(self):
        self.assertEqual("12.09.1700", dayOfProgrammer(1700))
        
    def test_seven(self):
        self.assertEqual("13.09.2100", dayOfProgrammer(2100))
        
if __name__ == '__main__':
    unittest.main()