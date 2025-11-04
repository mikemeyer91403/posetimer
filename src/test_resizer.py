import unittest
import os
from resizer import fit_image

class TestResizer(unittest.TestCase):

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

    # case 5: we treat square as a fit to height case, but it is likely rare for this content

    def test_square_canvas_portrait(self):
        resize = fit_image((100,300), (600,600))
        self.assertEqual(resize[0],200)
        self.assertEqual(resize[1], 600)

    def test_square_canvas_landscape(self):
        resize = fit_image((300,100), (600,600))
        self.assertEqual(resize[0],600)
        self.assertEqual(resize[1], 200)
    
    def test_square_canvas_big(self):
        resize = fit_image((300,300), (600,600))
        self.assertEqual(resize[0],600)
        self.assertEqual(resize[1], 600)

    def test_square_canvas_shrink(self):
        resize = fit_image((3000,3000), (600,600))
        self.assertEqual(resize[0],600)
        self.assertEqual(resize[1], 600)


#TODO: further test cases for 
# landscape to landscape shrink, grow
# portrait to portrait shrink, grow
# landscape fitting in portrait window, grow
# landscape fitting in portrait window, shrink
# portrait fitting in landscape window, grow
# portrait fitting in landscape window, shrink

