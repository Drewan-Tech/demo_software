#  Copyright 2016
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED


if __name__ == '__main__':
  from demo_software.infrastructure import demo_database
  demo_database.create_database()
  demo_database.create_tables()
