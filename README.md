# convex-hull-pathfinder
A program to generate a set of convex hulls from a list of arbitrary polygons, then find a path around them.
Convex hulls are found in a divide-and-conquer manner and are bruteforced using [Andrew’s montone chain convex hull algorithm](https://en.wikibooks.org/wiki/Algorithm_Implementation/Geometry/Convex_hull/Monotone_chain). Paths are found using rudimentary raycasting.

## Controls
Key | Function
---: | ---
**Left mouse** | Add point to current polygon
**Right mouse** | Confirm current polygon
**Q** | Place waypoint
**E** | Find path between waypoints

## Screenshots
[screenshotA]: https://i.imgur.com/4VsutKm.png
![](https://i.imgur.com/4VsutKm.png)
![](https://i.imgur.com/QUPZ87A.png)