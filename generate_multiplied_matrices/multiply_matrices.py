#  Copyright 2016
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED


if __name__ == '__main__':
  import argparse
  from drewantech_common.value_checks import valid_directory
  from drewantech_common.string_generator \
      import generate_32_character_random_string
  import json
  from matrix_functions import multiply as multiply_matrices
  parser = argparse.ArgumentParser(description='Multiplies two matrices.')
  parser.add_argument('matrix_a_file',
                      type=argparse.FileType(mode='r'),
                      help='File containing matrix A data.')
  parser.add_argument('matrix_b_file',
                      type=argparse.FileType(mode='r'),
                      help='File containing matrix B data.')
  parser.add_argument('output_directory',
                      type=valid_directory,
                      help='Directory to write file containing product.')
  args = parser.parse_args()
  multiplied_matrix = (multiply_matrices(json.load(args.matrix_a_file),
                                         json.load(args.matrix_b_file)))
  file_location_and_name = ('{}/{}.asc'
                            .format(args.output_directory,
                                    generate_32_character_random_string()))
  with open(file_location_and_name, 'w') as matrix_write:
    json.dump(multiplied_matrix, matrix_write)
