from flask import Flask, render_template, request, jsonify  # importing Flask class from flask module
from flask_bootstrap import Bootstrap
import json
from flask_cors import CORS
import util

app = Flask(__name__)  # defining app
# CORS(app)
Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True


@app.route("/")  # ENDPOINT
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/getstarted")
def getstarted():
    return render_template('getstarted.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/result")
def result():
    return render_template('result.html')


@app.route("/resultfail")
def resultfail():
    return render_template('resultfail.html')


@app.route('/predict_outcome', methods=['POST'])
def predict_outcome():
    age1 = int(request.form['age'])
    job1 = int(request.form['job'])
    default1 = int(request.form['default1'])
    balance1 = int(request.form['balance'])
    housing1 = int(request.form['housing'])
    month1 = int(request.form['month'])
    duration1 = int(request.form['duration'])
    poutcome1 = int(request.form['poutcome'])
    print(poutcome1)

    response = jsonify({
        'estimated_outcome': util.get_subscribed_status(age1, job1, default1, balance1, housing1, month1, duration1,
                                                        poutcome1)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


app.run(debug=True)
