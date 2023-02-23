import numpy as np
import matplotlib.pyplot as plt
import sys

# Creates the frames for an animation of the rotating alpha beta vector of a three phase system

def abFrame():

    # Phase angles of phases A, B & C (Each 120 degrees out of phase)
    alpha = 0
    beta = 2*np.pi/3
    gamma = 4*np.pi/3

    # Defining parameters
    A = 3               #Phasor amplitude
    f = 50              #Frequency
    omega = 2*np.pi*f   #Rotational frequency
    # Parameters defined

    # Time range
    t = np.linspace(0, 0.02, 200)

    # Phasors
    a = A*np.cos(alpha - omega*t)
    b = A*np.cos(beta - omega*t)
    c = A*np.cos(gamma - omega*t)

    counter = 1
    print('Beginning to render frames.')
    for i in range(len(t)):
        omegaT = round(np.rad2deg(omega*t[i]), 2)
        plt.figure(figsize=(4, 4), dpi=200)

        # Plotting the phasors
        plt.plot([0, a[i] * np.cos(alpha)], [0, a[i] * np.sin(alpha)], marker='x', linewidth=2)
        plt.plot([0, b[i] * np.cos(beta)], [0, b[i] * np.sin(beta)], marker='x', linewidth=2)
        plt.plot([0, c[i] * np.cos(gamma)], [0, c[i] * np.sin(gamma)], marker='x', linewidth=2)

        # Clarke Transformation to get the ab phasor
        plt.plot([0, (2/3)*(a[i] * 1 + b[i] * -1/2 + c[i] * -1/2)],
                [0, (2/3)*(a[i] * 0 + b[i] * np.sqrt(3)/2 + c[i] * -np.sqrt(3)/2)],
                marker='x', linewidth=2)
        
        plt.title(f'Angle = {omegaT} degrees')
        plt.xlim([-5 * 1.01, 5 * 1.01])
        plt.ylim([-5 * 1.01, 5 * 1.01])
        plt.grid()
        # Saving frame
        filePath = sys.path[0] + f'/frames/frame {counter}.png'
        plt.savefig(filePath, dpi=100)
        print(f'Frame {counter} done, {round(100*counter/len(t), 2)}%.')
        counter += 1
    print('Done')