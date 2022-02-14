player_1, player_2 = input().split(', ')
matrix_dimensions = 7
score_and_number_rounds = {player_1: [501, 0], player_2: [501, 0]}
matrix = []

for i in range(matrix_dimensions):
    matrix.append(input().split())


def select_player(number_rounds, player1, player2):
    return player1 if number_rounds % 2 != 0 else player2


number_of_rounds = 0
while True:
    row, col = [int(el) for el in eval(input())]
    number_of_rounds += 1
    player = select_player(number_of_rounds, player_1, player_2)
    current_throw = matrix[row][col]
    first_digit = int(matrix[row][0])
    second_digit = int(matrix[row][-1])
    third_digit = int(matrix[0][col])
    fourth_digit = int(matrix[-1][col])
    sum_4_nums = first_digit + second_digit + third_digit + fourth_digit
    if 0 > row > matrix_dimensions - 1 or 0 > col > matrix_dimensions - 1:
        continue
    else:
        score_and_number_rounds[player][1] += 1
        if current_throw.isdigit():
            score_and_number_rounds[player][0] -= int(current_throw)

        elif current_throw == "D":
            score_and_number_rounds[player][0] -= sum_4_nums * 2
        elif current_throw == "T":
            score_and_number_rounds[player][0] -= sum_4_nums * 3
        elif current_throw == "B":
            print(f'{player} won the game with {number_of_rounds} throws!')
            break
        if score_and_number_rounds[player][0] <= 0:
            print(f'{player} won the game with {score_and_number_rounds[player][1]} throws!')
            break
