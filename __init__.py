#!/usr/bin/env python3.4s

from flask import Flask,render_template,request,send_from_directory,session,redirect,url_for,json,flash
from flask import request


app = Flask(__name__)

app.config['SECRET_KEY'] = 'my details secret!'


@app.route('/',methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/form',methods=['GET','POST'])
def form():
	return render_template('tech_reg(2).html')

@app.route('/form_main',methods=['GET','POST'])
def form_main():
	return render_template('form_main.html')
	
@app.route('/form_submit',methods=['GET','POST'])
def form_submit():
	a = request.form['personname']
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

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        Name = request.form['Name']
        college = request.form['college']
        Mobile = request.form['Mobile']
        e_mail = request.form['e_mail']
        print(Name, college, Mobile, e_mail)
        flash('success', 'success')
        return redirect(url_for('registration'))
    else:
        return render_template('yup.html')


if __name__ == '__main__':
	app.run(host='0.0.0.0',port=9876,debug=True)
