class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def print_rectangle(self):
        print('w: ', self.w)
        print('h ', self.h)
        print('area: ', self.w * self.h)
        print('perimeter: ', (self.w + self.h)*2)


r = Rectangle(w=4, h=6)
r.print_rectangle()

