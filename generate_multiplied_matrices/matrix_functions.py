#  Copyright 2016
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED


def multiply(matrix_a, matrix_b):
  transpose_b = transpose(matrix_b)
  return[[sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b))
         for col_b in transpose_b] for row_a in matrix_a]


def transpose(matrix):
  return list(zip(*matrix))
