#!/usr/bin/env python3.4s

from flask import Flask,render_template,request,send_from_directory,session,redirect,url_for,json
from flask import request


app = Flask(__name__)

app.config['SECRET_KEY'] = 'my details secret!'


@app.route('/',methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/form',methods=['GET','POST'])
def form():
	return render_template('form.html')

@app.route('/form_main',methods=['GET','POST'])
def form_main():
	return render_template('form_main.html')
	
@app.route('/form_submit',methods=['GET','POST'])
def form_submit():
	a = request.form['form-contact-name']
	print a
	return "hi"

@app.route('/form_data',methods=['POST','GET'])
def form_data():
	firstname = request.form['firstname']
	lastname = request.form['lastname']
	phno = request.form['phno']
	f = open('abc.txt','a')
	f.write('Data: '+firstname+" "+lastname+" "+phno+"\n")
	return ('I got '+firstname+" "+lastname+" "+phno)

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=9876,debug=True)
