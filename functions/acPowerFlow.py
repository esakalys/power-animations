import numpy as np
import matplotlib.pyplot as plt
import sys

# Program plots various electrical quantities for a simple electrical transmission system
# as a function of the phase angle between the sending and receiving voltages
# Generates the frames for an animation

def acPowerFlow():
    # Define Parameters
    f = 50              # Frequency
    omega = 2*np.pi*f   # Angular frequency

    L = 4e-3            # Line inductance
    Xl = omega * L      # Line reactance

    VrA = 339           # Receiving voltage amplitude
    VsA = 339           # Sending voltage amplitude
    # Defining parameters done

    # Angle and time ranges
    theta = np.linspace(0, 2*np.pi, 360)

    tNum = 10000
    t = np.linspace(0, 0.02, tNum)

    # Receiving voltage
    Vr = VrA * np.sin(omega*t)

    counter = 1
    print('Beginning to render frames.')
    for angle in theta:
        
        # Sending voltage
        Vs = VsA * np.sin(omega*t + angle)

        # Voltage across the line
        Vl = Vs - Vr

        # Current flowing through the line
        I = Vl/Xl

        # Shifting the current to account for the fact that it lags the line voltage by 90 degrees 
        Ishifted = np.zeros(tNum)
        for x in range(int(len(t)/4), len(t)):
            Ishifted[x] = I[int(x-len(t)/4)]
        for x in range(0, int(len(t)/4)):
            Ishifted[x] = I[int(x+len(t)*(3/4))]

        # Instantaneous power in kW
        P = (Ishifted*Vs)/1000

        # Plotting the waveforms
        plt.figure(figsize=(8, 8), dpi=100)
        plt.plot(t, Vs, label='Vs, V', color='#6D75F8', linewidth=2)
        plt.plot(t, Vr, label='Vr, V', color='#DA11F4', linewidth=2)
        plt.plot(t, Vl, label='Vl, V', color='#11DFF4', linewidth=2)
        plt.plot(t, Ishifted, label='I, A', color='#E62A11', linewidth=2)
        plt.plot(t, P, label='Power, kW', color='#2aa777', linewidth=2)
        plt.plot([0, 0.02], [np.average(P), np.average(P)],
                label='Average Power, kW = ' + str(round(np.average(P), 2)),
                linewidth=2, color='#2aa777', linestyle='--')
        plt.legend(loc=1)
        plt.title(f'Phase shift = {round(angle*(180/np.pi), 2)} degrees')
        plt.ylim([-700, 700])
        plt.tick_params(
            axis='x',  # changes apply to the x-axis
            which='both',  # both major and minor ticks are affected
            bottom=False,  # ticks along the bottom edge are off
            top=False,  # ticks along the top edge are off
            labelbottom=False)  # labels along the bottom edge are off
        plt.grid()

        # Saving frame
        filePath = sys.path[0] + f'/frames/frame {counter}.png'
        plt.savefig(filePath, dpi=100)
        print(f'Frame {counter} done, {round(100*counter/len(theta), 2)}%.')
        counter += 1
    print('Frame rendering done.')
