import sys


def evaluate_game(opponents_input: int, your_input: int):
    return ((((your_input - opponents_input) % 3) + 1) % 3) * 3
    # this works since the winning choice has the numerical value of 1 higher than the opponent's modulo 3 shifted by 1
    # so 1 < 2 < 3 < 1
    # so ((your_input - opponents_input) % 3) evaluates to 1 if won, 0 if drawn, 2 if loss
    # + 1) % 3) rotates this to 0 = loss, 1 = draw, 2 = win
    # thereby the result is 0 for loss, 3 for draw and 6 for a win


def evaluate_strategy(input_file_name):
    with open(input_file_name, 'r') as f:
        lines = f.readlines()

    your_score = 0
    for line in lines:
        (opponent_play, your_play) = line.split()
        num_opponent = ord(opponent_play) - ord('A') + 1  # we assign both choices the values 1-3 for r,p,s
        num_you = ord(your_play) - ord('X') + 1
        your_score += num_you + evaluate_game(num_opponent, num_you)

    print('The sum of all your scores is: %d' % your_score)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = "input.txt"
    evaluate_strategy(file_name)
