from enum import Enum
import random

class SequenceType(Enum):
    LOOP = "loop"       #plays over and over
    ONCE = "once"       #plays the list once
    RANDOM = "random"   # select a random image; this loops indefinitely
    #TODO: perhaps a random once feature that just picks one image at random?


class Sequencer():

# I don't think sequencer needs to know much about play lists, 
# I want it to just tell us the next file, and to return None if there isn't one.
# the file_list is literally just file names or abspaths

    def __init__(self, type, file_list, duration=30, name=None):
        self.type = type     #SequenceType for the playlist
        # file list is a list of filename strings
        #TODO: do we want this to just be a list of abspaths, or do we want
        # to pass a root directory, and build the names ourselves?
        # we will pre-filter this list of files and pass it only valid image files
        self.files = file_list
        self.duration = duration
        self.name = name  #this is a placeholder for named lists
        self.currentIndex = 0

    def __repr__(self):
        return f"Sequencer: name={self.name}, type={self.type}, duration={self.duration}\n {len(self.files)} files:{self.files}"

    def num_files(self):
        #print (f"numfiles: {len(self.files)}")
        #print(self.files)
        return len(self.files)
    
    def first_file(self):
        if len(self.files) != 0:
            self.currentIndex = 1
            return self.files[0]
        else:
            return None
    

    def next_file(self):
        if self.type == SequenceType.RANDOM:
            if (len(self.files)!= 0):
                #TODO: maybe make sure that we don't repeat
                # same image twice (except if single image list)
                rand = random.choice(self.files)
            else:
                rand = None
            return rand
        if self.type == SequenceType.LOOP:
            if self.currentIndex == len(self.files):
                self.currentIndex = 0
            next = self.files[self.currentIndex]
            self.currentIndex += 1
            return next
        if self.type == SequenceType.ONCE:
            if self.currentIndex == len(self.files):
                return None
            next = self.files[self.currentIndex]
            self.currentIndex += 1
            return next
            


        