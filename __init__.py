#!/usr/bin/env python3.4s

from flask import Flask,render_template,request,send_from_directory,session,redirect,url_for,json
from flask import request


app = Flask(__name__)

app.config['SECRET_KEY'] = 'my details secret!'


@app.route('/',methods=['GET'])
def potato():
	return render_template('index.html')

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
