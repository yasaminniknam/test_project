from flask import Flask, redirect, url_for, request,Session
app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name


@app.route('/login',method = ['GET'])
def login():

Session[‘username’] = ’admin’
Session[‘password’] = ’1234’
	if request.form['Username']==Session['usrname'] and request.form['Password']==Session['password'] :
return redirect(url_for('main'))
   else:
      return redirect('/login')

if __name__ == '__main__':
   app.run(debug = True)