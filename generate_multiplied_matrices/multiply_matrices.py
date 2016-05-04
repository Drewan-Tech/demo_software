#  Copyright 2016
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED


if __name__ == '__main__':
  import sys
  try:
    import argparse
    from drewantech_common.value_checks import valid_directory
    from drewantech_common.string_generator \
        import generate_32_character_random_string
    import json
    from matrix_functions import multiply as multiply_matrices
    import os
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
    instance_id = generate_32_character_random_string()
    module_name = (os.path.basename(__file__).rstrip('.py'))
    multiplied_matrix = (multiply_matrices(json.load(args.matrix_a_file),
                                           json.load(args.matrix_b_file)))
    file_location_and_name = ('{}/{}_{}_Matrix_A.asc'
                              .format(args.output_directory,
                                      instance_id,
                                      module_name))
    with open(file_location_and_name, 'w') as matrix_write:
      json.dump(multiplied_matrix, matrix_write)
    sys.exit(0)
  except Exception as e:
    print(e)
    sys.exit(1)
