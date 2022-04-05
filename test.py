
import random
print('\n\nWe are playing Rock(1) Paper(2) Scissor(3)')
while True:
                # With user input.
    choice1 =  int(input('\nPlayer 1 choice : '))
    if choice1 <= 0 or choice1 > 3:
        print('Wrong choice')
        break                                     
    choice2 = int(input('Player 2 choice : '))
    if choice2 <= 0 or choice2 > 3:
        print('Wrong choice')
        break
                # Random play.
    '''choice1 = random.randint(1,3)           
    choice2 = random.randint(1,3)'''

    if choice1 == choice2:
        print("It's a Draw.")
    elif (choice1 == 1 and choice2 == 2) or (choice1 == 2 and choice2 == 3) or (choice1 == 3 and choice2 == 1):
        print('Player 2 wins.')
    else:
        print('Player 1 wins.')

    c = input('\nDo you want to play more : (Yes/y), (No/n) : ')
    if c == 'n':
        break
    elif c == 'y':
        continue
    else:
        print('Wrong selection')
        break

print()