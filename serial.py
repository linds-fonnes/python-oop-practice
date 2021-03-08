"""Python serial number generator."""

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
    def __init__(self,start=100):
        #starts serial generator
        self.start = start
        self.next = start + 1

    def __repr__(self):
        #returns representation of Serial Generator
        return(f"<Serial Generator start={self.start} next={self.next}>")

    def generate(self):
        #returns start number incremented by 1 each time
        self.next += 1
        return self.next - 1
    def reset(self):
        #resets count back to start value
        self.next = self.start
