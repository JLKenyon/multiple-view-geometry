
'''
In Multiple View Geometry, section 2.3.3, page 30-31, we learn:

A conic can be uniquely defined by 5 points.

This is regardless of any sort of "order" or other structure, given 5 
independent points we can make a conic as surely as three points make
a triangle.

I wanted to test this, so this is my quick and dirty approach.

Here the user clicks out 5 points at random in the window provided.
Each new click will remove the oldest point, and add the new point.

With the 5 points, we create a 5x6 matrix, and find the null space. This
null space is the 6 constants, [a,b,c,d,e,f] which fill out the equation
ax**2 + bxy + cy**2 + dx + ey + f = 0.

Drawing the lines is a bit tricky, and I'm lazy, so what I did as a quick
and dirty solution was to pick a bunch of random points, and then do a
random walk hill climb to move each random point closer to the curve.

This is easy enough by just plugging the random point into the equation
above, and then add +/- 5 pixels to each of the coordinates in that random
point, and keep which ever one has a result which is closer to the ideal value
of zero. Do that like a bunch of times, and the random point should be pretty
close to being on the conic line.
'''

import sys, pygame
import numpy as np
from scipy.linalg import null_space
import random

pygame.init()

size = width, height = 800, 600
black = 0, 0, 0

pixel_rad = 2

screen = pygame.display.set_mode(size)


points = []
curve_points = []


def build_conic_vector(pts):
    return np.array([ \
    [pts[0][0]**2, pts[0][0] * pts[0][1], pts[0][1]**2, pts[0][0], pts[0][1], 1], \
    [pts[1][0]**2, pts[1][0] * pts[1][1], pts[1][1]**2, pts[1][0], pts[1][1], 1], \
    [pts[2][0]**2, pts[2][0] * pts[2][1], pts[2][1]**2, pts[2][0], pts[2][1], 1], \
    [pts[3][0]**2, pts[3][0] * pts[3][1], pts[3][1]**2, pts[3][0], pts[3][1], 1], \
    [pts[4][0]**2, pts[4][0] * pts[4][1], pts[4][1]**2, pts[4][0], pts[4][1], 1]])


def conic_eval(pt, conic):
    return conic[0] * pt[0] * pt[0] + conic[1] * pt[0] * pt[1] + conic[2] * pt[1] * pt[1] + conic[3] * pt[0] + conic[4] * pt[1] + conic[5]

def hill_climb( pt, conic):
    initial_error = conic_eval(pt, conic)
    for num in range(500):
        new_pt = (pt[0] + random.randrange(-5, 5), pt[1] + random.randrange(-5, 5))
        new_error = conic_eval(new_pt, conic)
        if new_error**2 < initial_error**2:
            pt = new_pt
            initial_error = new_error

    return (pt, initial_error)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            points.append( (x, y) )
            if len(points) > 5:
                points = points[1:6]
            if len(points) == 5:
                A = build_conic_vector(points)
                ns = null_space(A)
                curve_points = []
                errors = []
                for n in range(100):
                    rx = float(random.randrange(0, width))
                    ry = float(random.randrange(0, height))
                    (pt, error) = hill_climb( (rx, ry), ns)
                    curve_points.append( pt )
                    errors.append(error)


    screen.fill(black)
    pixel_rad = 2
    for pt in curve_points:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(pt[0] - pixel_rad, pt[1] - pixel_rad, 2 * pixel_rad, 2 * pixel_rad))
    pixel_rad = 4
    for pt in points:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(pt[0] - pixel_rad, pt[1] - pixel_rad, 2 * pixel_rad, 2 * pixel_rad))
        
    pygame.display.flip()

