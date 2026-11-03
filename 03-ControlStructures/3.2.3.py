###
# The car has three driving modes: Auto (A), Manual (M) and Eco (E).
# In each of these three modes, the average fuel consumption in liters
# per 100 km is 7, 9 and 6 respectively. Write a program that calculates
# total fuel consumption for a given distance in km and a given
# driving mode.
#
driving_mode = input('Enter driving mode (A/M/E):')
distance = int(input('Enter distance in km'))

if driving_mode == 'A':
    fuel_consumption = 7 # liters per 100km
elif driving_mode == 'M':
    fuel_consumption = 9 # liters per 100km
elif driving_mode == 'E':
    fuel_consumption = 6 # liters per 100km

total_consumption = (fuel_consumption * distance) / 100
print('Total fuel consumption over a distance of {} km in driving mode {} is {} liters'.format(distance, driving_mode, total_consumption))
