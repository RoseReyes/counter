from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsASecretKey'

@app.route('/') #This is the root
def index():
    session['counter'] = 0
    session.modified = True
    return render_template('index.html')

@app.route('/increaseCount', methods=['POST'])
def increaseCount():
	incrementType = str(request.form['increase'])
	session['counter']+=2
	return render_template('index.html', counter = session['counter'])

@app.route('/decreaseCount', methods=['POST'])
def decreaseCount():
	reverseType = str(request.form['decrease'])
	session['counter']-=1
	return render_template('index.html', counter = session['counter'])

#need to verify why method not allowed error occur when the whole route is accessed not refreshed


app.run(debug=True)