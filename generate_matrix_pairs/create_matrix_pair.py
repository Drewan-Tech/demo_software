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
  import sys
  try:
    import argparse
    import json
    from drewantech_common.value_checks import valid_directory
    from drewantech_common.string_generator \
        import generate_32_character_random_string
    import os
    from demo_infrastructure.demo_database import (db_connection,
                                                   database_name,
                                                   Job,
                                                   GeneratedFile)
    from drewantech_common.database_operations import database_transaction
    parser = argparse.ArgumentParser(description='Generates two matrices of '
                                                 'random values with the size '
                                                 'provided. The row size of '
                                                 'matrix A will be the column '
                                                 'size of matrix B and the '
                                                 'column size of matrix A '
                                                 'will be the row size of '
                                                 'matrix B. The random values '
                                                 'will be in the range from '
                                                 '0 to the max range value '
                                                 'provided.')
    parser.add_argument('a_rows_b_columns',
                        type=int,
                        help='Matrix size of rows for matrix A and columns '
                             'for matrix B.')
    parser.add_argument('a_columns_b_rows',
                        type=int,
                        help='Matrix size of columns for matrix A and rows '
                             'for matrix B.')
    parser.add_argument('random_values_max_range',
                        type=float,
                        help='Max range values for the random values '
                             'populated into the matrices.')
    parser.add_argument('output_directory',
                        type=valid_directory,
                        help='Directory to write the two output matrix files.')
    args = parser.parse_args()
    instance_id = generate_32_character_random_string()
    module_name = (os.path.basename(__file__).rstrip('.py'))
    with (database_transaction(db_connection
          .connect_to_database(database_name))) as session:
      session.add(Job(id=instance_id, producer=module_name, is_finished=False))
    matrix_a, matrix_b = generate_pair_of_matrices(args
                                                   .a_rows_b_columns,
                                                   args
                                                   .a_columns_b_rows,
                                                   args
                                                   .random_values_max_range)
    matrices = {'Matrix_A': matrix_a,
                'Matrix_B': matrix_b}
    with (database_transaction(db_connection
          .connect_to_database(database_name))) as session:
      for matrix in matrices:
        file_location_and_name = ('{}/{}_{}_{}.asc'
                                  .format(args.output_directory,
                                          instance_id,
                                          module_name,
                                          matrix))
        session.add(GeneratedFile(file_name=file_location_and_name,
                                  job_id=instance_id))
        with open(file_location_and_name, 'w') as matrix_write:
          json.dump(matrices[matrix], matrix_write)
    with (database_transaction(db_connection
          .connect_to_database(database_name))) as session:
      job = session.query(Job).filter_by(id=instance_id).one()
      job.is_finished = True
    sys.exit(0)
  except Exception as e:
    print(e)
    sys.exit(1)
