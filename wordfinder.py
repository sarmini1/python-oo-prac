from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    #__init__ (self,filepath)
        # runs word_clean_up method and saves result to words variable
        # Return "'count' words read"
    
    # def random(self)
        # use imported choice function to pick a word from the list and return it
    
    # def word_clean_up(self,filepath)
        #returns new list removing end line characters from file object words

    def __init__(self, filepath):
        """Accepts a filepath to a text file containing words"""
        self.words = self.word_clean_up(filepath)
        print(f"{len(self.words)} words read")

    def random(self):
        """Returns a random word from the file"""
        return choice(self.words)
        
    def word_clean_up(self, filepath):
        """removes new line characters from words"""
        return [word[0: len(word) - 1] for word in open(filepath, 'r')]

#class RandomWordFinder(WordFinder):

    #def word_clean_up(self,filepath):
        #return list comprehension filtering out lines that
        # start with hashtags or spaces


class RandomWordFinder(WordFinder):
    """Finds valid words from file"""
    def word_clean_up(self, filepath):
        """ Removes comments and blank spaces, returns filtered list of words """
        return [word for word in super().word_clean_up(filepath)
                if not word.startswith("#") and not word == ""]
