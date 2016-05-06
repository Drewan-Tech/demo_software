#  Copyright 2016
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED


def run(output_directory):
  from drewantech_common.value_checks import valid_directory
  from drewantech_common.string_generator \
      import generate_32_character_random_string
  import json
  from matrix_functions import multiply as multiply_matrices
  import os
  from demo_software.infrastructure.demo_database import (db_connection,
                                                          database_name,
                                                          Job,
                                                          GeneratedFile,
                                                          OperatingOn,
                                                          JobStatus)
  from drewantech_common.database_operations import database_transaction
  valid_directory(output_directory)
  instance_id = generate_32_character_random_string()
  module_name = (os.path.basename(__file__).rstrip('.py'))
  required_producer = 'create_matrix_pair'
  matrix_files = {}
  with (database_transaction(db_connection
        .connect_to_database(database_name))) as session:
    session.add(Job(id=instance_id, producer=module_name, is_finished=False))
    potential_jobs = (session.query(Job)
                      .filter_by(producer=required_producer,
                                 is_finished=True)
                      .all())
    already_worked_jobs = (session.query(OperatingOn).all())
    canidate_jobs = []
    for potential_job in potential_jobs:
      canidate_job = True
      for worked_job in already_worked_jobs:
        if potential_job.id in worked_job.operand_id:
          canidate_job = False
      if canidate_job:
        canidate_jobs.append(potential_job)
    if not canidate_jobs:
      session.add(JobStatus(job_id=instance_id,
                            status='No jobs need matrix multiplication.'))
      job = session.query(Job).filter_by(id=instance_id).one()
      job.is_finished = True
    else:
      job_to_work = canidate_jobs[0].id
      session.add(OperatingOn(operator_id=instance_id, operand_id=job_to_work))
      for row in (session
                  .query(GeneratedFile)
                  .filter_by(job_id=job_to_work)
                  .all()):
        if 'Matrix_A' in row.file_name:
          matrix_files['Matrix_A'] = row.file_name
        else:
          if 'Matrix_B' in row.file_name:
            matrix_files['Matrix_B'] = row.file_name
          else:
            message = ('Unrecognized file name, {}, cannot process.'
                       .format(row.file_name))
            session.add(JobStatus(job_id=instance_id,
                                  status=message))
            raise ValueError(message)
      if not matrix_files:
        message = ('No files found for job {}.'.format(job_to_work))
        session.add(JobStatus(job_id=instance_id,
                              status=message))
        raise ValueError(message)
  if matrix_files:
    for matrix_type in matrix_files:
      if type(matrix_files[matrix_type]) is not str:
        message = ('The type of the file name, {}, is not a str.'
                   .format(matrix_files[matrix_type]))
        with (database_transaction(db_connection
              .connect_to_database(database_name))) as session:
          session.add(JobStatus(job_id=instance_id,
                                status=message))
        raise TypeError(message)
      if not os.path.isfile(matrix_files[matrix_type]):
        message = ('The file name, {}, is not valid.'
                   .format(matrix_files[matrix_type]))
        with (database_transaction(db_connection
              .connect_to_database(database_name))) as session:
          session.add(JobStatus(job_id=instance_id,
                                status=message))
        raise OSError(message)
    file_location_and_name = ('{}/{}_{}_Matrix_A.asc'
                              .format(args.output_directory,
                                      instance_id,
                                      module_name))
    with open(matrix_files['Matrix_A'], 'r') as matrix_A_file:
      with open(matrix_files['Matrix_B'], 'r') as matrix_B_file:
        multiplied_matrix = multiply_matrices(json.load(matrix_A_file),
                                              json.load(matrix_B_file))
        with open(file_location_and_name, 'w') as matrix_write:
          json.dump(multiplied_matrix, matrix_write)
    with (database_transaction(db_connection
          .connect_to_database(database_name))) as session:
      job = session.query(Job).filter_by(id=instance_id).one()
      job.is_finished = True
      session.add(GeneratedFile(file_name=file_location_and_name,
                                job_id=instance_id))
      message = ('Successfully multiplied matrices.')
      session.add(JobStatus(job_id=instance_id,
                            status=message))


if __name__ == '__main__':
  import sys
  try:
    import argparse
    from drewantech_common.value_checks import valid_directory
    parser = argparse.ArgumentParser(description='Multiplies two matrices.')
    parser.add_argument('output_directory',
                        type=valid_directory,
                        help='Directory to write file containing product.')
    args = parser.parse_args()
    run(args.output_directory)
    sys.exit(0)
  except Exception as e:
    print(e)
    sys.exit(1)
