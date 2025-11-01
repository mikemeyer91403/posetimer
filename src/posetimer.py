#Posetimer
#
# 
import tkinter as tk
import os
import argparse
from PIL import Image, ImageTk
from sequencer import SequenceType, Sequencer
from playlist import PlayList

#configure_parser
# sets up the argparse parser behavior
def configure_parser(parser, default_duration, default_path):
    parser.add_argument("-d", "--duration", type=int, default = default_duration, help="number of seconds to display each image (default: %(default)s) ")
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("-r","--random", action ="store_true", help="cycle through images in random order")
    group.add_argument("-l", "--loop", action ="store_true", help="loop images in directory order")
    group.add_argument("-o", "--once", action ="store_true", default=True, help="cycle through images once (default mode)")
    parser.add_argument("--ipath", nargs="?", default=default_path, help="path to directory with images to display (default: %(default)s)")  


def present_new_image(root, canvas, sequencer, poseDuration):
    #canvas.create_image(10,10, image = None, anchor = tk.NW)
    nextImg = sequencer.next_file()
    if (nextImg != None):
        try: 
            print(f"Opening {os.path.abspath(nextImg)}")
            with Image.open(nextImg) as pil_image:
                print(f"Image {nextImg}:  {pil_image.size}")
        # TODO: we'll want to get the image size and scale it to fit canvas size if needed.
                tk_image = ImageTk.PhotoImage(pil_image)
                canvas.create_image(10,10, image = tk_image, anchor = tk.NW)
            #root.after((poseDuration * 1000), present_new_image,root,canvas,sequencer,poseDuration)
        except FileNotFoundError:
            print(f"Error: file \'{nextImg}\' not found. Please provide valid image path and name.")




def main():

    # These are our default values
    defaultImagePath = "./images"
    defaultPoseDuration = 5
    defaultSequenceType = SequenceType.ONCE

    currentPath = defaultImagePath
    poseDuration = defaultPoseDuration
    sequenceType = defaultSequenceType
    currentImage = 'images/test1.png'

    ####################################################################
    #Command line parsing
    ####################################################################

    parser = argparse.ArgumentParser()
    configure_parser(parser, defaultPoseDuration, defaultImagePath)
    args = parser.parse_args()
    #TODO: can supress this print once more testing is done
    print (args)
    ####################################################################
    # process any overrides from the command line
    ####################################################################

    if args.duration:
        poseDuration = args.duration
    if args.ipath:
        currentPath = args.ipath

    # these modes are mutually exclusive
    if args.random:
        sequenceType = SequenceType.RANDOM
    elif args.loop:
        sequenceType = SequenceType.LOOP
    else:
        sequenceType = SequenceType.ONCE

    #TODO: This is also active for troubleshooting
    print(f"Duration: {poseDuration}\nSequenceType:{sequenceType}\nimagePathRoot:{currentPath}")

    ####################################################################
    # generate a playlist from the specified image directory
    # resulting list will be image files only, sorted in directory order
    # Will throw error if no files in resulting playlist
    ####################################################################
    playlist = PlayList(currentPath)
    playlist.load()
    if playlist.image_count == 0:
        print(f"Error: no images in directory {playlist.fullPath}")
        import sys; sys.exit()


    ####################################################################
    # instantiate a sequencer with the playlist and sequence type
    ####################################################################
    sequencer = Sequencer(sequenceType, playlist.imagePaths, poseDuration)

    # Start value for the countdown
    timeRemaining = poseDuration

    # setting up the canvas
    root = tk.Tk()
    root.title("Pose Timer")
    label = tk.Label(root, text ="Pose Timer")
    label.pack(pady=10)
    canvas = tk.Canvas(root, width=1000, height = 1000, bg = "lightgray")
    canvas.pack(pady=10)

   # present_new_image(root,canvas,sequencer,poseDuration)

    currentImage = sequencer.first_file()
    if(currentImage == None):
        import sys; sys.exit()
    def update_screen(currentImage):
        if (currentImage != None):
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
            currentImage = sequencer.next_file()
            root.after((1000 * poseDuration),update_screen, currentImage)

    update_screen(currentImage)

    root.mainloop()
    # print("Posetimer:  Starting pose sequence")
    # print(f"Displaying poses from  {currentPath} for {poseDuration} seconds")

    # print (f"Now displaying:  {currentImage}")
    # with Image.open(currentImage) as img:
    #     img.load()
    #     img.show()
    
   

main()

    


