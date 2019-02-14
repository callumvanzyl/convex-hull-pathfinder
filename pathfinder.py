from convex_hull import ConvexHull
from point import Point

# Checks if a line intersects a polygon
def get_polygons_intersecting_line(polygons, p1, p2):
    intersecting = []
    t = 0
    while t < 1:
        point = p1.lerp(p2, t) # Get the point t% from point a to b
        for p in polygons: # For each polygon...
            if point.intersects_polygon(p): # If point on line intersects polygon...
                polygons.remove(p) # Don't recheck the same polygon multiple times
                intersecting.append(p)
        t+=0.05
    return intersecting

# Find a path through a set of polygons, passing through each waypoint once
def find_path(polygons, waypoints):
    path = []
    temp_waypoints = waypoints.copy()

    for i in range(0, len(temp_waypoints)-1):
        temp_polygons = polygons.copy()
        
        p1 = temp_waypoints[i]
        p2 = temp_waypoints[i+1]
        
        intersecting = get_polygons_intersecting_line(temp_polygons, p1, p2) # Find any polygons between the waypoints

        if (len(intersecting)>0): # If there are intersecting polygons...
            all_points = []
            all_points.append(p1)
            all_points.append(p2)

            for polygon in intersecting:
                for point in polygon:
                    all_points.append(point)

            ch = ConvexHull()
            ch.set_points(all_points)
            ch.compute()
            cp = ch.get_computed_points()
            a = cp.index(p1)
            b = cp.index(p2)

            points = None
            if (a<b):
                points = cp[a:b+1]
            else:
                a, b = b, a
                points = cp[a:b+1]
                points.reverse()        

            path.extend(points)
        else: # If there are no intersecting polygons...
            path.append(p1)
            path.append(p2)

    return path


        