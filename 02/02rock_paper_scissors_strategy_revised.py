import sys


def evaluate_strategy(input_file_name):
    with open(input_file_name, 'r') as f:
        lines = f.readlines()

    your_score = 0
    for line in lines:
        (opponent_play, intended_goal) = line.split()
        num_opponent = ord(opponent_play) - ord('A') + 1
        num_intended_goal = ord(intended_goal) - ord('Y')  # -1 if loss, 0 if draw, 1 if win
        num_you = ((num_opponent - 1 + num_intended_goal) % 3) + 1  # assigns the numerical value of the intended choice
        your_score += num_you + (num_intended_goal + 1) * 3  # result is already known, so no evaluation necessary

    print('The sum of all your scores is: %d' % your_score)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = "input.txt"
    evaluate_strategy(file_name)
