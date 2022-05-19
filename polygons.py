import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
 
 
class Coord:
    def __init__(self, x1, y1):
        self.point = np.array((x1, y1))
 
    def distance(self, other):
        return sqrt((self.point[0] - other.point[0])**2 + (self.point[1] - other.point[1])**2)
 
 
class Polygon:
    def __init__(self, *args):
      self.points = np.array([point for point in args])
 
    def perimeter(self):
      distances = [p0.distance(p1) for p0, p1 in zip(self.points[1:], self.points[:-1])]
      distances.append(self.points[0].distance(self.points[-1]))
      return sum(distances)

 
    def plot(self):
      fig, ax = plt.subplots()
      points = np.array([coord.point for coord in self.points])
      ax.fill(points.T[0], points.T[1], edgecolor='black', linewidth=3)
      plt.show()

 
 
class Triangle(Polygon):
    def __init__(self, p0, p1, p2):
      super().__init__(p0, p1, p2)
 
    def area(self):
      pass
    


# Complete the .distance method of Coord to find the Cartesian distance between 2 Coords
#	Install pytest and write a test function to create two points and check that the distance between them is correct.
#	Write the .perimeter method of the Polygon by summing the cartesian distances between successive points.
#	Again write a test function to test the distance.
#	Complete the __init_ method for the Triangle subclass by calling the super() command.
#	Write a .area method for the Triangle class that will calculate the area using Heron’s formula.
