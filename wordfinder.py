"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """
    returns a random word from file of words
    >>> wf = WordFinder("testwords.txt")
    4 words read

    >>> wf.random() in ["Lemur","Dog","Monkey","Fish"]
    True
    """
    def __init__(self,path):
        """Reads file and prints number of words"""
        self.file = open(path,"r")
        self.words = self.strip_list()
        print(f"{len(self.words)} words read")
    
    def strip_list(self):
        """strips each word and inputs them into an interable list"""
        return [word.strip() for word in self.file]
            

    def random(self):
        """Returns a random word"""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """accounts for files with blank lines/# & will return only words
    >>> swf = SpecialWordFinder("specialwords.txt")
    4 words read
    
    >>> swf.random() in ["kale","parsnips","apple","mango"]
    True
    """
    def strip_list(self):
        return [word.strip() for word in self.file if not word.startswith("#") and word.strip()]
        