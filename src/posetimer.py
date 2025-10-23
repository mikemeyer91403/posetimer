#Posetimer
#
# 
import tkinter as tk
import os
from PIL import Image, ImageTk
from sequencer import SequenceType

def main():

    # These are default values
    defaultImagePath = "./images"
    defaultPoseDuration = 12
    defaultSequenceType = SequenceType.ONCE

    currentPath = defaultImagePath
    poseDuration = defaultPoseDuration
    sequenceType = defaultSequenceType
    currentImage = 'images/test1.png'




    # setting up the canvas
    root = tk.Tk()
    canvas = tk.Canvas(root, width=1000, height = 1000, bg = "lightgray")
    canvas.pack(pady=10)

    try: 
        print(f"Opening {os.path.abspath(currentImage)}")
        with Image.open(currentImage) as pil_image:
            print(f"Image {currentImage}:  {pil_image.size}")
        # TODO: we'll want to get the image size and scale it to fit canvas size if needed.
            tk_image = ImageTk.PhotoImage(pil_image)
            canvas.create_image(10,10, image = tk_image, anchor = tk.NW)
            canvas.image = tk_image # keeping a reference for later
    except FileNotFoundError:
        print(f"Error: file \'{currentImage}\' not found. Please provide valid image path and name.")


    root.mainloop()
    # print("Posetimer:  Starting pose sequence")
    # print(f"Displaying poses from  {currentPath} for {poseDuration} seconds")

    # print (f"Now displaying:  {currentImage}")
    # with Image.open(currentImage) as img:
    #     img.load()
    #     img.show()
    
   

main()

    


