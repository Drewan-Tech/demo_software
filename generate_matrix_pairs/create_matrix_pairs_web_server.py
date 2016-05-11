#  Copyright 2016
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED


from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
  return ('Create Matrix Pairs')
