class Rectangle:
    def __init__(self, w, h):
        if w <= 0 or h <= 0:
            self.width = 0
            self.height = 0
        else:
            self.width = w
            self.height = h

    def print(self):
        if self.width == 0 or self.height == 0:
            print("Empty rectangle")
        else:
            for _ in range(self.height):
                print("X" * self.width)


# Example usage:
rect1 = Rectangle(5, 3)
rect1.print()
# Output:
# XXXXX
# XXXXX
# XXXXX

rect2 = Rectangle(0, 4)
rect2.print()
# Output:
# Empty rectangle
