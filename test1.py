
from flask import Flask,redirect, url_for, request,render_template,session
import requests
app = Flask(__name__)

@app.route('/',methods= ['POST','GET'])
def login():
	
	if request.method=='POST':
		if  request.form['Username']=='Admin' and request.form['Password']=='1234' :
			session['username']='Admin'
			session['password']='1234'
			return render_template('test1.html',user=session['username'])
		else:
			error="Invalid Password or username"
			return render_template('login.html',error=error)
	else:
		error="" 
		return render_template('login.html',error=error)

@app.route('/main',methods = ['POST','GET'])
def search():
		
	if request.method=='POST':	
		word = request.form['searched_word']
		address="https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exintro=&exsentences=2&explaintext=&format=json&redirects=&formatversion=2&titles=" + word
		return render_template('aftersearch.html',data=requests.get(address).json()['query']['pages'][0]['extract'])
	else :
		error="Sorry!You cannot search till you login"
		return render_template('login.html',error=error)
if __name__ == '__main__':
   app.secret_key = 'super secret key'
   app.run(debug = True)
