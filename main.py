import math, random

from tkinter import Canvas, Tk

from convex_hull import ConvexHull
from pathfinder import find_path
from point import Point

all_hulls = []
all_polygons = []
all_waypoints = []

cp = []
mouse_position = None

# Draw a dot on a canvas
def draw_dot(canvas, color, size, point):
	canvas.create_oval(point.get_x()-size/2, point.get_y()-size/2, point.get_x()+size/2, point.get_y()+size/2, fill=color, outline="")

# Draw a line from the given points
def draw_line(canvas, p1, p2):
	canvas.create_line(p1.get_x(), p1.get_y(), p2.get_x(), p2.get_y(), fill="black", width=16)

# Draw a polygon using a list of points
def draw_polygon(canvas, points):
        coords = []
        for p in points:
                coords.append(p.get_x())
                coords.append(p.get_y())
        colours = ["blue", "green", "orange", "red", "violet", "yellow"]
        canvas.create_polygon(coords, fill=random.choice(colours))

# Fires when the user left-clicks the mouse
def on_left_click(event):
	global cp, mouse_position
	cp.append(mouse_position) # Add the mouse position the the current polygon
	draw_dot(event.widget, "red", 8, mouse_position)

# Fires when the user right-clicks the mouse
def on_right_click(event):
	global all_polygons, cp
	if len(cp) >= 3: # A polygon cannot be created from less than three points
		draw_polygon(event.widget, cp)
		all_polygons.append(cp) # Add the current polygon to the list of all polygons
		cp = [] # Reset the polygon

# Fires when the user moves the mouse
def on_mouse_moved(event):
	global mouse_position
	mouse_position = Point(event.x, event.y, event.widget)

# Fires when the user presses the e key
def do_pathfinding(event):
	global all_polygons, all_waypoints
	path = find_path(all_polygons, all_waypoints)
	lenpath = len(path)
	for i in range(0, lenpath-1): # Draw the path
		p1 = path[i]
		p2 = path[i+1] # Next points in path
		draw_line(event.widget, p1, p2)

# Fires when the user presses the q key
def place_waypoint(event):
	global all_waypoints, mouse_position
	draw_dot(event.widget, "black", 16, mouse_position)
	all_waypoints.append(mouse_position)

def main():
	gui = Tk()
	gui.title("D&C Convex Hull")

	canvas = Canvas(gui)
	canvas.focus_set()

	canvas.bind("<Button-1>", on_left_click)
	canvas.bind("<Button-3>", on_right_click)
	canvas.bind("<Motion>", on_mouse_moved)
	canvas.bind("e", do_pathfinding)
	canvas.bind("q", place_waypoint)
	canvas.pack(expand=True, fill="both")

	gui.mainloop()

if __name__ == "__main__":
	main()
