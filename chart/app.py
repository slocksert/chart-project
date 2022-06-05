from flask import Flask, render_template, request, flash
from chart_plotter import plotter
import datetime as dt

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def get_result():
    data = request.args.get('date_input')
    plotter.start = data
    return plotter
    

    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080,debug=True)