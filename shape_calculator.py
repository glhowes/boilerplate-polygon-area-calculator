class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __repr__(self):
        self.string = f"Rectangle(width={self.width}, height={self.height})"
        return self.string
    
    def set_width(self, new_width):
        self.width = new_width
    
    def set_height(self, new_height):
        self.height = new_height
    
    def get_area(self):
        self.area = self.width * self.height
        return self.area

    def get_perimeter(self):
        self.perimeter = (2 * self.width) + (2 * self.height)
        return self.perimeter
    
    def get_diagonal(self):
        self.diagonal = (((self.width ** 2) + (self.height ** 2)) ** .5)
        return self.diagonal
     
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            error = "Too big for picture."
            return error
        else:
            self.row = str((self.width * "*")) + "\n"
            self.picture = self.row * self.height
            return self.picture
    
    def get_amount_inside(self, rectangle):
        self.fit_no = self.get_area() // rectangle.get_area()
        return self.fit_no
    
class Square(Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side

    def __repr__(self):        
        self.sq_string = f"Square(side={self.width})"
        return self.sq_string

    def set_side(self, new_side):
        self.width = new_side
        self.height = new_side

    def set_width(self, new_width):
        self.width = new_width
        self.height = new_width

    def set_height(self, new_height):
        self.width = new_height
        self.height = new_height
      