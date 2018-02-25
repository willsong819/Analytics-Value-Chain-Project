from flask import Flask,request,render_template
import pickle
import pandas as pd
import statsmodels.api as sm

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def parser():
 return render_template('index.html')

@app.route('/', methods = ['POST'])
def model():
  mileage_new = float(request.form['mileage'])
  door_count_new = float(request.form['door_count'])
  seat_count_new = float(request.form['seat_count'])
  engine_displacement_new = float(request.form['engine_displacement'])
  engine_power_new = float(request.form['engine_power'])
  user_input = [mileage_new,door_count_new,seat_count_new,engine_displacement_new,engine_power_new]

  mymodel=pickle.load(open('mymodel.p',"rb"))
  pred="The predicted price is: €"+str(round(float(mymodel.predict(user_input)),2))
  return render_template("index.html",price=pred)
  
if __name__ == '__main__':
	app.run()


