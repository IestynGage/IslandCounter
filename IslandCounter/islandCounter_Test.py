import unittest
from islandCounter import OceanMap

class TestHint(unittest.TestCase):
    emptyIsland = [[0 for i in range(5)] for j in range(5)]
    def test_single_island(self):
        """
        Aim:
            to see object can deal with expected data
        """
        testMap = list(map(list, self.emptyIsland))
        testMap[1][1] = 1
        testMap[1][0] = 1
        testOceanMap = OceanMap(testMap)

        actual      = testOceanMap.largestIsland()
        expected    = 2

        self.assertEqual(expected, actual)

    def test_multiply_island_1(self):
        """
        Aim:
            to test object with multilple islands
        """
        testMap = list(map(list, self.emptyIsland))
        #island 1
        testMap[2][3] = 1
        testMap[2][2] = 1
        testMap[1][2] = 1
        #island 2
        testMap[4][4] = 1

        testOceanMap = OceanMap(testMap)

        actual      = testOceanMap.largestIsland()
        expected    = 3

        self.assertEqual(expected, actual)

    def test_multiply_island_2(self):
        """
        Aim:
            to test object with multilple islands
        """
        testMap = list(map(list, self.emptyIsland))
        #island 1
        testMap[0][3] = 1
        testMap[0][2] = 1
        testMap[0][1] = 1
        testMap[1][2] = 1
        #island 2
        testMap[3][3] = 1
        testMap[2][3] = 1
        #island 4
        testMap[4][0] = 1
        testMap[4][1] = 1

        testOceanMap = OceanMap(testMap)
        testOceanMap.printMap()

        actual      = testOceanMap.largestIsland()
        expected    = 4

        self.assertEqual(expected, actual)


unittest.main()