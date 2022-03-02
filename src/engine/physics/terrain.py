import pygame
import src.engine.physics.physics as physics
import src.engine.physics.normal as normal
import functools
from functools import partial

class Terrain(physics.Object):
    def __init__(self, sprite, scale, x, y, name = "undefinedTerrain", frict = 0.7, edges = None, normalFuns = None):
        physics.Object.__init__(self, sprite, scale, x, y, name, frict)
        self.edges = edges
        self.normalFuns = normalFuns

def is_between(point1, point2, testPoint):
    (x1, y1) = point1
    (x2, y2) = point2
    (x3, y3) = testPoint
    (y1, y2, y3) = (-y1, -y2, -y3) # to allow for typical slope calculations
    if testPoint in [point1, point2]:
        # print("deffo True")
        return True
    if (x2 == x1):
        # print("linearly-like: ", end = "")
        # print((x1 == x3) and (y3 >= min(y1,y2)) and (y3 <= max(y1,y2)))
        return ((x1 == x3) and (y3 >= min(y1,y2)) and (y3 <= max(y1,y2)))
    if (y2 == y1):
        # print("linearly-like: ", end="")
        # print((y1 == y3) and (y3 >= min(y1,y2)) and (y3 <= max(y1,y2)))
        return ((y1 == y3) and (y3 >= min(y1,y2)) and (y3 <= max(y1,y2)))

    m = (y2-y1)/(x2-x1)
    b = y1-(m*x1)
    # print("equation:  ", end = "")

    y = m*x3 + b
    floor = math.floor(y)
    if((x3 == 99) & (y3 == -1)):
        print("({: },{: }) between ({: },{: }) & ({: },{: })".format(x3, y3, x1, y1, x2, y2), end="\t\t")
        print("y = " + str(m) + "x + " + str(b) + " \t->\t (x3,y) = (" + str(x3) + ", " + str((m * x3 + b)) + ")\t\t", end="")

        print("\n{}\t{}\t{}\t{}".format(x3, y, math.floor(y), math.floor(y)+1))
        print("")

    return((floor == y3) or (floor +1 == y3) or (floor - 1 == y3))

def from_polygon(points, scale, color = (0,255,0,255), name = "undefinedPolygon", frict = 0.7):
    xValues = [point[0] for point in points]
    minX = min(xValues); maxX = max(xValues)
    yValues = [point[1] for point in points]
    minY = min(yValues); maxY = max(yValues)
    for point in points:
        point[0] -= minX
        point[1] -= minY
    sprite = pygame.Surface((maxX-minX, maxY-minY), flags=pygame.SRCALPHA)
    pygame.draw.polygon(sprite, color, points)

    outline = []; edges = []
    for point in pygame.mask.from_surface(sprite).outline():
        if point not in outline:
            outline.append(point)
    for i in range(len(points)):
        edges.append(list(filter((partial(is_between, points[i], points[(i+1)%len(points)])), outline)))
    for edge in edges:
        print(edge)
    return Terrain(sprite, scale, minX, minY, name, frict, edges)