import matplotlib.pyplot as plt
import numpy as np

# Function that will plot vectors
# Vectors are passed in with the x variable which is an array with each row being a vector, column 0 is the x component,
# column 1 is the y component

def plotVector(fig, x, legend):
    X = np.array(x)
    nRows, nCol = X.shape
    for i in range(nRows):
        fig.plot([0, X[i, 0]], [0, X[i, 1]], marker='D')
    fig.plot(0, 0, marker='D', color='k')
    fig.legend(legend)
    fig.grid(zorder=0.5)
