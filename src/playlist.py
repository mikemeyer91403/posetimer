import os


class PlayList():

    def __init__(self, filepath):
        self.basePath = filepath
        self.absBasePath = os.path.abspath(filepath)
        if (not os.path.exists(self.absBasePath)):
            raise FileExistsError(f"Directory {filepath} not found")
        self.imagePaths = []
        self.imageNames = []

    def load(self):
        # we may have already loaded absPath, make sure we do load it otherwise 
        # we also need to check in case we've changed base path.
        absPath = os.path.abspath(self.basePath)
        if self.absBasePath != absPath:
            self.absBasePath = absPath

        if not os.path.exists(self.absBasePath):
            raise FileExistsError(f":directory {self.absBasePath} not found")
        else:
            self.imagePaths, self.ImageNames = get_directory_list(self.basePath)
        self.imageNames.sort()
        self.imagePaths.sort()

    def absolutePath(self):
        return self.absBasePath
    
    def setNewBasePath(self,newPath):
        savedPath = self.basePath
        if newPath:
            self.basePath = newPath
            absPath = os.path.abspath(newPath)
            if os.path.exists(absPath):
                self.absBasePath = absPath
            else:
                # report error and keep paths the same
                print(f"Error: new path {newPath} does not exist, not changed")
                self.basePath = savedPath

    
    def image_count(self):
        return len(self.imagePaths)
    
    def files(self):
        return self.imagePaths
    
#### end of instance methods
    
def get_directory_list(basePath):
    path = basePath
    absPath = os.path.abspath(basePath)
    #verified that our paths are correct
    #print(f"BASEPATH:{basePath}\nABSPATH:{absPath}")
    # this is a list of the file names before filtering
    raw_list = os.listdir(absPath)

    # we want to save
    imageNames = []
    paths = []

    for name in raw_list:
        if is_image(absPath, name):
            imageNames.append(name)
            paths.append(os.path.join(absPath, name))
    # if we loaded any images, then update
    # we return the lists of full paths and a list of just names in case we want to display
    #print(paths)
    #print(imageNames)
   
    if (len(paths) !=0 and paths != None and imageNames != None):
        return paths, imageNames
    else:
        return [], []
    



def is_image(abspath, filename):
    valid_ext = ["jpg", "png", "gif", "jpeg"]

    filepath = os.path.join(abspath, filename)
    if not os.path.isfile(filepath) or not os.path.exists(filepath):
        return False
    nameparts = filename.split(".", maxsplit=1)
    if len(nameparts)>1:
        ext = nameparts[1]
    else:
        return False
    if ext in valid_ext:
        return True
    return False
       


