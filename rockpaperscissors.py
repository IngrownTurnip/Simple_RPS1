from random import randint

def rps():
    options = ('rock', 'paper', 'scissors', 'quit')
    player_choice = 'yes'
    player_score = []
    computer_score = []
    while player_choice != 'quit':
        rand_choice = randint(0, 2)
        computer_choice = options[rand_choice]
        player_choice = input('Choose rock, paper, scissors, or quit: ')
        if player_choice == 'rock' and computer_choice == 'scissors':
            player_score.append(1)
            total_player_score = sum(player_score)
            total_computer_score = sum(computer_score)
            print('\nRock beats Scissors! Player Wins!')
            print(f'Player score: {total_player_score} \nComputer score: {total_computer_score}\n')
        elif player_choice == 'paper' and computer_choice == 'rock':
            player_score.append(1)
            total_player_score = sum(player_score)
            total_computer_score = sum(computer_score)
            print('\nPaper beats Rock! Player Wins!')
            print(f'Player score: {total_player_score} \nComputer score: {total_computer_score}\n')
        elif player_choice == 'scissors' and computer_choice == 'paper':
            player_score.append(1)
            total_player_score = sum(player_score)
            total_computer_score = sum(computer_score)
            print('\nScissors beat Paper! Player Wins!')
            print(f'Player score: {total_player_score} \nComputer score: {total_computer_score}\n')
        elif player_choice == computer_choice:
            total_player_score = sum(player_score)
            total_computer_score = sum(computer_score)
            print(f'\nComputer chose {computer_choice}')
            print('Tie!')
            print(f'Player score: {total_player_score} \nComputer score: {total_computer_score}')
        elif player_choice not in options:
            print('\n...funny\n')
        else:
            computer_score.append(1)
            total_player_score = sum(player_score)
            total_computer_score = sum(computer_score)
            print(f'\n{computer_choice} beats {player_choice}')
            print('Computer wins')
            print(f'Player score: {total_player_score} \nComputer score: {total_computer_score}\n')


rps()
