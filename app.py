from functions.animate import createAnimation, clearFrames
from functions.acPowerFlow import acPowerFlow
from functions.voltageSag import voltageSag
from functions.abFrame import abFrame
from functions.rotMagField import rotMagField
from functions.statorMagField import statorFields

# Select which animation to generate and enter the file name

def main():
    clearFrames()
    #rotMagField(400, (6, 3), 200)
    #voltageSag()
    #abFrame()
    #acPowerFlow()
    statorFields()
    createAnimation(fileName='Stator Magnetic Fields', reverse=False)
    
if __name__ == '__main__':
    main()

    