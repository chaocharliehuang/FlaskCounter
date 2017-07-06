from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    if session.get('count'):
        session['count'] += 1
    else:
        session['count'] = 1
    return render_template('index.html')

@app.route('/add2', methods=['POST'])
def add2():
    session['count'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['count'] = 0
    return redirect('/')

app.run(debug=True)