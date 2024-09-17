class Rectangle():
    """
    Represents the the Rectangle
    """

    def __init__(self, length:int, width:int) -> None:
        self.length = length
        self.width = width

    def __iter__(self):
        # Reset the iter_index for each instance
        self._iter_index = 0
        return self
    
    def __next__(self):
        if self._iter_index == 0:
            self._iter_index += 1
            return {'length': self.length}
        elif self._iter_index == 1:
            self._iter_index += 1
            return {'width': self.width}
        else:
            raise StopIteration

# Create an instance of Rectangle class
rectangle = Rectangle(10, 20)

# Iterate through the instance
for item in rectangle:
    print(item)

# Output:
# {'length': 10}
# {'width': 20}
