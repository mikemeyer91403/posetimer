from enum import Enum
import random

class SequenceType(Enum):
    LOOP = "loop"       #plays over and over
    ONCE = "once"       #plays the list once
    RANDOM = "random"   # select a random image


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
        self.currentindex = 0

    def __repr__(self):
        return f"Sequencer: name={self.name}, type={self.type}, duration={self.duration}\n {len(self.files)} files:{self.files}"

    def num_files(self):
        return len(self.files)
    
    def first_file(self):
        if len(self.files) != 0:
            return self.files[0]
        else:
            return None
    
# I think this is messed up, this seems to assume you use 
#first file and then 

    def next_file(self):
        if self.type == SequenceType.RANDOM:
            if (len(self.files)!= 0):
                rand = random.choice(self.files)
            else:
                rand = None
            return rand
        if self.type == SequenceType.LOOP:
            self.currentindex += 1
            if self.currentindex == len(self.files):
                self.currentindex = 0
            return self.files[self.currentindex]
        if self.type == SequenceType.ONCE:
            self.currentindex +=1
            if self.currentindex == len(self.files):
                return None
            return self.files[self.currentindex]
            


        