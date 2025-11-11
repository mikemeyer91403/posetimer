import tkinter as tk
from PIL import Image, ImageTk

def fit_image(size, canvas_size):
    # c = tk.Canvas(canvas)
    # cwidth = c.winfo_width()
    # cheight= c.winfo_height()
    cwidth = canvas_size[0]
    cheight = canvas_size[1]
    #print(f"Fit Image: original size: {size}")
    #print(f" Fitting to: ({cwidth},{cheight})")

    oldsize = size
    newsize = size

    width = size[0]
    height = size[1]
    canvas_aspect = cwidth / cheight
    image_aspect =  width/height



    ##  case 1: canvas is landscape and image is landscape
    ## if image aspect is larger, then we fit to the canvas width
    ## im image aspect is smaller, we fit to canvas height

    ## case 2: canvas is landscape and image is portrait, 
    ## we fit to canvas height (image aspect is smaller)

    ## case 3 canvas is portrait and image is landscape:
    ## we fit to canvas width (image aspect is larger)

    ## case 4 canvas is portrait and image is portrait
    # if image aspect is larger, we fit to canvas width
    # if image aspect is smaller, we fit to canvas height

    fit_to_width = (image_aspect > canvas_aspect)

    if (fit_to_width):
        #print("fitting to width")
        new_width = int(cwidth)
        new_height = int((height * new_width) / width)
        newsize = (new_width, new_height)
    else:
        #print("fitting to height")
        new_height = int(cheight)
        new_width = int((width * new_height)/height)
        newsize = (new_width, new_height)
    print (f"Fit Image: New Size: {newsize}")
    return newsize

    

