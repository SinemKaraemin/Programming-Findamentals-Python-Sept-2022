import sys

print('Choose rock, paper or scissors')
player_1 = input('player_1: ')
player_2 = input('player_2: ')
winner = ''

if player_1 == 'rock' and player_2 == 'scissors':
    winner += player_1
elif player_1 == 'rock' and player_2 == 'paper':
    winner += player_1
elif player_1 == 'scissors' and player_2 == 'rock':
    winner += player_2
elif player_1 == 'scissors' and player_2 == 'paper':
    winner += player_1
elif player_1 == 'paper' and player_2 == 'rock':
    winner += player_2
elif player_1 == 'paper' and player_2 == 'scissors':
    winner += player_2
elif player_1 == player_2:
    print('draw')
    sys.exit()

if winner == 'player_1':
    print('The winner is player_1')
else:
    print('The winner is player_2')
