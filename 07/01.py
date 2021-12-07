

def fuel_to_move_to_position(position_to_move_to, positions):
    total_fuel = sum([abs(position_to_move_to - x) for x in positions])
    return total_fuel


with open('01.txt') as f:
    crabs = [int(x) for x in f.read().split(",")]
    min_fuel = 9999999
    for x in range(min(crabs), max(crabs) + 1):
        fuel = fuel_to_move_to_position(x, crabs)
        if fuel < min_fuel:
            min_fuel = fuel
    print(min_fuel)
