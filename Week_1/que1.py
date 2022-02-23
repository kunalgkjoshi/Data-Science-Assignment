def matrix_mul(a, b):
    columns_a = len(a[0])
    rows_b = len(b)

    if columns_a == rows_b:
        result_lst = [[sum(a * b for a, b in zip(a_row, b_col))
                       for b_col in zip(*b)]
                      for a_row in a]
        return result_lst
    else:
        print('Not Possible')


A = [[1, 3, 4],
    [2, 5, 7],
    [5, 9, 6]]

B = [[1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]]

product = matrix_mul(A, B)
print(product)
