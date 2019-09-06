rows, cols = (5,5)
theInput = [[0 for i in range(cols)] for j in range(rows)]
theInput[1][1] = 1
theInput[1][2] = 1
theInput[2][2] = 1

theInput[4][0] = 1
theInput[4][1] = 1
theInput[4][2] = 1
theInput[4][3] = 1
theInput[4][4] = 1


class OceanMap:
    """
    This class represents the map for the ocean.

    Attributes:
        Map {2D Array}: An array with 1's and 0's, 1 representing island 0's
                        represent ocean
    """
    def __init__(self, OceanMap):
        """
        This function is used during declarion to set 'map' (Array)

        Args:
            OceanMap {2D Array} sets attribute Map for the object
        """
        self.Map = OceanMap

    def largestIsland(self):
        """
        Counts size of each island and returns size of the largest island

        Returns:
            {int} Size of the largest island
        """
        x,y = (0,0)
        largest_island = 0
        for x in range(len(self.Map)):
            for y in range(len(self.Map[0])):
                islandSize = self.countIsland(x,y)
                if largest_island < islandSize:
                    largest_island = islandSize

        return largest_island


    def countIsland(self,x,y):
        """
        Counts the size of a single island and returns the size.

        Args:
            x {int} The X coordinate of an location of part of island
            y {int} The Y Coordiante of an location of part of island

        Returns:
            {int} The Size of the island
        """
        if (x >= len(self.Map)) or (y >= len(self.Map[0])):
            return 0

        theMap = list(map(list, self.Map))
        toSearch = [(x,y)]
        islandSize = 0
        for oceanTuple in toSearch:
            if (oceanTuple[0] >= len(self.Map)) or (oceanTuple[1] >= len(self.Map[0])):
                continue

            if(theMap[oceanTuple[0]][oceanTuple[1]] == 1):
                islandSize += 1
                theMap[oceanTuple[0]][oceanTuple[1]] = 0
                toSearch.append((oceanTuple[0]+1,oceanTuple[1]))
                toSearch.append((oceanTuple[0]-1,oceanTuple[1]))
                toSearch.append((oceanTuple[0],oceanTuple[1]+1))
                toSearch.append((oceanTuple[0],oceanTuple[1]-1))

        return islandSize

    def printMap(self):
        for row in self.Map:
            print(row)

oceanMP = OceanMap(theInput)

output = oceanMP.largestIsland()

print(output)

