def multiply_matrices(A, B):
    result = [[sum(a * b for a, b in zip(row, col)) for col in zip(*B)] for row in A]
    print("Matrix A:")
    for row in A:
        print(row)
    print("Matrix B:")
    for row in B:
        print(row)
    print("Result of Matrix Multiplication:")
    for row in result:
        print(row)

A = [[1, 2], [3, 4]]
B = [[2, 0], [1, 2]]

multiply_matrices(A, B)
