import numpy as np
from pprint import pprint

asteroid_map = list(map(str.strip, open('input.txt', 'r').readlines()))

# Part 1

max_vision = 0
for y0 in range(len(asteroid_map)):
    for x0 in range(len(asteroid_map[y0])):
    
        if asteroid_map[y0][x0] == '#': 
            vision = set()

            for y1 in range(len(asteroid_map)):
                for x1 in range(len(asteroid_map[y1])):
                    if y1 == y0 and x1 == x0:
                        continue
                    if asteroid_map[y1][x1] == '#':
                        vision.add(np.arctan2(y0-y1,x0-x1))
            current_vision = len(vision)
            if current_vision > max_vision:
                max_vision = current_vision
                best_coords = (x0, y0)
print('Part1: Coords={}, Number Of Visible Asteroids={}'.format(best_coords, max_vision)) # (26,36) 347

# Part 2

(x0, y0) = best_coords
current_asteroid = 0
asteroid_coords = {}
for y in range(len(asteroid_map)):
    for x in range(len(asteroid_map[y])):
        if y == y0 and x == x0:
            continue
        if asteroid_map[y][x] == '#':
            phi = np.arctan2(y0-y,x0-x)
            if phi not in asteroid_coords:
                asteroid_coords[phi] = [(x,y)]
            else:
                asteroid_coords[phi].append((x,y))

# Re-Order keys so that the first is the closest positive to 0
sorted_keys = sorted(asteroid_coords.keys())
for i in range(len(sorted_keys)):
    if sorted_keys[i] >= 1.56:
        start = i
        break
sorted_keys = sorted_keys[start:] + sorted_keys[:start]

asteroids_destroyed = 0
N_coords = len(sorted_keys)
while asteroids_destroyed < 200:
    coords_destroyed = asteroid_coords[sorted_keys[asteroids_destroyed]].pop()
    asteroids_destroyed += 1

print('Part2: {}'.format(coords_destroyed[0]*100 + coords_destroyed[1]))





