import numpy as np
import matplotlib.pyplot as plt
import sys
from functions.plotVector import plotVector

# Program plots the line voltage phasor and magnitude at different parts of a transmission line

def voltageSag():
    # Define Parameters
    L = 4e-3                # Line inductance
    V = 400                 # Sending & receiving voltage amplitude
    delta = np.deg2rad(30)  # Phase angle between the sending and receiving voltages
    # Defining parameters done

    # Voltage Phasors
    Vs = [V * np.cos(delta/2), V * np.sin(delta/2)]
    Vr = [V * np.cos(-delta/2), V * np.sin(-delta/2)]

    x = [Vs, Vr, 0]

    legend = ['Vs', 'Vr', 'Vl']

    # range across the line
    kNum = 100
    kRange = np.linspace(0, 1, kNum)

    VlList = []

    counter = 1
    print('Beginning to render frames.')
    for k in kRange:
        
        # Line voltage
        VlA = V * np.sqrt(1 + 4*k*(k-1)*(np.sin(delta/2))**2)
        VlList.append(VlA)

        # Line voltage phase angle
        theta = delta/2 - k*delta

        # Line voltage phasor
        Vl = [VlA * np.cos(theta), VlA * np.sin(theta)]
        x[2] = Vl

        # Plotting
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8), dpi=100)
        ax1.set_title(f'Voltage Sag, k ={round(k, 2)}')

        # Plotting the phasors
        plotVector(ax1, x, legend)

        #Plotting the magnitude
        ax2.plot(kRange[0:len(VlList)], VlList, color='orange')
        ax2.plot(kRange[counter-1], VlA, marker='D', color='red')
        ax2.set_xlim(-0.05, 1.05)
        ax2.set_ylim(0.8*V, 1.1*V)
        ax2.legend([f'Vl = {round(VlA)}'])
        ax2.grid()

        # Saving frame
        filePath = sys.path[0] + f'/frames/frame {counter}.png'
        fig.savefig(filePath, dpi=100)
        print(f'Frame {counter} done, {round(100*counter/len(kRange), 2)}%.')
        counter += 1
    print('Frame rendering done.')


