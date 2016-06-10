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
      return redirect(url_for('multiply_matrices'))


@app.route('/multiply_matrices/')
def multiply_matrices():
  from multiply_matrices import run as multiply_run
  try:
    multiply_run(output_directory=('/home/benton/drewan_tech/demo_output/'))
    flash('A set of generated matrices have been multiplied.')
    return redirect(url_for('index'))
  except Exception as e:
    flash(e)
    return redirect(url_for('index'))
