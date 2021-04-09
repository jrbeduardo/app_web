from flask import Flask, request, jsonify, render_template, url_for, redirect, flash, session
import json 
from flask_bootstrap import Bootstrap
from flask_form import * 
import util

app=Flask(__name__)
Bootstrap(app)

@app.route("/")
def home():
	form = MyForm()
	form.validate()
	return render_template('index.html', form=form)

@app.route("/predicted_diabetes", methods=['POST'])
def predicted_diabetes():
	glucose = int(request.form['glucose'])
	bmi = float(request.form['bmi'])
	age = int( request.form['age'] )
	response = jsonify({
		'estimated_diabetes': util.get_diabetes_predicted(glucose, bmi, age)
	})
	return response


if __name__=="__main__":
	print("Iniciando servidor python flask...")
	app.run(debug=True)