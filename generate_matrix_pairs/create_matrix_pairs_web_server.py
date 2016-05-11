#  Copyright 2016
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED


from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
  return ('Create Matrix Pairs')

if __name__ == '__main__':
  app.run(host='localhost', port=8080, debug=True)
