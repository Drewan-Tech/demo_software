#  Copyright 2016
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED


from drewantech_common.database_operations \
    import PostgresqlDatabaseManipulation


database_name = 'demo_database'


db_connection = PostgresqlDatabaseManipulation('benton',
                                               'benton',
                                               'localhost',
                                               5432,
                                               'benton')


def create_database():
  db_connection.manipulate_database('CREATE', database_name)


def drop_database():
  db_connection.manipulate_database('DROP', database_name)
