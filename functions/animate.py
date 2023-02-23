import sys
import os
import imageio
from natsort import natsorted

# Program makes an animation out of the frames stored in /frames

def readFrames(reverse):
    directory = sys.path[0] + '/frames'

    frames = os.listdir(directory)
    frames = natsorted(frames)

    frameNum = len(frames)-1
    if reverse:
        frameNum *= 2

    images = []
    counter = 1
    print('Reading frames started.')
    for frame in frames:
        if frame != '.gitignore':
            file = directory + f'/{frame}'
            images.append(imageio.imread(file))
            print(f'Frame {counter} done, {round(100*counter/frameNum, 2)}%.')
            counter += 1

    if reverse:
        frames = natsorted(frames, reverse=True)
        for frame in frames:
            if frame != '.gitignore':
                file = directory + f'/{frame}'
                images.append(imageio.imread(file))
                print(f'Frame {counter} done, {round(100*counter/frameNum, 2)}%.')
                counter += 1

    print('Reading frames complete.')
    return images

def createAnimation(fileName, reverse=False):
    filePath = sys.path[0]+f'/animations/{fileName}.gif'

    images = readFrames(reverse)

    print('Rendering.')
    imageio.mimsave(filePath, images, fps=24)
    print('Done.')

def clearFrames():
    directory = sys.path[0] + '/frames'
    frames = os.listdir(directory)
    for frame in frames:
        if frame != '.gitignore':
            file = directory + f'/{frame}'
            os.remove(file)