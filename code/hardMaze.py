import mazeRunner
import random
import mazeOutput
import time

def mazeGenerator(n, p):
    maze = [[0] * n for i in range(n)]
    for row in range(n):
        for col in range(n):
            if row == 0 and col == 0:
                continue
            if row == n - 1 and col == n - 1:
                continue
            r = random.random()
            if r < p:
                maze[row][col] = 1
    return maze


class geneticAlgorithm:
    n = 100 #size of maze
    p = 0.1 #rate of wall
    nMaze = 100 #number of maze
    rMutate = 0.05 #rate of mutation
    nIteration = 100 # number of iteration
    preList = []

    def run(self, list):
        self.createBeginningSpecies(list)
        for i in range(self.nIteration):
            print("Iteration : " + str(i))
            self.select(list)
            self.crossover(list)
            self.mutate(list)
            self.valid(list)
            for j in range(self.nMaze):
                name = './images/' + str(i) + '_' + str(j) + '.png'
                mazeOutput.createImage(list[j], self.n, name)

    def createBeginningSpecies(self, list):
        runner = mazeRunner.MazeRunner()
        startPoint, endPoint = mazeRunner.Point(1, 1), mazeRunner.Point(self.n, self.n)
        count = 0
        while count < self.nMaze:
            path = []
            maze = mazeGenerator(self.n, self.p)
            list.append(maze)
            runner.DFSRunner(startPoint, endPoint, list[count], path)
            if len(path) == 0:
                list.pop()
                continue
            self.preList.append(maze)
            count += 1


    def select(self, list):
        runner = mazeRunner.MazeRunner()
        startPoint, endPoint = mazeRunner.Point(1, 1), mazeRunner.Point(self.n, self.n)
        length_of_maze = []
        length_of_expanded = []
        length_of_fringe = []
        for i in range(self.nMaze):
            path = []
            runner.BFSRunner(startPoint, endPoint, list[i], path)
            #length_of_maze.append(len(path))
            #length_of_expanded.append(runner.maxExpanded)
            length_of_fringe.append(runner.maxFringe)
        """
        totalPath = 0
        for i in range(self.nMaze):
            totalPath += length_of_maze[i]
        print("Ave :" + str(totalPath / self.nMaze))
        print("----------")
        """
        """
        totalExpanded = 0
        for i in range(self.nMaze):
            totalExpanded += length_of_expanded[i]
        print("Ave :" + str(totalExpanded / self.nMaze))
        print("----------")
        """
        totalFringe = 0
        for i in range(self.nMaze):
            totalFringe += length_of_fringe[i]
        print("Ave :" + str(totalFringe / self.nMaze))
        print("----------")

        rate = []
        for i in range(self.nMaze):
            rate.append(length_of_fringe[i] / totalFringe)

        tempRate = []
        tempList = []
        for i in range(self.nMaze):
            tempRate.append(rate.pop())
            tempList.append(list.pop())

        for i in range(1, self.nMaze):
            tempRate[i] += tempRate[i - 1]

        for i in range(self.nMaze):
            r = random.random()
            for j in range(self.nMaze - 1):
                if r <= tempRate[j]:
                    list.append(tempList[j])
                    break
                if j == self.nMaze - 2:
                    list.append(tempList[j + 1])

    def crossover(self, list):
        crossTime = int(self.nMaze / 2)
        tempList = []
        for i in range(self.nMaze):
            tempList.append(list.pop())
        for i in range(crossTime):
            newMaze1 = [[0] * self.n for i in range(self.n)]
            newMaze2 = [[0] * self.n for i in range(self.n)]
            crossP = random.randint(1, self.n - 1)
            for row in range(self.n):
                for col in range(self.n):
                    if col < crossP:
                        newMaze1[row][col] = tempList[2 * i][row][col]
                        newMaze2[row][col] = tempList[2 * i + 1][row][col]
                    else:
                        newMaze1[row][col] = tempList[2 * i + 1][row][col]
                        newMaze2[row][col] = tempList[2 * i][row][col]
            list.append(newMaze1)
            list.append(newMaze2)

    def mutate(self, list):
        nMutate = int(self.n * self.n * self.rMutate)
        for i in range(self.nMaze):
            p = 0
            while p < nMutate:
                randomRow = random.randint(0, self.n - 1)
                randomCol = random.randint(0, self.n - 1)
                if randomRow == 0 and randomCol == 0:
                    continue
                if randomRow == self.n - 1 and randomCol == self.n - 1:
                    continue
                if list[i][randomRow][randomCol] == 0:
                    list[i][randomRow][randomCol] = 1
                else:
                    list[i][randomRow][randomCol] = 0
                p += 1

    def valid(self, list):
        runner = mazeRunner.MazeRunner()
        startPoint, endPoint = mazeRunner.Point(1, 1), mazeRunner.Point(self.n, self.n)
        for i in range(self.nMaze):
            path = []
            runner.DFSRunner(startPoint, endPoint, list[i], path)
            if len(path) == 0:
                list[i] = self.preList[i]
                continue
            self.preList[i] = list[i]


"""
g = geneticAlgorithm()
list = []
g.run(list)
"""
