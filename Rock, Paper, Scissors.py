import random
import time
import sys
Bot = ['Rock','Paper', 'Scissors']
Botpick = ''
print('WELCOME TO ROCK, PAPER, SCISSORSSSS!!!!!!')
time.sleep(1)
A = 0
B = 0
C = int(input('How many rounds do you wish to play to? '))
while True:
    Playerpick = str(input('Choose Rock, Paper or Scissors: '))
    Botpick +=(random.choice(Bot))
    time.sleep(.7)
    print('You chose ' + Playerpick)
    time.sleep(.7)
    print('Bot chose ' + Botpick)
    time.sleep(.7)
    if Botpick == Playerpick: print('Its a Draw')
    elif Botpick == 'Rock' and Playerpick == 'Scissors':
        print('You Lose.')
        A = A + 1
    elif Botpick == 'Paper' and Playerpick == 'Rock':
        print('You Lose.')
        A = A + 1
    elif Botpick == 'Scissors' and Playerpick == 'Paper':
        print('You Lose.')
        A = A + 1
    elif Playerpick == 'Rock' and Botpick == 'Scissors':
        print('You Win!')
        B = B + 1
    elif Playerpick == 'Paper' and Botpick == 'Rock':
        print('You Win!')
        B = B + 1
    elif Playerpick == 'Scissors' and Botpick == 'Paper':
        print('You Win!')
        B = B + 1
    else: print('Input not recongized.')
    
    Botpick = Botpick.replace('R', '')
    Botpick = Botpick.replace('o', '')
    Botpick = Botpick.replace('c', '')
    Botpick = Botpick.replace('k', '')
    Botpick = Botpick.replace('P', '')
    Botpick = Botpick.replace('a', '')
    Botpick = Botpick.replace('p', '')
    Botpick = Botpick.replace('e', '')
    Botpick = Botpick.replace('r', '')
    Botpick = Botpick.replace('S', '')
    Botpick = Botpick.replace('i', '')
    Botpick = Botpick.replace('s', '')
    time.sleep(.5)
    print('Bot Score: ')
    print(A)
    time.sleep(.5)
    print('Player Score: ')
    print(B)
    if A == C:
        print('YOU GET NOTHING YOU LOSE.')
        time.sleep(3)
        break
    elif B == C:
        print('CONGRATULATIONS! YOU WON!')
        time.sleep(3)
        break
    else:
        time.sleep(.5)

