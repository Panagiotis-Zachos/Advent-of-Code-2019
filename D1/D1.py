import math
import os

os.chdir('C:\\Users\\Panos\\Google Drive\\ECE\\Python Files\\Advent of Code 2019\\D1\\')
f = open('input.txt', 'r')

total_fuel = 0
for module in f:
    fuel_amount = math.floor(int(module) / 3) - 2
    while fuel_amount > 0:
        total_fuel += fuel_amount
        fuel_amount = math.floor(fuel_amount / 3) - 2
print(total_fuel)

