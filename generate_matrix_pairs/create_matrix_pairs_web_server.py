#  Copyright 2016
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED


from flask import (Flask,
                   render_template,
                   request)


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    return render_template('index_get.html')
  else:
    if request.method == 'POST':
      return render_template('index_post.html',
                             A_rows_B_columns=request.form['A_rows_B_columns'],
                             B_rows_A_columns=request.form['B_rows_A_columns'],
                             max_random_value=request.form['max_random_value'])
