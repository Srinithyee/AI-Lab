import math
import random


class point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def dist(self, p2) -> int:
        dx = self.x - p2.x
        dy = self.y - p2.y
        return math.sqrt(math.pow(dx,2) + math.pow(dy, 2))
    
    @staticmethod
    def genrand(limx: tuple, limy: tuple):
        limx1, limx2 = limx
        limy1, limy2 = limy
        x = random.randint(limx1, limx2)
        y = random.randint(limy1, limy2)
        return point(x, y)


class polygon:
    def __init__(self, points):
        self.points = points

    def inside(self, x: int, y: int) -> bool:
        vals = []
        for i in range(len(points) - 1):
            x1, y1 = self.points[i].x, self.points[i].y
            x2, y2 = self.points[i+1].x, self.points[i+1].y

            A = -(y2-y1)
            B = x2 - x1
            C = -(A*x1 + B*y1)

            vals.append(A*x + B*y + C)
        
        x1, y1 = self.points[len(points) - 1].x, self.points[len(points) - 1].y
        x2, y2 = self.points[0].x, self.points[0].y
        A = -(y2-y1)
        B = x2 - x1
        C = -(A*x1 + B*y1)
        vals.append(A*x + B*y + C)
        
        t1 = all(d>=0 for d in vals)
        t2 = all(d<=0 for d in vals)
        return t1 or t2


class grid:
    def __init__(self, m: int, n: int, polygons, start: point, goal: point):
        self.actions = ["u", "d", "l", "r"]
        self.m = m
        self.n = n
        self.polygons = polygons
        self.current = start
        self.goal = goal
    
    def isGoal(self) -> bool:
        return self.start == self.goal
    
    def get_actions(self):
        admissable_actions = []
        for action in self.actions:
            x, y = self.current
            admissable = True
            if action == "u":
                y += 1
            if action == "d":
                y -= 1
            if action == "l":
                x -= 1
            if action == "r":
                x += 1
            if(x < 0 or x >= self.n or y < 0 or y >= self.m):
                continue
                
            for polygon in self.polygons:
                if polygon.inside(x, y) == True:
                    admissable = False
                    break
            
            print(x, y, admissable)
            if admissable:
                admissable_actions.append(action)
        return admissable_actions
    

