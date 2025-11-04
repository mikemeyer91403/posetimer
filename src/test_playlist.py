import unittest
import os
from playlist import PlayList, get_directory_list, is_image

class TestPlaylist(unittest.TestCase):

    def test_init(self):
      pl = PlayList("testimg/list1")
      self.assertIsNotNone(pl)
      self.assertEqual(pl.basePath, "testimg/list1")
    
      

    def test_load(self):
        pl = PlayList("testimg/list3")
        pl.load()
        self.assertEqual(pl.image_count(), 3)
        print(os.path.abspath(pl.absolutePath()))
        expectedPaths = []
        for i in range(3):
           expectedPaths.append(os.path.join(os.path.abspath("testimg/list3"),f"img{i+1}.jpg"))
        print(f"Expected:{expectedPaths}")
        print(f"Actual:{pl.imagePaths}")
        self.assertEqual(pl.imagePaths, expectedPaths)


    def test_set_new_base_path(self):
        pl = PlayList("./images")
        self.assertEqual(pl.basePath, "./images")
        pl.setNewBasePath("testimg/list1")
        absPath = os.path.abspath("testimg/list1")
        self.assertEqual (pl.basePath, "testimg/list1")
        self.assertEqual(pl.absolutePath(), absPath)
        self.assertEqual(pl.absBasePath, absPath)


    def test_absolute_path(self):
        pl = PlayList("./images")
        #TODO: don't hardcode this, use os to generate it
        self.assertEqual(pl.absolutePath(), "/Users/mikemeyer/bootdevclass/github.com/mikemeyer91403/posetimer/images")
        self.assertEqual(pl.absolutePath(), os.path.abspath("./images"))
        #pl2 = PlayList()
        #self.AssertEqual(pl2.absolutePath(), "")
    

    def test_image_count_happy(self):
        pl = PlayList("./testimg/list1")
        pl.load()
        self.assertEqual(pl.image_count(), 3)
       

    def test_image_count_filter(self):
        pl = PlayList("./testimg/list2")
        pl.load()
        self.assertEqual(pl.image_count(), 6)

    def test_get_directory_list(self):
        self.maxDiff = None
        imagePaths, imageNames = get_directory_list("./testimg/list1")
        self.assertEqual( len(imagePaths), 3)
        self.assertEqual(len(imageNames), 3)
        filenames = ["test1.png","test2.jpg","test3.png"]
        expectedPaths = []
        for file in filenames:
           expectedPaths.append(os.path.join(os.path.abspath("testimg/list1"),file))
        imagePaths.sort()
        imageNames.sort()
        #print(f"Expected:{expectedPaths}")
        #print(f"Actual:{imagePaths}")
        self.assertEqual(imagePaths ,expectedPaths)
        self.assertEqual(imageNames, filenames)


    def test_is_image(self):
        self.assertTrue(is_image(os.path.abspath("./testimg/list2"), "img1.jpg"))
        self.assertTrue(is_image(os.path.abspath("./testimg/list2"), "img4.png"))
        self.assertTrue(is_image(os.path.abspath("./testimg/list2"), "img5.jpeg"))
        self.assertTrue(is_image(os.path.abspath("./testimg/list2"), "img6.gif"))


        self.assertFalse(is_image(os.path.abspath("./testimg/list2"), "list0"))  #directory
        self.assertFalse(is_image(os.path.abspath("./testimg/list2"), "README.md"))
        self.assertFalse(is_image(os.path.abspath("./testimg/list2"), "doesntexist"))


        

    def test_files(self):
        pl = PlayList("./testimg/list1")
        pl.load()
        filenames = ["test1.png","test2.jpg","test3.png"]
        expectedPaths = []
        for file in filenames:
           expectedPaths.append(os.path.join(os.path.abspath("testimg/list1"),file))
        expectedPaths.sort()
        self.assertEqual(pl.files(),expectedPaths)

