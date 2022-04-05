
import math

amount = float(input('\nEnter the amount to begin with : '))

interest = float(input('Enter the interest rate :'))

time = int(input('Emter the duration :'))

final = (amount * math.pow((1 + interest/100),time)) - amount

print('The amount has grown by {:.2f}\n'.format(final))