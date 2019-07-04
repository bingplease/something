
class Node:
    def __init__(self, point1=None, point2=None):
        print(self)
        if point1:
            self.point1 = point1
            self.name1 = point1.__class__.__name__
        if point2:
            self.point2 = point2
            self.name2 = point2.__class__.__name__

f = Node()
g = Node(point1=f)
