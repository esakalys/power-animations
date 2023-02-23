import numpy as np

# Function that returns x and y values for a circle with a specified radius and offset

def createCircle(radius, xOffset, yOffset):
    angleRange = np.linspace(0, 2*np.pi, 100)
    xRange = radius*np.cos(angleRange)+xOffset
    yRange = radius*np.sin(angleRange)+yOffset
    circle = np.stack((xRange, yRange))
    return circle