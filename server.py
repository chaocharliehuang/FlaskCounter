from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key = 'secret'
count = 0

@app.route('/')
def index():
    global count
    count += 1
    session['count'] = count
    return render_template('index.html')

app.run(debug=True)