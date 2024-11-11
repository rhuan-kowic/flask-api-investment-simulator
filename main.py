from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
  title = "Investment Simulator"
  return render_template('index.html', title=title)

app.run(debug=True)
