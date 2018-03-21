from flask import Flask,request,render_template
import pickle
import pandas as pd
import statsmodels.api as sm
import logging

logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('used_car_webapp.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def parser():
  """This function renders the initial web page"""
  return render_template('index.html')

@app.route('/', methods = ['POST'])
def model():
  """
  This is the main function for the flask app.  

  It first stores user inputs, loads the pre-stored pickle model file, and makes prediction.  

  Finally it will refresh the page with the predicted price shown on the bottom.
  """

  mileage_new = float(request.form['mileage'])
  door_count_new = float(request.form['door_count'])
  seat_count_new = float(request.form['seat_count'])
  engine_displacement_new = float(request.form['engine_displacement'])
  engine_power_new = float(request.form['engine_power'])
  user_input = [mileage_new,door_count_new,seat_count_new,engine_displacement_new,engine_power_new]
  
  logger.info("Successfully got user inputs. Inputs are: %s" % str(user_input))

  mymodel=pickle.load(open('mymodel.p',"rb"))
  pred="The predicted price is: €"+str(round(float(mymodel.predict(user_input)),2))
  
  logger.info("Successfully predicted the price. It is: %s" % str(pred))

  return render_template("index.html",price=pred)
  
if __name__ == '__main__':
	app.run(host='0.0.0.0')


