from flask import Flask, url_for, render_template
from routes.home import home_route
from routes.simulate import simulate_route

app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(simulate_route)
app.run(debug=True)
