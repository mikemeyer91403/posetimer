# Posetimer
#
# 
from PIL import Image

#TODO: make an enum for the sequence type
# once, random, looping

def main():

    # These are default values
    defaultImagePath = "./images"
    defaultPoseDuration = 120
    sequenceType = "once"

    currentPath = defaultImagePath
    poseDuration = defaultPoseDuration
    currentImage = 'images/test1.png'


    print("Posetimer:  Starting pose sequence")
    print(f"Displaying poses from  {currentPath} for {poseDuration} seconds")

    print (f"Now displaying:  {currentImage}")
    with Image.open(currentImage) as img:
        img.load()
        img.show()
    with Image.open("images/test2.jpg") as img:
        img.load()
        img.show()

main()

    


