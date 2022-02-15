dimensions_matrix = int(input())
matrix = []
food_eaten = 0


def is_valid_position(ma, row, col):
    if row < 0 or col < 0 or row >= len(ma) or col >= len(ma):
        return False
    return True


def what_symbol(ma, row, col, food_eaten=None):
    if ma[row][col] == "*":
        food_eaten += 1
        ma[row][col] = "S"
    elif ma[row][col] == "-":
        ma[row][col] = "S"
    elif ma[row][col] == "B":
        ma[row][col] = "."
        if row == burrows[0]:
            pass


for _ in range(dimensions_matrix):
    matrix.append([x for x in input()])
burrows = []
for row in range(dimensions_matrix):
    for col in range(dimensions_matrix):
        if matrix[row][col] == "S":
            start_row, start_col = row, col
        elif matrix[row][col] == "B":
            burrows.append(row)
            burrows.append(col)

start_position = matrix[start_row][start_col]
while True:
    command = input()
    if command == "up":
        try:
            current_position = matrix[start_row - 1][start_col]
        except IndexError:
            print("Game over")
            print(f'Food eaten: {food_eaten}')
            break

    elif command == "down":
        pass
    elif command == "right":
        pass
    if command == "left":
        pass
