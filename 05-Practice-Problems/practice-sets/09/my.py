# Matrix Multiplication in Simple Way

# Input matrix sizes
rows1 = int(input("Enter rows of first matrix: "))
cols1 = int(input("Enter columns of first matrix: "))

rows2 = int(input("Enter rows of second matrix: "))
cols2 = int(input("Enter columns of second matrix: "))

# Check multiplication condition
if cols1 != rows2:
    print("Matrix multiplication not possible")

else:
    # First matrix input
    matrix1 = []
    print("Enter first matrix:")

    for i in range(rows1):
        row = list(map(int, input().split()))
        matrix1.append(row)

    # Second matrix input
    matrix2 = []
    print("Enter second matrix:")

    for i in range(rows2):
        row = list(map(int, input().split()))
        matrix2.append(row)

    # Result matrix
    result = []

    for i in range(rows1):
        row = []

        for j in range(cols2):
            total = 0

            for k in range(cols1):
                total += matrix1[i][k] * matrix2[k][j]

            row.append(total)

        result.append(row)

    # Print result
    print("Result Matrix:")

    for row in result:
        print(row)
