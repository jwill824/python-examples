import unittest

class City:
    def __init__(self, population):
        self.population = population
        self.neighbors = []

    def traffic_to(self, city, n):
        traffic = n.population
        for neighbor in n.neighbors:
            if neighbor == city:
                continue
            traffic += self.traffic_to(n, neighbor)
        return traffic
    
    def get_maximum_traffic(self):
        maximum = 0
        for neighbor in self.neighbors:
            traffic = self.traffic_to(self, neighbor)
            if traffic > maximum:
                maximum = traffic
        return maximum

class test(unittest.TestCase):
    def test_basic(self):
        city1 = City(1)
        city2 = City(2)
        city3 = City(3)
        city4 = City(4)
        city5 = City(5)

        city1.neighbors = [city5]
        city2.neighbors = [city5]
        city3.neighbors = [city5]
        city4.neighbors = [city5]
        city5.neighbors = [city1, city2, city3, city4]

        self.assertEqual(city1.get_maximum_traffic(), 14)
        self.assertEqual(city2.get_maximum_traffic(), 13)
        self.assertEqual(city3.get_maximum_traffic(), 12)
        self.assertEqual(city4.get_maximum_traffic(), 11)
        self.assertEqual(city5.get_maximum_traffic(), 4)
        
    def test_complex(self):
        city1 = City(2)
        city2 = City(8)
        city3 = City(7)
        city4 = City(10)
        city5 = City(12)
        city6 = City(5)

        city1.neighbors = [city2]
        city2.neighbors = [city1, city3, city4]
        city3.neighbors = [city2]
        city4.neighbors = [city2, city5, city6]
        city5.neighbors = [city4]
        city6.neighbors = [city4]

        self.assertEqual(city1.get_maximum_traffic(), 42)
        self.assertEqual(city2.get_maximum_traffic(), 27)
        self.assertEqual(city3.get_maximum_traffic(), 37)
        self.assertEqual(city4.get_maximum_traffic(), 17)
        self.assertEqual(city5.get_maximum_traffic(), 32)
        self.assertEqual(city6.get_maximum_traffic(), 39)

if __name__ == '__main__':
    unittest.main()
