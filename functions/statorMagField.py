
import numpy as np
import matplotlib.pyplot as plt
import sys

# Program the creates the frames for an animation of the individual magnetic fields in a three-phase single pole stator, 
# as well as the overall magnetic field

def statorFields():

  # Defining the constants
  I = 10
  f = 50
  w = 2*np.pi*f
  N = 10
  # Constants defined

  # Defining the angluar and time ranges
  theta = np.linspace(0, 2*np.pi, 360)
  t = np.linspace(0, 0.02, 100)

  # Defining the currents
  iA = I*np.sin(w*t)
  iB = I*np.sin(w*t - 2*np.pi/3)
  iC = I*np.sin(w*t - 4*np.pi/3)

  # Looping through the time range
  counter = 1
  print('Beginning to render frames.')
  for k in range(len(t)):
    # Calculating the individual magnetic fields
    fA = N*iA[k]*np.cos(theta)
    fB = N*iB[k]*np.cos(theta - 2*np.pi/3)
    fC = N*iC[k]*np.cos(theta - 4*np.pi/3)

    # Calculating the ovarall magnetic field
    F = fA + fB + fC

    # Plotting
    plt.figure(figsize=(6, 4), dpi=400)
    plt.plot(theta, fA, color='blue')
    plt.plot(theta, fB, color='green')
    plt.plot(theta, fC, color='red')
    plt.plot(theta, F, color='black', linewidth=2)
    plt.xlim([0, 2*np.pi])
    plt.xticks([])
    plt.xticks([], minor=True)
    plt.yticks([])
    plt.yticks([], minor=True)

    # Saving frame
    filePath = f'{sys.path[0]}/frames/frame {counter}.png'
    plt.savefig(filePath, dpi=100)
    print(f'Frame {counter} done, {round(100*counter/len(t), 2)}%.')
    counter += 1
  print('Frame rendering done.')