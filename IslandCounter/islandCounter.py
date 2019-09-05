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
    def __init__(self,OceanMap):
        self.Map = OceanMap

    def largestIsland(self):
        x,y = (0,0)
        largest_island = 0
        for x in range(len(self.Map)):
            for y in range(len(self.Map[0])):
                islandSize = self.countIsland(x,y)
                if largest_island < islandSize:
                    largest_island = islandSize

        return largest_island


    def countIsland(self,x,y):
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

