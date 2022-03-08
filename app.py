from flask import Flask,render_template

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def map():
    return render_template('map.html')