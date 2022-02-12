matrix_dimensions = 6
throws = 3

matrix = [input().split() for _ in range(matrix_dimensions)]
total_score = 0
for throw in range(throws):
    row, col = eval(input())
    if row > matrix_dimensions or col > matrix_dimensions:
        continue
    if matrix[row][col] == "B":
        stroke_column = []
        for el in range(matrix_dimensions):
            if matrix[el][col].isdigit():
                stroke_column.append(int(matrix[el][col]))
        matrix[row][col] = 0

        total_score += sum(stroke_column)

if total_score < 100:
    print(f"Sorry! You need {100 - total_score} points more to win a prize.")
elif 100 <= total_score < 200:
    print(f"Good job! You scored {total_score} points, and you've won Football.")
elif 200 <= total_score < 300:
    print(f"Good job! You scored {total_score} points, and you've won Teddy Bear.")
elif total_score >= 300:
    print(f"Good job! You scored {total_score} points, and you've won Lego Construction Set.")