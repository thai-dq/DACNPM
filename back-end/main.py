from flask import Flask,request,render_template
import db
import json
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('layout.loitd',var1="ahihi")

@app.route("/users")
def findName():
	db.connectDB()
	results = db.getData()
	temp =[]
	for data in results:
		temp.append(data)
	db.closeDB()
	return json.dumps(temp)
<<<<<<< HEAD
@app.route("/user/<_username>")
def findNameID(_username):
	db.connectDB()
	results = db.getUser(_username);
=======

@app.route("/user/<int:username>")
def findNameID(username):
	db.connectDB()
	results = db.getUser(username)
>>>>>>> 38a8ce6de7134140ae44f0f3623dbdbed5d5df8b
	temp =[]
	for data in results:
		temp.append(data)
	db.closeDB()
	return json.dumps(temp)

@app.route("/insert")
def insertDB():
	db.connectDB()
	_id = "test1235"
	db.insertData(_id, "1234567", 0)
	db.closeDB()
<<<<<<< HEAD
	return "OK"
=======

@app.route("/login", methods=['POST'])
def login():
	db.connectDB()
	#data = request.form
	username = request.form['username']
	password = request.form['password']
	#print(request.data)
	users = db.getUserByUsername(username)
	db.closeDB()
	for user in users:
		if (user == None):
			return Response("{'a':'b'}", status=401, mimetype='application/json') 
		#encryptedPass = bcrypt.generate_password_hash(data.password)
		if (username == user['tai_khoan'] and password == user['mat_khau']):#bcrypt.check_password_hash(encryptedPass, password)):
			return user

	
>>>>>>> 38a8ce6de7134140ae44f0f3623dbdbed5d5df8b
