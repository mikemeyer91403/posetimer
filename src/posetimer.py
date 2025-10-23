#Posetimer
#
# 
import tkinter as tk
import os
import argparse
from PIL import Image, ImageTk
from sequencer import SequenceType

def configure_parser(parser, default_duration, default_path):
    parser.add_argument("-d", "--duration", type=int, default = default_duration, help="number of seconds to display each image (default: %(default)s) ")
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("-r","--random", action ="store_true", help="cycle through images in random order")
    group.add_argument("-l", "--loop", action ="store_true", help="loop images in directory order")
    group.add_argument("-o", "--once", action ="store_true", default=True, help="cycle through images once (default mode)")
    parser.add_argument("--ipath", nargs="?", default=default_path, help="path to directory with images to display (default: %(default)s)")  

def main():

    # These are default values
    defaultImagePath = "./images"
    defaultPoseDuration = 12
    defaultSequenceType = SequenceType.ONCE

    currentPath = defaultImagePath
    poseDuration = defaultPoseDuration
    sequenceType = defaultSequenceType
    currentImage = 'images/test1.png'

    parser = argparse.ArgumentParser()
    configure_parser(parser, defaultPoseDuration, defaultImagePath)
    # parser.add_argument("-d", "--duration", type=int, default = defaultPoseDuration, help="number of seconds to display each image (default: %(default)s) ")
    # group = parser.add_mutually_exclusive_group(required=False)
    # group.add_argument("-r","--random", action ="store_true", help="cycle through images in random order")
    # group.add_argument("-l", "--loop", action ="store_true", help="loop images in directory order")
    # group.add_argument("-o", "--once", action ="store_true", default=True, help="cycle through images once (default mode)")
    # parser.add_argument("--ipath", nargs="?", default="./images", help="path to directory with images to display (default: %(default)s)")
    args = parser.parse_args()
    print (args)

    if args.duration:
        poseDuration = args.duration
    if args.ipath:
        currentPath = args.ipath
    if args.random:
        sequenceType = SequenceType.RANDOM
    elif args.loop:
        sequenceType = SequenceType.LOOP
    else:
        sequenceType = SequenceType.ONCE

    print(f"Duration: {poseDuration}\nSequenceType:{sequenceType}\nimagePathRoot:{currentPath}")


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

    


