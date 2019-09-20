import matplotlib.pyplot as plt
import numpy as np


def createImage(maze, n, name):
    # Make a n*n grid...
    nrows, ncols = n, n
    image = np.zeros(nrows*ncols)

    for row in range(n):
        for col in range(n):
            image[row * n + col] = maze[row][col]

    # Reshape things into a 9x9 grid.
    image = image.reshape((nrows, ncols))

    #row_labels = range(nrows)
    #col_labels = range(ncols)
    plt.matshow(image)
    #plt.xticks(range(ncols), col_labels)
    #plt.yticks(range(nrows), row_labels)
    plt.savefig(name)
    plt.close()

def createPath(maze, n, path, name):
    # Make a n*n grid...
    nrows, ncols = n, n
    image = np.zeros(nrows*ncols)

    for row in range(n):
        for col in range(n):
            image[row * n + col] = maze[row][col]

    for p in path:
        image[(p.row - 1) * n + (p.col - 1)] = 3
    # Reshape things into a 9x9 grid.
    image = image.reshape((nrows, ncols))

    #row_labels = range(nrows)
    #col_labels = range(ncols)
    plt.matshow(image)
    #plt.xticks(range(ncols), col_labels)
    #plt.yticks(range(nrows), row_labels)
    plt.savefig(name)
    plt.close()

def createAPath(maze, n, path, name):
    # Make a n*n grid...
    nrows, ncols = n, n
    image = np.zeros(nrows*ncols)

    for row in range(n):
        for col in range(n):
            image[row * n + col] = maze[row][col]

    for p in path:
        image[p[0] * n + p[1]] = 3
    # Reshape things into a 9x9 grid.
    image = image.reshape((nrows, ncols))

    #row_labels = range(nrows)
    #col_labels = range(ncols)
    plt.matshow(image)
    #plt.xticks(range(ncols), col_labels)
    #plt.yticks(range(nrows), row_labels)
    plt.savefig(name)
    plt.close()
