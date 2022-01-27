def print_matrix(matrix, n, m,  width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()

n = int(input())
m = int(input())

matrix = []

for i in range(n):
    temp = [ input() for num in range(m) ]
    matrix.append(temp)

print_matrix(matrix, n, m)

"""
n, m = int(input()), int(input())
matrix = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(input())
        matrix.append(row)

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()
"""
