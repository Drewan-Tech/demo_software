#  Copyright 2016
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED


def generate_pair_of_matrices(a_rows_b_columns,
                              a_columns_b_rows,
                              max_matrix_value):
  """Generate a pair of matrices filled with random values.

  The matrices will be generated so they can be multiplied. So the number of
  matrix A rows will match the number of matrix B columns and the number of
  matrix A columns will match the number of matrix B rows. The matrices will
  have random values in the range between 0 and the provided max_matrix_value.
  """
  from create_random_matrix import create_matrix
  from drewantech_common.value_checks import is_number_type_not_complex
  if type(a_rows_b_columns) is not int:
    raise ValueError('The type of the arg to set the matrix A rows and '
                     'matrix B columns in generate_pair_of_matrices function '
                     'is not an int type.')
  if type(a_columns_b_rows) is not int:
    raise ValueError('The type of the arg to set the matrix A columns and '
                     'matrix B rows in generate_pair_of_matrices function '
                     'is not an int type.')
  if not is_number_type_not_complex(max_matrix_value):
    raise ValueError('The max matrix value arg passed to the '
                     'generate_pair_of_matrices function is not an int or '
                     'float type.')
  matrix_a = create_matrix(a_rows_b_columns,
                           a_columns_b_rows,
                           max_matrix_value)
  matrix_b = create_matrix(a_columns_b_rows,
                           a_rows_b_columns,
                           max_matrix_value)
  return matrix_a, matrix_b


if __name__ == '__main__':
  matrix_a, matrix_b = generate_pair_of_matrices(4, 2, 10)
  print('Matrix A: ')
  print(matrix_a)
  print('Matrix B: ')
  print(matrix_b)
