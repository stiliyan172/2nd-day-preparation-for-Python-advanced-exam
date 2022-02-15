def next_position(direction, row, col):
    if direction == 'down':
        return row + 1, col
    elif direction == 'up':
        return row -1, col
    elif direction == 'left':
        return row, col - 1
    elif direction == 'right':
        return row, col + 1

size = int(input())

matrix = []
snake_row = 0
snake_col = 0
food = 0
burrows = []
is_lost = False
for row in range(size):
    matrix.append(list(input()))
    for col in range(size):
        if matrix[row][col] == 'S':
            snake_row = row
            snake_col = col
        if matrix[row][col] == 'B':
            burrows.append([row,col])

while True:
    if food == 10:
        break
    command = input()
    next_row, next_col = next_position(command, snake_row, snake_col)

    if next_col < 0 or next_row < 0 or next_row >= size or next_col >= size:
        is_lost = True
        break
    if matrix[next_row][next_col] == 'B':
        matrix[next_row][next_col] = '.'
        matrix[snake_row][snake_col] = '.'
        burrows.pop(burrows.index([next_row, next_col]))
        snake_row, snake_col = burrows[0][0], burrows[0][1]
    elif matrix[next_row][next_col] == '*':
        food += 1
        matrix[snake_row][snake_col] = '.'
        snake_row, snake_col = next_row, next_col
    else:
        matrix[snake_row][snake_col] = '.'
        snake_row, snake_col = next_row, next_col
    matrix[snake_row][snake_col] = 'S'

if is_lost:
    matrix[snake_row][snake_col] = '.'
    print(f'Game over!')
else:
    print(f"You won! You fed the snake.")

print(f"Food eaten: {food}")

for i in matrix:
    print(*i, sep='')





