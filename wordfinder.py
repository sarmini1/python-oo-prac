from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    #__init__
        # pass file path open file function (filepath, r)
        # make list of words from file
        # save length of list as count of words
        # Return "'count' words read"
    
    # def random()
        # use imported choice function to pick a word from the list and return it

    def __init__(self, filepath):
        """Accepts a filepath to a text file containing words"""
        self.file = open(filepath, 'r')
        self.words = list(self.file)
        self.length = len(self.words)
        print(f"{self.length} words read")

    def random(self):
        """Returns a random word from the file"""
        
        word = choice(self.words)
        
        return word[0: len(word) - 1]
