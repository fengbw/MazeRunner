import time
class Point:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __ne__(self, other):
        return self.row != other.row or self.col != other.col


class MazeRunner:
    totalVisit = 1

    def DFSRunner(self, startPoint, endPoint, maze, stack):
        """
        :type nums: {int, int}, {int, int}, List[int][int]
        :rtype: List[(int, int)]
        """
        steps = 0
        found = False
        self.totalVisit = 1
        stack.append(startPoint)
        visited = [[0] * endPoint.row for i in range(endPoint.col)]
        while len(stack) != 0:
            current = stack[-1]
            row = current.row - 1
            col = current.col - 1
            if row == endPoint.row - 1 and col == endPoint.col - 1:
                break
            if col + 1 < endPoint.col and maze[row][col + 1] == 0 and visited[row][col + 1] == 0:
                col += 1
                stack.append(Point(row + 1, col + 1))
                self.totalVisit += 1
                visited[row][col] = 1
                continue
            elif row + 1 < endPoint.row and maze[row + 1][col] == 0 and visited[row + 1][col] == 0:
                row += 1
                stack.append(Point(row + 1, col + 1))
                self.totalVisit += 1
                visited[row][col] = 1
                continue
            elif col - 1 >= 0 and maze[row][col - 1] == 0 and visited[row][col - 1] == 0:
                col -= 1
                stack.append(Point(row + 1, col + 1))
                self.totalVisit += 1
                visited[row][col] = 1
                continue
            elif row - 1 >= 0 and maze[row - 1][col] == 0 and visited[row - 1][col] == 0:
                row -= 1
                stack.append(Point(row + 1, col + 1))
                self.totalVisit += 1
                visited[row][col] = 1
                continue
            else:
                stack.pop()



    def validMaze(self, startPoint, endPoint, maze):
        if maze[startPoint.row - 1][startPoint.col - 1] == 0 and maze[endPoint.row - 1][endPoint.col - 1] == 0:
            return True
        else:
            return False

    maxExpanded = 1
    maxFringe = 0

    def BFSRunner(self, startPoint, endPoint, maze, path):
        if not self.validMaze(startPoint, endPoint, maze):
            print("No Path!")
            return
        queue = [startPoint]
        self.maxExpanded = 1
        self.maxFringe = 0
        mark = [[Point(-1, -1)] * endPoint.col for i in range(endPoint.row)]
        mark[startPoint.row - 1][startPoint.col - 1] = startPoint
        while len(queue) != 0:
            front = queue.pop(0)
            row = front.row - 1
            col = front.col - 1
            if row - 1 >= 0 and maze[row - 1][col] == 0:
                if mark[row - 1][col] == Point(-1, -1):
                    mark[row - 1][col] = front
                    queue.append(Point(row, col + 1))
                    self.maxExpanded += 1
                    if Point(row, col + 1) == endPoint:
                        break
            if col + 1 < endPoint.col and maze[row][col + 1] == 0:
                if mark[row][col + 1] == Point(-1, -1):
                    mark[row][col + 1] = front
                    queue.append(Point(row + 1, col + 2))
                    self.maxExpanded += 1
                    if Point(row + 1, col + 2) == endPoint:
                        break
            if row + 1 < endPoint.row and maze[row + 1][col] == 0:
                if mark[row + 1][col] == Point(-1, -1):
                    mark[row + 1][col] = front
                    queue.append(Point(row + 2, col + 1))
                    self.maxExpanded += 1
                    if Point(row + 2, col + 1) == endPoint:
                        break
            if col - 1 >= 0 and maze[row][col - 1] == 0:
                if mark[row][col - 1] == Point(-1, -1):
                    mark[row][col - 1] = front
                    queue.append(Point(row + 1, col))
                    self.maxExpanded += 1
                    if Point(row + 1, col) == endPoint:
                        break
            self.maxFringe = max(self.maxFringe, len(queue))
        if len(queue) != 0:
            row = endPoint.row
            col = endPoint.col
            path.append(endPoint)
            while mark[row - 1][col - 1] != startPoint:
                path.append(mark[row - 1][col - 1])
                row = mark[row - 1][col - 1].row
                col = mark[row - 1][col - 1].col
            path.append(startPoint)

"""
maze = [[0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 0, 0], [0, 1, 1, 0, 1], [0, 0, 0, 0, 0]]
m = [[0, 0], [0, 0]]
startPoint = Point(1, 1)
endPoint = Point(5, 5)
runner = MazeRunner()
stack = []
path = []

startTime = time.time()
runner.DFSRunner(startPoint, endPoint, maze, stack)
endTime = time.time()
for p in stack:
    print(p.row, p.col)
print("DFS costs ", endTime - startTime, "seconds")
maze = [[0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 0, 0], [0, 1, 1, 0, 1], [0, 0, 0, 0, 0]]
startTime = time.time()
runner.BFSRunner(startPoint, endPoint, maze, path)
endTime = time.time()
for p in path:
    print(p.row, p.col)
print("BFS costs ", endTime - startTime, "seconds")
"""
