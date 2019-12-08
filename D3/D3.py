
from time import time

t0 = time()
f = open(r'C:\Users\Panos\Google Drive\ECE\Python Files\Advent of Code 2019\D3\input.txt','r')
line = f.readline().strip().split(',')
w1_coords = []
pos = [0,0]

for turn in line:
    direction, length = turn[0], turn[1:]
    if direction == 'R':
        for i in range(1, int(length)+1):
            temp_pos = (pos[0]+i, pos[1])
            w1_coords.append(temp_pos)
    elif direction == 'L':
        for i in range(1, int(length)+1):
            temp_pos = (pos[0]-i, pos[1])
            w1_coords.append(temp_pos)     
    
    elif direction == 'U':
        for i in range(1, int(length)+1):
            temp_pos = (pos[0], pos[1]+i)
            w1_coords.append(temp_pos)

    elif direction == 'D':
        for i in range(1, int(length)+1):
            temp_pos = (pos[0], pos[1]-i)
            w1_coords.append(temp_pos)
    pos[:] = temp_pos[:]

line = f.readline().strip().split(',')
w2_coords = []
pos = [0,0]
for turn in line:
    direction, length = turn[0], turn[1:]
    if direction == 'R':
        for i in range(1, int(length)+1):
            temp_pos = (pos[0]+i, pos[1])
            w2_coords.append(temp_pos)
    elif direction == 'L':
        for i in range(1, int(length)+1):
            temp_pos = (pos[0]-i, pos[1])
            w2_coords.append(temp_pos)     
    
    elif direction == 'U':
        for i in range(1, int(length)+1):
            temp_pos = (pos[0], pos[1]+i)
            w2_coords.append(temp_pos)

    elif direction == 'D':
        for i in range(1, int(length)+1):
            temp_pos = (pos[0], pos[1]-i)
            w2_coords.append(temp_pos)

    pos[:] = temp_pos[:]

# Part 1
distances = []
for cross in set(w1_coords).intersection(set(w2_coords)):
    distances.append(abs(cross[0])+abs(cross[1]))
distances.sort()
print(distances[0])

# Part 2
intersections = set(w1_coords).intersection(set(w2_coords))
distances = []
for inter in intersections:
    steps1 = 0
    while w1_coords[steps1] != inter:
        steps1 += 1
    steps2 = 0
    while w2_coords[steps2] != inter:
        steps2 += 1
    distances.append(steps1 + steps2 + 2)
distances.sort()
print(distances[0])
print(time() - t0)