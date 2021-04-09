#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from wtforms import Form, StringField, TextField, validators, IntegerField, DecimalField

class MyForm(Form):
	glucose = IntegerField('Glucose (mg/dl)', 
		[
		validators.DataRequired()
		])
	bmi = DecimalField('BMI (kg/m2))', 	[
		validators.DataRequired()
		])
	age = IntegerField('Age (years) ', 	[
		validators.DataRequired()
		])
