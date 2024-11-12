from flask import Blueprint, render_template, request

simulate_route = Blueprint('simulate', __name__)

@simulate_route.route('/simulate', methods=['POST'])
def simulate():
    initial = float(request.form['initial'])
    rate = float(request.form['rate'])
    time = int(request.form['time'])
    final_amount = round(initial * (1 + rate/100) ** time, 2)


    return render_template('result.html', 
                           initial=initial, 
                           final_amount=final_amount)