import math

def lerp(a, b, t):
	return a * (1-t) + (b*t)

class Point():
	def __init__(self, x, y, canvas=None):
		self._canvas = canvas
		self._x = x
		self._y = y
	
	def __str__(self):
		return str(self._x) + ", " + str(self._y)

	# Checks if the point is within a polygon
	# Inspired by the pnpoly algorithm by W. Randolph Franklin
	def intersects_polygon(self, points):
		lenpoints = len(points)
		intersects = False
		for i in range(lenpoints):
			j = (i+lenpoints-1)%lenpoints
			pi, pj = points[i], points[j]
			if( ((pi.get_y() > self._y) != (pj.get_y() > self._y)) and
			(self._x < (pj.get_x()-pi.get_x()) * (self._y-pi.get_y())/
			(pj.get_y()-pi.get_y()) + pi.get_x())):
				intersects=not intersects
		return intersects

	# Return a point that is linearly interpolated t percent from self to other
	def lerp(self, other, t):
		return Point(lerp(self._x, other.get_x(), t), lerp(self._y, other.get_y(), t))

	# Returns the magnitude from self to other
	def magnitude(self, other):
		return math.sqrt((other.get_x()-self._x)**2+(other.get_y()-self._y)**2)
		
	def get_x(self):
		return self._x
		
	def get_y(self):
		return self._y
