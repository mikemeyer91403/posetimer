from enum import Enum
from random import randint

class SequenceType(Enum):
    LOOP = "loop"       #plays over and over
    ONCE = "once"       #plays the list once
    RANDOM = "random"   # select a random image

class Sequencer():



    def __init__(self, type, file_list, duration=30, name=None):
        self.type = type     #SequenceType for the playlist
        # file list is a list of filename strings
        #TODO: do we want this to just be a list of abspaths, or do we want
        # to pass a root directory, and build the names ourselves?
        # we will pre-filter this list of files and pass it only valid image files
        self.files = file_list
        self.duration = duration
        self.name = name  #this is a placeholder for named lists
        self.currentindex = 0

    def __repr__(self):
        return f"Sequencer: name={self.name}, type={self.type}, duration={self.duration}\n {len(self.files)} files:{self.files}"

    def num_files(self):
        return len(self.files)
    
    def first_file(self):
        if len(self.files) != 0:
            return self.files[0]
    

    def next_file(self):
        if self.type == SequenceType.RANDOM:
            if (len(self.files)!= 0):
                rand = random.choice(self.files)
            else:
                rand = None
            #TODO: come up with random function
            return rand
        if self.type == SequenceType.LOOP:
            self.currentIndex += 1
            if self.currentIndex == len(self.files):
                self.currentIndex = 0
            return self.files[self.currentIndex]
        if self.type == SequenceType.ONCE:
            self.currentIndex +=1
            if self.currentIndex == len(self.files):
                return None
            


        