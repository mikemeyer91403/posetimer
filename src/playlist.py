class PlayList():

    def __init__(self, filepath):
        self.basePath = filepath
        self.absBasePath = ""
        self.imagePaths = ["images/test1.png", "images/test2.jpg", "images/test3.png"]

    def load(self):
        # generate absBasePath base on basePath
        # self get_directory_list
        pass

    
    def image_count(self):
        return len(self.imagePaths)
    
    def get_directory_list(self, basePath):
        # get list of file names
        # filter through the list for image extensions
        # build a list of abspaths on the list of filtered names
        # return the filtered list of abspaths
        #
        return ["images/test1.png", "images/test2.jpg", "images/test3.png"]

    def is_image(self, filename):
        # if file isDir, false
        # if file extension is one of the supported image types, true
        # extract image 
        pass

    def files(self):
        return ["images/test1.png", "images/test2.jpg", "images/test3.png"]

