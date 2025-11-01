import unittest

from sequencer import Sequencer, SequenceType

class TestSequencer(unittest.TestCase):

    def test_init(self):
        file_list = ["file1.jpg", "file2.jpg", "file3.jpg", "file4.jpg"]
        seq = Sequencer(SequenceType.LOOP, file_list)
        self.assertEqual(seq.num_files(), 4)
        self.assertEqual(seq.type, SequenceType.LOOP)
        self.assertEqual(seq.duration, 30) #default
        self.assertIsNone(seq.name)
        


    def test_num_files(self):
        file_list = ["file1.jpg", "file2.jpg", "file3.jpg", "file4.jpg"]
        seq = Sequencer(SequenceType.LOOP, file_list)
        self.assertEqual(seq.num_files(), 4)
    
    def test_first_file(self):
        file_list = ["file1.jpg", "file2.jpg", "file3.jpg", "file4.jpg"]
        seq = Sequencer(SequenceType.LOOP, file_list)
        self.assertEqual(seq.first_file(), "file1.jpg")

    def test_next_file(self):
        file_list = ["file1.jpg", "file2.jpg", "file3.jpg", "file4.jpg"]
        seq = Sequencer(SequenceType.LOOP, file_list)
        self.assertEqual(seq.next_file(), "file1.jpg")
        self.assertEqual(seq.next_file(), "file2.jpg")
        self.assertEqual(seq.next_file(), "file3.jpg")
        self.assertEqual(seq.next_file(), "file4.jpg")
        self.assertEqual(seq.next_file(),"file1.jpg")



    def test_once_seqtype(self):
        file_list = ["file1.jpg", "file2.jpg", "file3.jpg", "file4.jpg"]
        seq = Sequencer(SequenceType.ONCE, file_list)
        self.assertEqual(seq.next_file(), "file1.jpg")
        self.assertEqual(seq.next_file(), "file2.jpg")
        self.assertEqual(seq.next_file(), "file3.jpg")
        self.assertEqual(seq.next_file(), "file4.jpg")
        self.assertIsNone(seq.next_file())

    def test_random_seqtype(self):
        file_list = ["file1.jpg", "file2.jpg", "file3.jpg", "file4.jpg"]
        seq = Sequencer(SequenceType.RANDOM, file_list)
        for i in range(6):
            next = seq.next_file(); print(next)
            self.assertIsNotNone(next) 


    def test_first_then_next(self):
        file_list = ["file1.jpg", "file2.jpg", "file3.jpg", "file4.jpg"]
        seq = Sequencer(SequenceType.ONCE, file_list)  
        next = seq.first_file()
        self.assertEqual(next, "file1.jpg")
        next = seq.next_file()
        self.assertNotEqual(next,"file1.jpg")
