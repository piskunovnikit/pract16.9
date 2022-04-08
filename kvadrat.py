class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    #def getWidth(self):
    #    return self.width
#
    #def getHeight(self):
     #   return self.height
    def getArea(self):
        return self.a * self.b

class sqare:
    def __init__(self, a):
        self.a = a
    def getAreaSqare(self):
        return self.a ** 2


class circle:
    def __init__(self,r):
        self.r = r
    def getAreaCircle(self):
        return self.r ** 2 * 3.14

