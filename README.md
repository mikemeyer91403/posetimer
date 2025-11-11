# posetimer
A python script for timed display of multiple images.

## Purpose
The purpose of this script is for quicksketch drawing practice.  The user will select a directory containing image files of drawing poses, select a time per pose, and whether images are displayed in directory/alphabetical order, or in a random order.    

While the user will be able to select any duration for the images,  in general this is intended to display poses in fairly small increments, like 30 seconds, 1 or 2 minutes, or 5-10 minutes for longer pose.    An excellent example of the type of tool this is emulating is the SketchDaily www.sketchdaily.net website, but this will use the user's own reference materials, and won't require the web.  Also, the intention behind building this in python is to be able to use it on numerous platforms, like Raspberry Pi. 

# Syntax:
```
usage: posetimer.py [-h] [-d DURATION] [-r | -l | -o] [--ipath [IPATH]] [-w WIDTH] [-hh HEIGHT]

options:
  -h, --help            show this help message and exit
  -d, --duration DURATION
                        number of seconds to display each image (default: 5)
  -r, --random          cycle through images in random order
  -l, --loop            loop images in directory order
  -o, --once            cycle through images once (default mode)
  --ipath [IPATH]       path to directory with images to display (default: ./images)
  -w, --width WIDTH     canvas width in pixels (default: 1200)
  -hh, --height HEIGHT  canvas height in pixels (default: 1600)
```

# Installation instructions:


## Dependencies
I recommend that one builds this in a python venv, as there are some version dependencies
between Tkinder and different versions of python.  I had some issues installing on my Mac running Tahoe because the version of Python they ship with MacOS was not compatible with the most recent Tcl/Tk releases.  Apple's python gets the frameworks from Command Line Tools distribution, so if you've manually installed tkinder it will be put somewhere else.  Check out `INSTALL.md` for some tips, including Windows and Linux.

To set up a venv (on the Mac, the syntax for Windows is different):
```
python3 -m venv .venv
source .venv/bin/activate
```
I'm using 
- python 3.13.9
- Tcl/Tk 8.6.17
These versions are compatible, I had to install these via homebrew into the venv.  Instructions on how to do that are in the `INSTALL.md` file.
```
% pip list
Package Version
------- -------
pillow  12.0.0
pip     25.2
```


## testing/running
You should be able to run it from the root directory using
`./posetimer.sh`
To see all options, try 
`./posetimer.sh -h`
The shell script passes args down to the python script.

I've included a test script for running the unit tests.
`./test.sh`
This will run unit tests for the components that have them.

# Roadmap TO MVP
For my current purposes, the MVP is the feature set needed to display folders of poses in 
my archive, putting them up for a specified time for quickdraw.

1. ~~command line argument handling~~
2. ~~set default values for ordering, folder path, length of pose, window size~~
1. ~~set up image viewer and ability to display single image  (initial selection is in ./images)~~
2. ~~set up basic file list structure~~
3. ~~implement timed sequence from test file list~~
4. ~~build file list from directory argument~~
5. ~~update display window to use tkinter GUI~~
6. ~~files in directory order~~
7. ~~assure that files are images, skip non-image file~~
8. ~~file list sequencer (once, loop and random mode)~~
9. ~~Add GUI label for countdown timer~~
10. Display current file name  (Code there, need to learn more about tk layout, also not MVP)
10. ~~Refactor update_screen() to manage countdown as well as image changes.~~
11. ~~Add command line args for screen size, and set a sensible default in code.~~
12. ~~Update the posetimer.py script to pass args~~
11. ~~Further functional testing with local images.~~

# Possible future enhancements, by desirability
The upgrade path I have in mind is to make it easier to repeat a session I've done before and to
perhaps hand edit playlists.  

- A use case of selecting a session to draw with a gui, already I think it will save a lot of time
- also a use case of taking any current playlist and saving it in a list of favorites that I can recall later.

1. incorporate a GUI file picker to select folder
2. Get the current file name label working (need to spend more time learning tk layout techniques)
3. make the countdown timer bigger and bolder 
3. Label showing total number of images and current count, when appropriate
1. set default values for ordering, folder path, number of seconds or minutes in .poserc file
3. play sound when image changes and 80% point in pose
3. Change timer font color to red at end of pose
4. split layout with file list and image (list of poses and image name)?
7. Enhanced transition between images, like cross fades or fading at end?
10. enhanced file list management - multiple list management, and named lists
11. save file lists/directories in .poserc or .poselists file that can be hand edited
12. build custom file list across directories?
   



