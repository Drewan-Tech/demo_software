#  Copyright 2016
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED


from flask import (Flask,
                   render_template,
                   request,
                   flash,
                   url_for,
                   redirect)
from os import urandom


app = Flask(__name__)
app.secret_key = urandom(32)


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    return render_template('index.html')
  else:
    if request.method == 'POST':
      try:
        int(request.form['A_rows_B_columns'])
        int(request.form['B_rows_A_columns'])
      except:
        flash('Please provide integer values for the number of rows and '
              'columns.')
        return render_template('index.html')
      try:
        float(request.form['max_random_value'])
      except:
        flash('Please provide a valid number for the maximum random number.')
        return render_template('index.html')
      return redirect(url_for('matrix_pair',
                      A_rows_B_columns=int(request
                                           .form['A_rows_B_columns']),
                      B_rows_A_columns=int(request
                                           .form['B_rows_A_columns']),
                      max_random_value=float(request
                                             .form['max_random_value'])))


@app.route('/matrix_pair'
           '/<int:A_rows_B_columns>'
           '/<int:B_rows_A_columns>'
           '/<float:max_random_value>'
           '/')
def matrix_pair(A_rows_B_columns,
                B_rows_A_columns,
                max_random_value):
  from create_matrix_pair import run
  try:
    run(a_rows_b_columns=A_rows_B_columns,
        a_columns_b_rows=B_rows_A_columns,
        random_values_max_range=max_random_value,
        output_directory=('/home/benton/drewan_tech/demo_output/'))
    flash('A pair of matrices were generated for: '
          'A_rows_B_columns = {}, '
          'B_rows_A_columns = {}, '
          'max_random_value = {}'
          .format(A_rows_B_columns,
                  B_rows_A_columns,
                  max_random_value))
    return redirect(url_for('index'))
  except Exception as e:
    flash(e)
    return redirect(url_for('index'))
