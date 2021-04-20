class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    #start with dunder init function to take in the passed parameter
        #parameters would be self, start
            #inside the function:
                #declare self.start = start
                #declare self.counter_value = start

    #create method called generate that reads the counter_value variable
        #save total_value as self.counter_value + self.start
        #increment counter_value by 1
        #return total_value

    #create method called reset that resets counter
    #back to the initial value

    #creates class instance from a single passed-in parameter
        #each class instance will also be given a counter_value starting at 0
    def __init__(self,start):
        self.start = start
        self.counter_value = 0
    
    #method declares its own variable for the total value, equal to starting value + counter_value
    #increments counter value and returns the total
    def generate(self):
        """Returns current serial number and increments by 1
        """
        total_value = self.counter_value + self.start
        self.counter_value += 1
        return total_value
    
    #resets counter value back to 0
    def reset(self):
        """Resets the serial number generator back to the initial value
        """
        self.counter_value = 0