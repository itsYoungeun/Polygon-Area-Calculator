### Build a Polygon Area Calculator Project

In this project you will use object oriented programming to create a <mark>Rectangle</mark> class and a <mark>Square</mark> class. The <mark>Square</mark> class should be a subclass of Rectangle, and inherit its methods and attributes.

## Rectangle class

When a Rectangle object is created, it should be initialized with <mark>width</mark> and <mark>height</mark> attributes. The class should also contain the following methods:

- set_width
- set_height
- get_area: Returns area (width * height)
- get_perimeter: Returns perimeter (2 * width + 2 * height)
- get_diagonal: Returns diagonal ((width ** 2 + height ** 2) ** .5)
- get_picture: Returns a string that represents the shape using lines of '*'. The number of lines should be equal to the height and the number of '*' in each line should be equal to the width. There should be a new line (\n) at the end of each line. If the width or height is larger than 50, this should return the string: 'Too big for picture.'.
- get_amount_inside: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.

Additionally, if an instance of a <mark>Rectangle</mark> is represented as a string, it should look like: <mark>'Rectangle(width=5, height=10)'</mark>.

## Square class

The <mark>Square</mark> class should be a subclass of <mark>Rectangle</mark>. When a <mark>Square</mark> object is created, a single side length is passed in. The <mark>__init__</mark> method should store the side length in both the <mark>width</mark> and <mark>height</mark> attributes from the <mark>Rectangle</mark> class.

The <mark>Square</mark> class should be able to access the <mark>Rectangle</mark> class methods but should also contain a <mark>set_side</mark> method. If an instance of a <mark>Square</mark> is represented as a string, it should look like: <mark>'Square(side=9)'</mark>.

Additionally, the <mark>set_width</mark> and <mark>set_height</mark> methods on the <mark>Square</mark> class should set both the width and height.

## Usage example

Example Code
```
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
That code should return:
```

Example Code
```
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
```