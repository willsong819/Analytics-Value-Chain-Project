from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def parser():
 return render_template('index.html')

@app.route('/', methods = ['POST'])
def model():
  test = request.form['mileage']
  test2 = request.form['body type']
  if test == 'test' or test2 == 'compact':
    return '<h3> test succeed</h3>'
  else:
    return '<h3> invalid </h3>'


if __name__ == '__main__':
	app.run()


