class Rectangle:
    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise TypeError('Width and height must be greater than 0')
        self.width = width
        self.height = height
    
    def set_width(self, new_width):
        if new_width < 0:
            raise TypeError('Width must be greater than 0')
        self.width = new_width

    def set_height(self, new_height):
        if new_height < 0:
            raise TypeError('Height must be greater than 0')
        self.height = new_height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ""
        for i in range(self.height):
            picture += "*" * self.width + "\n"
        return picture

    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, new_width):
        self.set_side(new_width)

    def set_height(self, new_height):
        self.set_side(new_height)

    def set_side(self, new_side):
        super().set_width(new_side)
        super().set_height(new_side)

    def __str__(self):
        return f'Square(side={self.width})'

rect = Rectangle(10, 4)
sq = Square(4)

print(rect.get_perimeter())
rect.set_width(8)
rect.set_height(4)
print(rect.get_perimeter())
print(rect.get_area())
print(rect.get_diagonal())
print(rect.get_picture())
print(rect.get_amount_inside(sq))

print(rect)
print(sq)