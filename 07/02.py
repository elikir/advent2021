import sys

def triangle_sum(x, y):
   n = abs(x - y)
   rangeval = int(n * (n+1) / 2)
   return rangeval


def fuel_to_move_to_position(position_to_move_to, positions):
    total_fuel = sum([triangle_sum(x, position_to_move_to) for x in positions])
    return total_fuel


with open('01.txt') as f:
    crabs = [int(x) for x in f.read().split(",")]
    min_fuel = sys.maxsize
    for x in range(min(crabs), max(crabs) + 1):
        fuel = fuel_to_move_to_position(x, crabs)
        if fuel < min_fuel:
            min_fuel = fuel
    print(min_fuel)
