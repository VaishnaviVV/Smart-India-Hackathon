from flask import Flask,render_template

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')


@app.route('/aboutus',methods=['GET'])
def aboutus():
    return render_template('aboutus.html')

@app.route('/contactus',methods=['GET','POST'])
def contactus():
    return render_template('contactus.html')


@app.route('/map',methods=['GET','POST'])
def map():
    return render_template('map.html')