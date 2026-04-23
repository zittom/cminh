import math

class Point:

    def __init__(self, x=0, y=1):
        
        self.__x = x
        self.__y = y
    def read(self):
        try:
            line = input().strip().split()
            if len(line) >= 2:
                self.__x = int(line[0])
                self.__y = int(line[1])
        except ValueError:
            print("Dữ liệu nhập vào không hợp lệ!")
    def print(self):
        print(f"({self.__x}, {self.__y})")
    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def distance(self, P=None):
        if P is None:
            #
            return math.sqrt(self.__x**2 + self.__y**2)
        else:
            
            dx = P.getX() - self.__x
            dy = P.getY() - self.__y
            return math.sqrt(dx**2 + dy**2)
        
x, y = map(int, input().split())
p = Point(x, y)
p.print()
print(p.distance())