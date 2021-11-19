import random

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
    print(f'\n{computer} vs {user}!')  
    if user == computer:
        return "It's a tie!\n"
    if is_win(user, computer): 
        return 'You won!\n' 
    else: 
        return 'You lost!\n'
    
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

print(play())