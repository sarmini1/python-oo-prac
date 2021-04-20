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
        self.words = self.word_clean_up(filepath)
        print(f"{len(self.words)} words read")

    def random(self):
        """Returns a random word from the file"""
        
        return choice(self.words)
        
    def word_clean_up(self, filepath):
        """removes new linecharacters from file object"""
        words = list(open(filepath, 'r'))
        return [word[0: len(word) - 1] for word in words]
