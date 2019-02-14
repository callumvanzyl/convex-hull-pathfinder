import math
import random
import time

from point import Point

# Bruteforce a convex hull
# Inspired by Professor Xia Hong's lecture notes on D&C
def compute_convex_hull(points):
        points = sort_points_xcoord(points)
        lower = do_lower_hull(points)
        upper = do_upper_hull(points)
        return(lower[:-1] + upper[:-1]) # Clip the last point from the lower and upper hull

# Calculates the cross product of o, a, and b.
def cross(o, a, b):
        return (a.get_x() - o.get_x()) * (b.get_y() - o.get_y()) - (a.get_y() - o.get_y()) * (b.get_x() - o.get_x())

# Creates a convex hull from a series of points
# This is done by recursively splitting, bruteforcing, and merging smaller hulls
# Inspired by Professor Xia Hong's lecture notes on D&C
def dc_hull(points):
        lenpoints = len(points)
        if (lenpoints <= 6): # Bruteforce a hull if it is small enough
                return compute_convex_hull(points)
        else:
                left_points = points[:lenpoints//2]
                left_hull = dc_hull(left_points) 

                right_points =  points[lenpoints//2:]
                right_hull = dc_hull(right_points)

                return merge(left_hull, right_hull) # Merge the left and right hull

# Merge two convex hulls
# Inspired by a code snippet from https://www.geeksforgeeks.org/tangents-two-convex-polygons/
def merge(p1, p2):
        p1 = sort_points_ccw(p1)
        p2 = sort_points_ccw(p2)

        n1 = len(p1)
        n2 = len(p2)

        ia = 0
        for i in range(0, n1):
                if (p1[i].get_x() > p1[ia].get_x()):
                        ia = i

        ib = 0
        for i in range(0, n2):
                if (p2[i].get_x() < p2[ib].get_x()):
                        ib = i

        inda = ia; indb = ib
        done = False
        while (not done):
                done = True
                while (cross(p2[indb], p1[inda], p1[(inda+1)%n1]) >= 0):
                        inda = (inda+1)%n1
                while (cross(p1[inda], p2[indb], p2[(n2+indb-1)%n2]) <= 0):
                        indb = (n2+indb-1)%n2
                        done = False
        uppera = inda; upperb = indb

        inda = ia; indb = ib
        done = False
        while (not done):
                done = True
                while (cross(p1[inda], p2[indb], p2[(indb+1)%n2]) >= 0):
                        indb = (indb+1)%n2
                while (cross(p2[indb], p1[inda], p1[(n1+inda-1)%n1]) <= 0):
                        inda = (n1+inda-1)%n1
                        done = False
        lowera = inda; lowerb = indb

        temp_points = []

        ind = uppera
        temp_points.append(p1[uppera])
        while (ind != lowera):
                ind = (ind+1)%n1
                temp_points.append(p1[ind])

        ind = lowerb
        temp_points.append(p2[lowerb])
        while (ind != upperb):
                ind = (ind+1)%n2
                temp_points.append(p2[ind])

        return (temp_points)

# Creates the lower half of a convex hull
# Inspired by Professor Xia Hong's lecture notes on D&C
def do_lower_hull(points):
        temp_points = []
        for p in points:
                while (len(temp_points) >= 2 and cross(temp_points[-2], temp_points[-1], p) <= 0):
                        temp_points.pop()
                temp_points.append(p)
        return temp_points

# Creates the upper half of a convex hull
# Inspired by Professor Xia Hong's lecture notes on D&C
def do_upper_hull(points):
        temp_points = []
        for p in reversed(points):
                while len(temp_points) >= 2 and cross(temp_points[-2], temp_points[-1], p) <= 0:
                        temp_points.pop()
                temp_points.append(p)
        return temp_points

# Sorts a list of points counter-clockwise
def sort_points_ccw(points):
        lenpoints = len(points)
        centre = Point(sum(p.get_x() for p in points)/lenpoints, sum(p.get_y() for p in points)/lenpoints)
        points.sort(key=lambda p: (math.atan2(p.get_x()-centre.get_x(), p.get_y()-centre.get_y()) + 2*math.pi) % (2*math.pi))
        return points

# Sorts a list of points by their x coordinate
def sort_points_xcoord(points):
        lenpoints = len(points)
        for i in range(1, lenpoints):
                point = points[i]
                j = i-1
                while j >= 0 and point.get_x() < points[j].get_x():
                        points[j+1] = points[j]
                        j -= 1
                points[j+1] = point
        return points


class ConvexHull():
        def __init__(self):
                self._computed_points = []
                self._points = []

                self._i = 0

        def add_point(self, point):
                self._points.append(point)

        def compute(self):
                self._computed_points = sort_points_xcoord(self._points)
                self._computed_points= dc_hull(self._computed_points)

        def get_computed_points(self):
                return self._computed_points

        def get_points(self):
                return self._points

        def set_points(self, points):
                self._points = points
