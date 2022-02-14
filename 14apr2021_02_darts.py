player_1, player_2 = input().split(', ')
matrix_dimensions = 7
score = {player_1: 501, player_2: 501}
player_2_score = 501
matrix = []

for i in range(matrix_dimensions):
    matrix.append(input().split())


def select_player(number_rounds, player1, player2):
    return player1 if number_rounds % 2 != 0 else player2


number_of_rounds = 0
while True:
    number_of_rounds += 1
    row, col = [int(el) for el in eval(input())]
    player = select_player(number_of_rounds, player_1, player_2)
    current_throw = matrix[row][col]
    if 0 > row > matrix_dimensions - 1 or 0 > col > matrix_dimensions - 1:
        continue
    else:
        if current_throw.isdigit():
            score[player] -= int(current_throw)

        elif current_throw == "D":
            for el in range(matrix_dimensions):

