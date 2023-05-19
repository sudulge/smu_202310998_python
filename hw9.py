class Point:

    def __init__(self, x = 0 , y = 0):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")
    
    def set(self, x, y):
        self.x = x 
        self.y = y
        return True
    
    def get(self):
        return (self.x, self.y)


class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        self.lt = Point(x1, y1)
        self.rb = Point(x2, y2)
        # 항상 lt가 rb보다 왼쪽 상단에 있다고 가정
        # x1 < x2, y1 < y2  

    def show(self):
        self.lt.show()
        self.rb.show()
    
    def getWidth(self):
        return self.rb.x - self.lt.x
    
    def getHeight(self):
        return self.rb.y - self.lt.y
    
    def getArea(self):
        return self.getWidth() * self.getHeight()
    
    def getPerimeter(self):
        return (self.getWidth() + self.getHeight()) * 2
    
        

# 주 프로그램부
r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()
r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')