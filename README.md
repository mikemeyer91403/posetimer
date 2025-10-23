# posetimer
A python script for timed display of multiple images.

## Purpose
The purpose of this script is for quicksketch drawing practice.  The user will select a directory containing image files of drawing poses, select a time per pose, and whether images are displayed in directory/alphabetical order, or in a random order.    

While the user will be able to select any duration for the images,  in general this is intended to display poses in fairly small increments, like 30 seconds, 1 or 2 minutes, or 5-10 minutes for longer pose.    An excellent example of the type of tool this is emulating is the SketchDaily www.sketchdaily.net website, but this will use the user's own reference materials, and won't require the web.  Also, the intention behind building this in python is to be able to use it on numerous platforms, like Raspberry Pi. 

# Syntax:
```
usage: posetimer.py [-h] [-d DURATION] [-r | -l | -o] [--ipath [IPATH]]

options:
  -h, --help            show this help message and exit
  -d, --duration DURATION
                        number of seconds to display each image (default: 12)
  -r, --random          cycle through images in random order
  -l, --loop            loop images in directory order
  -o, --once            cycle through images once (default mode)
  --ipath [IPATH]       path to directory with images to display (default:
                        ./images)
```

# Installation instructions:
(tbd)
Probably will be using Pillow and TKinter, playsound for sound playback

# Roadmap TO MVP
1. command line argument handling
2. set default values for ordering, folder path, length of pose, window size
1. set up image viewer and ability to display single image  (initial selection is in ./images)
2. set up basic file list structure 
3. implement timed sequence from test file list
4. build file list from directory argument
5. files in directory order
6. assure that files are images, skip non-image file
7. file list sequencer and random mode

# Extensions
1. set default values for ordering, folder path, number of seconds or minutes in .poserc file
2. update display window to use tkinter GUI
3. play sound when image changes and 80% point in pose
4. use tkinter to provide enhanced GUI layout
5. GUI Add large countdown timer
6. in directory mode, show 1 of n counter
7. Enhanced transition between images if needed (crossfade)
8. show list of poses and current image name?
9. incorporate a GUI file picker
10. enhanced file list management - multiple list management, and named lists
11. save file lists/directories in .poserc
12. build custom file list across directories?
13. Export a list playback as a video?
   



