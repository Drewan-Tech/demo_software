#  Copyright 2016
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED


def multiply_matrices(matrix_a, matrix_b):
  transpose_b = transpose_matrix(matrix_b)
  return[[sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b))
         for col_b in transpose_b] for row_a in matrix_a]


def transpose_matrix(matrix):
  return list(zip(*matrix))


if __name__ == '__main__':
  print(multiply_matrices([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
