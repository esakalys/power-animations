import numpy as np
import matplotlib.pyplot as plt
import sys
from functions.createCircle import createCircle
import math

# Program that plots an animation of the currents and magnetic fields
# in a three-phase machine with a specified number of frames

def rotMagField(frameNum, figSize, dpiArg):

    # Define parameters
    intRadius = 6
    extRadius = 8
    cntDelta = (extRadius - intRadius)/2
    wireRadius = 0.7
    f = 50
    omega = 2*np.pi*f
    # Parameters defined

    # Creates the case
    intCircle = createCircle(intRadius, 0, 0)
    extCircle = createCircle(extRadius, 0, 0)

    # Defines the coordinates of the wires within the case
    wireOffsets = [[0, (intRadius+cntDelta)],
                [0, -(intRadius+cntDelta)],
                [-(intRadius+cntDelta)*np.cos(np.pi/6), -(intRadius+cntDelta)*np.sin(np.pi/6)],
                [(intRadius+cntDelta)*np.cos(np.pi/6), (intRadius+cntDelta)*np.sin(np.pi/6)],
                [(intRadius+cntDelta)*np.cos(np.pi/6), -(intRadius+cntDelta)*np.sin(np.pi/6)],
                [-(intRadius+cntDelta)*np.cos(np.pi/6), (intRadius+cntDelta)*np.sin(np.pi/6)]]

    # Creates the wires
    wires = []
    wireColors = ['red', 'red',  'blue', 'blue', 'yellow', 'yellow']
    for i in range(len(wireColors)):
        wires.append(createCircle(wireRadius, wireOffsets[i][0], wireOffsets[i][1]))

    # Defines the time range
    tRange = np.linspace(0, 0.06, frameNum)

    # Defines the currents
    phases = []
    for i in range(3):
        angle = i*2*np.pi/3
        phases.append(np.sin(omega*tRange + angle))

    # Defines the overall magnetic field
    magFieldX = -4*np.sin(omega*tRange)
    magFieldY = -4*np.cos(omega*tRange)
    magField = np.stack((magFieldX, magFieldY))

    # Plots the frames
    for counter in range(tRange.size):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figSize, dpi=dpiArg)

        # Plotting the case
        ax1.plot(intCircle[0], intCircle[1], color='k')
        ax1.plot(extCircle[0], extCircle[1], color='k')

        # Plotting the wires
        counterWire = 0
        for wire in wires:
            ax1.plot(wire[0], wire[1], color=wireColors[counterWire])
            counterWire += 1

        # Plotting the current flow direction in the wires
        markers = []
        for phase in phases:
            if phase[counter] >= 0:
                markers.append('x')
                markers.append('o')
            else:
                markers.append('o')
                markers.append('x')
            
        counterWire = 0
        for wire in wireOffsets:
            ax1.plot(wire[0], wire[1], marker=markers[counterWire], markersize=8*abs(phases[math.floor(counterWire/2)][counter]), color=wireColors[counterWire])
            counterWire += 1

        # Plotting the individual magnetic fields
        magFields = []
        magFields.append(createCircle(4*phases[0][counter], wireOffsets[0][0], wireOffsets[0][1]))
        magFields.append(createCircle(4*phases[0][counter], wireOffsets[1][0], wireOffsets[1][1]))
        magFields.append(createCircle(4*phases[1][counter], wireOffsets[2][0], wireOffsets[2][1]))
        magFields.append(createCircle(4*phases[1][counter], wireOffsets[3][0], wireOffsets[3][1]))
        magFields.append(createCircle(4*phases[2][counter], wireOffsets[4][0], wireOffsets[4][1]))
        magFields.append(createCircle(4*phases[2][counter], wireOffsets[5][0], wireOffsets[5][1]))

        for field in magFields:
            ax1.plot(field[0], field[1], color='grey', linestyle='--', linewidth=1)

        # Plotting the magnetic field directions
        magArrows = []
        for i in range(len(phases)):
            magArrows.append([wireOffsets[i*2][0]+4*phases[i][counter],
                              wireOffsets[i*2][1]])
            magArrows.append([wireOffsets[i*2][0]-4*phases[i][counter],
                              wireOffsets[i*2][1]])
            magArrows.append([wireOffsets[i*2][0],
                              wireOffsets[i*2][1]+4*phases[i][counter]])
            magArrows.append([wireOffsets[i*2][0],
                              wireOffsets[i*2][1]-4*phases[i][counter]])
            magArrows.append([wireOffsets[(i*2)+1][0]+4*phases[i][counter],
                              wireOffsets[(i*2)+1][1]])
            magArrows.append([wireOffsets[(i*2)+1][0]-4*phases[i][counter],
                              wireOffsets[(i*2)+1][1]])
            magArrows.append([wireOffsets[(i*2)+1][0],
                              wireOffsets[(i*2)+1][1]+4*phases[i][counter]])
            magArrows.append([wireOffsets[(i*2)+1][0],
                              wireOffsets[(i*2)+1][1]-4*phases[i][counter]])

        markers = []
        for phase in phases:
            markers.append('v')
            markers.append('^')
            markers.append('>')
            markers.append('<')
            markers.append('^')
            markers.append('v')
            markers.append('<')
            markers.append('>')

        fieldCounter = 0
        for magArrow in magArrows:
            ax1.plot(magArrow[0], magArrow[1], marker=markers[fieldCounter], color='grey')
            fieldCounter += 1

        # Plotting the overall magnetic field
        ax1.arrow(-magField[0][counter], -magField[1][counter],
                  2*magField[0][counter], 2*magField[1][counter], color='grey', width=0.3)

        # Plotting the currents
        counterPhase = 0
        for phase in phases:
            ax2.plot(tRange[0:counter], phase[0:counter], color=wireColors[counterPhase])
            ax2.plot(tRange[counter], phase[counter], marker='o', markersize=2, color=wireColors[counterPhase])
            counterPhase += 2

        # Formatting Plots
        ax1.axis('equal')
        ax1.set_xlim([-10, 10])
        ax1.set_ylim([-10, 10])
        ax1.set_axis_off()
        ax2.set_xticks([])
        ax2.set_xticks([], minor=True)
        ax2.set_yticks([])
        ax2.set_yticks([], minor=True)
        ax2.set_xlim([0, 0.06])
        ax2.set_ylim([-1.1, 1.1])

        # Saving frame
        filePath = sys.path[0] + f'/frames/frame {counter+1}.png'
        fig.savefig(filePath, dpi=dpiArg)
        print(f'Frame {counter+1} done, {round(100*(counter+1)/len(tRange), 2)}%.')