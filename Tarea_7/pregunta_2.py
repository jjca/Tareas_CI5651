# A Python3 program to find convex hull of a set of points. Refer 
# https://www.geeksforgeeks.org/orientation-3-ordered-points/
# for explanation of orientation()

from functools import cmp_to_key

class Point:
	def __init__(self, x = None, y = None):
		self.x = x
		self.y = y

p0 = Point(0, 0)

def nextToTop(S):
	return S[-2]

def distSq(p1, p2):
	return ((p1.x - p2.x) * (p1.x - p2.x) +
			(p1.y - p2.y) * (p1.y - p2.y))

def orientation(p, q, r):
	val = ((q.y - p.y) * (r.x - q.x) -
		(q.x - p.x) * (r.y - q.y))
	if val == 0:
		return 0 # collinear
	elif val > 0:
		return 1 # clock wise
	else:
		return 2 # counterclock wise

def compare(p1, p2):

	# Find orientation
	o = orientation(p0, p1, p2)
	if o == 0:
		if distSq(p0, p2) >= distSq(p0, p1):
			return -1
		else:
			return 1
	else:
		if o == 2:
			return -1
		else:
			return 1

def convexHull(points, n):

	ymin = points[0].y
	min = 0
	for i in range(1, n):
		y = points[i].y

		if ((y < ymin) or
			(ymin == y and points[i].x < points[min].x)):
			ymin = points[i].y
			min = i

	# Place the bottom-most point at first position
	points[0], points[min] = points[min], points[0]

	p0 = points[0]
	points = sorted(points, key=cmp_to_key(compare))

	m = 1 # Initialize size of modified array
	for i in range(1, n):
	
		# Keep removing i while angle of i and i+1 is same
		# with respect to p0
		while ((i < n - 1) and
		(orientation(p0, points[i], points[i + 1]) == 0)):
			i += 1

		points[m] = points[i]
		m += 1 # Update size of modified array

	if m < 3:
		return None

	S = []
	S.append(points[0])
	S.append(points[1])
	S.append(points[2])

	for i in range(3, m):
		while ((len(S) > 1) and
		(orientation(nextToTop(S), S[-1], points[i]) != 2)):
			S.pop()
		S.append(points[i])

	return S

# Driver Code
input_points = [(0, 3), (1, 1), (2, 2), (4, 4),(0, 0), (1, 2), (3, 1), (3, 3)]
#input_points = [(0,3),(2,2),(1,1),(2,1),(3,0),(0,0),(3,3)]

points = []
for point in input_points:
	points.append(Point(point[0], point[1]))
n = len(points)
capas = 0
while n > 2:
	border_points = convexHull(points, n)
	if border_points != None:
		for pt in border_points:
			if pt in points:
				points.remove(pt)
		capas = capas+1			
	else:
		capas = capas+1
		break
	n = len(points)
if n == 1 or n == 2:
	capas+=1
print(capas)