import random
from ascii_art import choice_visual_dict

def visual_ascii(player1, player2):
    if player1 == 'r' and player2 == 'r':
        return choice_visual_dict[0]
    if player1 == 'r' and player2 == 'p':
        return choice_visual_dict[1]
    if player1 == 'r' and player2 == 's':
        return choice_visual_dict[2]
    if player1 == 'p' and player2 == 'r':
        return choice_visual_dict[3]
    if player1 == 'p' and player2 == 'p':
        return choice_visual_dict[4]
    if player1 == 'p' and player2 == 's':
        return choice_visual_dict[5]
    if player1 == 's' and player2 == 'r':
        return choice_visual_dict[6]
    if player1 == 's' and player2 == 'p':
        return choice_visual_dict[7]
    if player1 == 's' and player2 == 's':
        return choice_visual_dict[8]

def is_win(player, opponent):
    """ Return True if player wins following this rule: r > s, s > p, p > r

    Args:
        player (str): Player's choice
        opponent (str): Computer's choice

    Returns:
        [bool]: True if player wins over computer
    """
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player =='p' and opponent == 'r'):
        return True

def play():
    """ Play Rock, Paper, Scissors game. Ask user for choice and compare it with random choice from the computer

    Returns:
        [str]: Winning phrase
    """
    choices = ['r', 'p', 's']
    user = input("\nLet's play Rock, Paper, Scissors! What's your choice? \n'r' for rock, 'p' for paper, or 's' for scissors?: ")
    while user not in choices:
        print('Please select a valid choice.')
        user = input("\nWhat's your choice? \n'r' for rock, 'p' for paper, or 's' for scissors?: ")
    computer = random.choice(choices)  
    print(f'\n{visual_ascii(computer, user)}')  
    if user == computer:
        return "                     It's a tie!\n"
    if is_win(user, computer): 
        return '                     You won!\n' 
    else: 
        return '                     You lost!\n'

print(play())