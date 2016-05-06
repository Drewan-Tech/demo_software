#  Copyright 2016
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED


def create_matrix(number_of_rows,
                  number_of_columns,
                  scaling_factor):
  """Will create a matrix with the given size. The random numbers generated
  will be in the range of 0 to the scaling factor.
  """
  import random
  from drewantech_common.value_checks import is_number_type_not_complex
  if type(number_of_rows) is not int:
    raise TypeError('Number of rows arg passed to create_matrix function is '
                    'not an int type')
  if type(number_of_columns) is not int:
    raise TypeError('Number of columns arg passed to create_matrix function '
                    'is not an int type')
  if not is_number_type_not_complex(scaling_factor):
    raise TypeError('Scaling factor arg passed to create_matrix function '
                    'is not an int or float type.')
  return [[(random.random() * scaling_factor)
           for column in range(number_of_columns)]
          for row in range(number_of_rows)]


if __name__ == '__main__':
  print(create_matrix(7, 3, 10))
