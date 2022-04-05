import math

horizontal = float(input('\nEnter the initial horizontal position (x): '))
vertical = float(input('Enter initial position (y0): '))
velocity = float(input('Enter the velocity (v): '))
theta = int(input('Enter the initial angle : '))
rad = math.radians(theta)

value = vertical + horizontal*math.tan(rad) - 1/2 *((9.8*horizontal*horizontal)/ (velocity*velocity*math.cos(rad)*math.cos(rad)))

print('The trajectory is {:.2f}\n'.format(value))
