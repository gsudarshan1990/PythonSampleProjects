import math
class Line():
    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2

    def distance_between_points(self):
        x1,y1=self.coor1
        x2,y2=self.coor2
        distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
        return distance

    def slope_of_line(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        slope=(y2-y1)/(x2-x1)
        return slope


coordiante1=(3,2)
coordinate2=(8,10)

li=Line(coordiante1,coordinate2)
print(li.distance_between_points())
print(li.slope_of_line())
