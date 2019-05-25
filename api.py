from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/") #Decorators
def home():
    return render_template('home.html')

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/loc")
def loc():
	return "I am in Bangalore"

@app.route("/con")
def con():
	return render_template('contact.html')

@app.route("/login",methods=['POST'])
def login():
	user={'username':'vinay','password':'vinay'}
	username=request.form['username']
	password=request.form['password']

	if user['username'] == username:
		if user['password'] == password:
			return "login succesful!"
		return "Password doesn't match"
	return "username doesn't match"

app.run(debug=True)