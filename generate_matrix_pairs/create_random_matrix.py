#  Copyright 2016
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED

import random


def create_matrix(number_of_rows,
                  number_of_columns,
                  scaling_factor):
  """Will create a matrix with the given size. The random numbers generated
  will be in the range of 0 to the scaling factor.
  """
  if type(number_of_rows) is not int:
    raise ValueError('Number of rows arg passed to create_matrix function is '
                     'not an int type')
  if type(number_of_columns) is not int:
    raise ValueError('Number of columns arg passed to create_matrix function '
                     'is not an int type')
  if not valid_scaling_factor_type(scaling_factor):
    raise ValueError('Scaling factor arg passed to create_matrix function '
                     'is not an int or float type.')
  return [[(random.random() * scaling_factor)
           for column in range(number_of_columns)]
          for row in range(number_of_rows)]


def valid_scaling_factor_type(scaling_factor):
  if type(scaling_factor) is not int:
    if type(scaling_factor) is not float:
      return False
  return True


if __name__ == '__main__':
  print(create_matrix(7, 3, 10))
