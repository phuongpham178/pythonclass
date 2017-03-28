1. Write a simple Rectangle class. It should do the following:

Accepts length and width as parameters when creating a new instance
Has a perimeter method that returns the perimeter of the rectangle
Has an area method that returns the area of the rectangle
Don't worry about coordinates or negative values, etc.


class Rectangle:

    def __init__(self, length, width): # this initializes the object with the given parameters
        self.__length = length # assign length
        self.__width = width # assign width

    def set_length(self, length): # this method allows us pass the Rectangle object a value and set the object's length to the given value
        self.__length = length # assign length

    def set_width(self, width): # had 'model' here # same thing, for width
        self.__width = width # assign width

    def get_length(self): # this method does one thing...
        return self.__length # return the Rectangle object's length

    def get_width(self): # and same for width
        return self.__width

    def get_area(self): # this actually does something: multiplies width by height and returns that value
        return self.get_width() * self.get_length() # underscores were wrong

    def get_perimeter(self): # similarly, this adds double the length to double the width and returns that value
        return self.get_width() * 2 + self.get_length() * 2 # underscores were wrong, missing self

def main(): # our main program, which will test our Rectangle class
    length = float(input('Length? ')) # request a length and turn that string into a float
    width = float(input('Width? ')) # request a width and turn that string into a float
    rectangle = Rectangle(length, width) # create a new Rectangle object with the given length and width
    print(rectangle.get_length(), rectangle.get_width()) # print the object's length and width, using the getters
    print(round(rectangle.get_area(), 2)) # round the area to 2 places and print it
    print(round(rectangle.get_perimeter(), 2)) # round the perimeter to 2 places and print it
    rectangle.set_length(22.345) # calls the Rectangle object's length setter and passes it a new value, which will set the object's length to the given value
    rectangle.set_width(15.789) # same for width
    print(round(rectangle.get_area(), 2)) # print the area again to see the new value
    print(round(rectangle.get_perimeter(), 2)) # print the perimeter again to see the new value

main() # call our main method - without this, nothing happens
