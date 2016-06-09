#  Copyright 2016
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED


from flask import (Flask,
                   render_template,
                   request,
                   flash)
from os import urandom


app = Flask(__name__)
app.secret_key = urandom(32)


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    return render_template('index_get.html')
  else:
    if request.method == 'POST':
      try:
        int(request.form['A_rows_B_columns'])
        int(request.form['B_rows_A_columns'])
      except:
        flash('Please provide integer values for the number of rows and '
              'columns.')
        return render_template('index_get.html')
      try:
        float(request.form['max_random_value'])
      except:
        flash('Please provide a valid number for the maximum random number.')
        return render_template('index_get.html')
      try:
        from os import path
        if not path.isdir(request.form['output_location']):
          raise OSError('Path not valid.')
      except:
        flash('{} is not a valid path.'
              .format(request.form['output_location']))
        return render_template('index_get.html')
      return render_template('index_post.html',
                             A_rows_B_columns=request
                             .form['A_rows_B_columns'],
                             B_rows_A_columns=request
                             .form['B_rows_A_columns'],
                             max_random_value=request
                             .form['max_random_value'],
                             output_location=request
                             .form['output_location'])
