import mazeRunner
import random
import mazeOutput
import time
import hardMaze
import astar
import os

if __name__ == '__main__':
    """
    g = hardMaze.geneticAlgorithm()
    list = []
    g.run(list)
    """

    n = 100
    p = 0.1
    #print("p : 0.2, maze = 100 * 100")
    while p == 0.1:
        number = 0
        mazeList = []
        for i in range(1000):
            mazeList.append(hardMaze.mazeGenerator(n, p))
        runner = mazeRunner.MazeRunner()
        startPoint, endPoint = mazeRunner.Point(1, 1), mazeRunner.Point(n, n)
        lengthS = 0
        lengthL = 0
        dfsT = 0
        bfsT = 0
        amT = 0
        aeT = 0
        count = 0
        for i in range(1000):
            stack = []
            list = []
            dfsS = time.time()
            runner.DFSRunner(startPoint, endPoint, mazeList[i], stack)
            dfsE = time.time()
            if len(stack) == 0:
                i -= 1
                continue
            dfsT += (dfsE - dfsS)

            bfsS = time.time()
            runner.BFSRunner(startPoint, endPoint, mazeList[i], list)
            bfsE = time.time()
            bfsT += (bfsE - bfsS)

            dfsS = time.time()
            path = astar.astar_e(mazeList[i], n, count, (n-1, n-1), (0, 0))
            dfsE = time.time()
            aeT += (bfsE - bfsS)

            dfsS = time.time()
            path = astar.astar_m(mazeList[i], n, count, (n-1, n-1), (0, 0))
            dfsE = time.time()
            amT += (bfsE - bfsS)

            #lengthS += runner.totalVisit
            #lengthL += runner.maxExpanded
            if len(stack) == 0:
                number += 1
        print("DFS ave time: " + str(dfsT / 1000) + " Seconds")
        print("BfS ave time: " + str(bfsT / 1000) + " Seconds")
        print("A_E ave time: " + str(aeT / 1000) + " Seconds")
        print("A_M ave time: " + str(amT / 1000) + " Seconds")
        #print("p = " + str(p) + "(DFS): " + str(lengthS / (1000 - number)))
        #print("p = " + str(p) + "(BFS): " + str(lengthL / (1000 - number)))
        #print("p = " + str(p) + ": " + str((1000 - number) / 10) + "%")
        break

    """
    main_m = "./AStar_m"
    os.system(main_m)
    main_e = "./AStar_e"
    os.system(main_e)
    n = 2800
    maze = hardMaze.mazeGenerator(n)
    runner = mazeRunner.MazeRunner()
    startPoint, endPoint = mazeRunner.Point(1, 1), mazeRunner.Point(n, n)
    path = []
    stack = []
    startTime = time.time()
    runner.DFSRunner(startPoint, endPoint, maze, stack)
    endTime = time.time()
    #for p in stack:
    #    print(p.row, p.col)
    print("DFS costs ", endTime - startTime, "seconds")
    startTime = time.time()
    runner.BFSRunner(startPoint, endPoint, maze, path)
    endTime = time.time()
    print("BFS costs ", endTime - startTime, "seconds")
    """
    """
    n = 100
    p = 0.2
    maze = hardMaze.mazeGenerator(n, p)
    runner = mazeRunner.MazeRunner()
    startPoint, endPoint = mazeRunner.Point(1, 1), mazeRunner.Point(n, n)
    path = []
    runner.DFSRunner(startPoint, endPoint, maze, path)
    mazeOutput.createPath(maze, n, path, "./DFS.png")
    path = []
    runner.BFSRunner(startPoint, endPoint, maze, path)
    mazeOutput.createPath(maze, n, path, "./BFS.png")
    count = 0
    path = []
    path = astar.astar_e(maze,n,count, (n-1, n-1), (0, 0))
    mazeOutput.createAPath(maze, n, path, "./A_e.png")
    path = []
    path = astar.astar_m(maze,n,count, (n-1, n-1), (0, 0))
    mazeOutput.createAPath(maze, n, path, "./A_m.png")
    """
    """
    n = 100
    p = 0.1
    while p < 0.5:
        number = 0
        count = 0
        mazeList = []
        for i in range(1000):
            mazeList.append(hardMaze.mazeGenerator(n, p))

        lengthS = 0
        lengthL = 0
        dfsT = 0
        bfsT = 0
        for i in range(1):
            path = []
            dfsS = time.time()
            path = astar.astar_e(mazeList[i], n, count, (n-1, n-1), (0, 0))
            dfsE = time.time()
            dfsT += (dfsE - dfsS)
            if not path:
                number += 1
                continue
            lengthS += len(path)

            path = []
            bfsS = time.time()
            path = astar.astar_m(mazeList[i], n, count, (n-1, n-1), (0, 0))
            bfsE = time.time()
            bfsT += (bfsE - bfsS)
            lengthL += len(path)

            #lengthS += runner.totalVisit
            #lengthL += runner.maxExpanded
        #print("DFS ave time: " + str(dfsT / 1000) + " Seconds")
        #print("BfS ave time: " + str(bfsT / 1000) + " Seconds")
        print("p = " + str(p) + "(A_e): " + str(lengthS / (1000 - number)))
        print("p = " + str(p) + "(A_m): " + str(lengthL / (1000 - number)))
        #print("p = " + str(p) + ": " + str((1000 - number) / 10) + "%")
        p += 0.05
    """
