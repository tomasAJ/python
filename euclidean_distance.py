"""EUCLIDIAN DISTANCE BETWEEN (2,3) AND (10,8)"""

# https://en.wikipedia.org/wiki/Euclidean_distance#:~:text=In%20mathematics%2C%20the%20Euclidean%20distance,being%20called%20the%20Pythagorean%20distance.

import math


def distance_absolute_difference(point_p, point_q):
    """ONE DIMENSION"""
    distance = abs(point_p-point_q)  # d(p,q)=|p-q|
    return distance


def distance_another_way(point_p, point_q):
    """ONE DIMENSION"""
    distance = math.sqrt(math.pow((point_p-point_q), 2))
    return distance


def distance_cartesian_coordinates(point_p1, point_p2, point_q1, point_q2):
    """TWO DIMENSION"""
    distance = math.sqrt(math.pow((point_q1-point_p1), 2) +
                         math.pow((point_q2-point_p2), 2))
    return distance


print(distance_absolute_difference(1, 10))
print(distance_another_way(1, 10)
      )
print(distance_cartesian_coordinates(2, 3, 10, 8)
      )


x1, y1 = 2, 3
x2, y2 = 10, 8

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(distance)
