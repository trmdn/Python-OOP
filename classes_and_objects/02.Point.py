class Point():
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    
    def set_x(self, nex_x):
        self.x = int(nex_x)
    
    def set_y(self, next_y):
        self.y = int(next_y)
    
    def __str__(self):
        return f"The point has coordinates ({self.x},{self.y})"
    
p = Point(2, 4)
print(p)
p.set_x(3)
p.set_y(5)
print(p)
