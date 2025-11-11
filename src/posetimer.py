#Posetimer
#
# 
import tkinter as tk
import os
import argparse
from PIL import Image, ImageTk
from sequencer import SequenceType, Sequencer
from playlist import PlayList
from resizer import fit_image

#configure_parser
# sets up the argparse parser behavior
def configure_parser(parser, default_duration, default_path, default_width, default_height):
    parser.add_argument("-d", "--duration", type=int, default = default_duration, help="number of seconds to display each image (default: %(default)s) ")
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("-r","--random", action ="store_true", help="cycle through images in random order")
    group.add_argument("-l", "--loop", action ="store_true", help="loop images in directory order")
    group.add_argument("-o", "--once", action ="store_true", default=True, help="cycle through images once (default mode)")
    parser.add_argument("--ipath", nargs="?", default=default_path, help="path to directory with images to display (default: %(default)s)")  
    parser.add_argument("-w", "--width", type=int, default=default_width, help="canvas width in pixels (default: %(default)s) ")
    parser.add_argument("-hh", "--height", type=int, default=default_height, help="canvas height in pixels (default: %(default)s) ")


def timestring(remainingSeconds):
    sec =int( remainingSeconds % 60)
    min = int(remainingSeconds / 60)
    return (f"{min}:{sec:02d}")

########################################################
######  Main
########################################################
def main():

    # These are our default values
    defaultImagePath = "./images"
    defaultPoseDuration = 5
    defaultSequenceType = SequenceType.ONCE
    defaultHeight = 1600
    defaultWidth = 1200

    currentPath = defaultImagePath
    poseDuration = defaultPoseDuration
    sequenceType = defaultSequenceType
    currentImage = 'images/test1.png'
    currentHeight = defaultHeight
    currentWidth = defaultWidth

    ####################################################################
    #Command line parsing
    ####################################################################

    parser = argparse.ArgumentParser()
    configure_parser(parser, defaultPoseDuration, defaultImagePath, defaultWidth, defaultHeight)
    args = parser.parse_args()
    #TODO: can suppress this print once more testing is done
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

    if args.width:
        currentWidth = args.width
    if args.height:
        currentHeight = args.height
    

    #TODO: This is also active for troubleshooting
    print(f"Duration: {poseDuration}\nSequenceType:{sequenceType}\nimagePathRoot:{currentPath}")

    ####################################################################
    # generate a playlist from the specified image directory
    # resulting list will be image files only, sorted in directory order
    # Will throw error if no files in resulting playlist
    ####################################################################
    playlist = PlayList(currentPath)
    playlist.load()
    if playlist.image_count() == 0:
        print(f"Error: no images in directory {playlist.absBasePath}")
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
    timerLabel = tk.Label(root, text ="Pose Timer")
    timerLabel.pack(pady=10)


    canvas = tk.Canvas(root, width=currentWidth, height = currentHeight, bg = "lightgray")
    #canvas.pack(pady=10)
    canvas.pack(fill="both", expand=True)

    imageLabel = tk.Label(root, text = "Image Name")
    imageLabel.pack(pady=10)

    currentImage = sequencer.first_file()
    if(currentImage == None):
        import sys; sys.exit()

    #####
    ##### Inline Screen Update
    #####
    def update_screen(currentImage, timerLabel, imageLabel, poseDuration, remainingSeconds):
        #print (f"update_screen: {currentImage} {remainingSeconds}")
        timerLabel.config (text = timestring(remainingSeconds))
        shortImageName = ''
        if currentImage:
            shortImageName = os.path.split(currentImage)[1]
        finished = False
        if (currentImage != None and remainingSeconds == 0):
            try: 
                print(f"Opening {os.path.abspath(currentImage)}")
                with Image.open(currentImage) as pil_image:
                    canvas_size = (canvas.winfo_reqwidth(), canvas.winfo_reqheight())
                    print(f"Image {shortImageName}:  {pil_image.size}")
                    print(f"Canvas size: {canvas.winfo_reqwidth()}, {canvas.winfo_reqheight()}")
                    
                # TODO: this may be a naive way to handle tk canvas, and canvas might
                # not be the best/lightest way to display image, given we aren't drawing on it
                    oldsize = pil_image.size
                    newsize = fit_image(oldsize, canvas_size)
                    pil_image = pil_image.resize(newsize)

                    tk_image = ImageTk.PhotoImage(pil_image)
                    canvas.create_image(10,10, image = tk_image, anchor = tk.NW)
                    canvas.image = tk_image # keeping a reference for later
            except FileNotFoundError:
                print(f"Error: file \'{currentImage}\' not found. Please provide valid image path and name.")

            imageLabel.config(text = shortImageName)
            currentImage = sequencer.next_file()
            remainingSeconds = poseDuration
            timerLabel.config (text = timestring(remainingSeconds))
            remainingSeconds -=1
        else:
            if (remainingSeconds > 0):
                remainingSeconds -=1
        finished = (remainingSeconds == 0 )and (currentImage == None ) 
        if finished:
            print (f"finished: {finished}") 

        if (not finished):
            root.after(1000, update_screen, currentImage, timerLabel, imageLabel, poseDuration,remainingSeconds)
    ######
    ###### End Inline Screen update
    ######

    # start with initial value of 0 to load immediately
    update_screen(currentImage, timerLabel, imageLabel, poseDuration, 0)

    root.mainloop()
#######################################################
##### End Main    
#######################################################
  

main()

    


