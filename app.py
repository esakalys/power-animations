from functions.animate import createAnimation, clearFrames
from functions.acPowerFlow import acPowerFlow
from functions.voltageSag import voltageSag
from functions.abFrame import abFrame
from functions.rotMagField import rotMagField

# Select which animation to generate and enter the file name

def main():
    clearFrames()
    #rotMagField(400, (6, 3), 200)
    #voltageSag()
    #abFrame()
    #acPowerFlow()
    #createAnimation(fileName='Rotating Magnetic Field lowRes', reverse=False)
    
if __name__ == '__main__':
    main()

    