#  Copyright 2016
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED


if __name__ == '__main__':
  from demo_infrastructure import demo_database
  demo_database.drop_tables()
  demo_database.drop_database()
