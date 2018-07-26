#from flask import Flask
#app = Flask(__name__)

#@app.route("/hello")
#def hello():
#    return "Hello World!" 



#if __name__ == '__main__':
 #    app.run()
from flask import Flask
app = Flask(__name__)

@app.route('https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles=<name>')
def hello_name(name):
   return 'Hello %s!' % name

if __name__ == '__main__':
   app.run(debug = True)