import random

hand = ['rock', 'paper', 'scissors']
player_name = input('Enter name: ')

while True:
    player = input('Select action (rock, paper, scissors): ')
    if player.lower() not in hand:
        print('Invalid action.')
        continue
    computer = random.choice(hand)

    print(f'{player_name} puts {player.lower()}')
    print(f'Computer puts {computer}')

    if player.lower() == computer:
        print("It's tie! Again!")
        continue

    if player.lower() == 'paper':
        if computer == 'rock':
            print(f'{player_name} wins!')
        else:
            print(f'Computer wins!')

    if player.lower() == 'rock':
        if computer == 'scissors':
            print(f'{player_name} wins!')
        else:
            print(f'Computer wins!')

    if player.lower == 'scissors':
        if computer == 'paper':
            print(f'{player_name} wins!')
        else:
            print(f'Computer wins!')

    x = input('Wanna play again (y/n)? ')
    if x.lower() == 'y':
        continue
    else:
        break
