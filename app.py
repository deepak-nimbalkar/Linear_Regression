from flask import Flask, app, render_template, request,jsonify
from flask_cors import CORS, cross_origin
import pickle
# import sklearn.neighbors._base
import sys
# sys.modules['sklearn.neighbors.base'] = sklearn.neighbors._base

app = Flask(__name__)

@app.route('/', methods=['GET'])
@cross_origin()

def homepage():
    return render_template('index.html')


@app.route('/predict', methods=['POST','GET'])
@cross_origin()

def index():
    if request.method == 'POST':
        try:
            CRIM = float(request.form['CRIM'])
            ZN = float(request.form['ZN'])
            INDUS = float(request.form['INDUS'])
            CHAS = float(request.form['CHAS'])
            NOX = float(request.form['NOX'])
            RM = float(request.form['RM'])
            AGE = float(request.form['AGE'])
            DIS = float(request.form['DIS'])
            RAD = float(request.form['RAD'])
            TAX = float(request.form['TAX'])
            PTRATIO = float(request.form['PTRATIO'])
            B = float(request.form['B'])
            LSTAT = float(request.form['LSTAT'])
            
            # print(LSTAT)
            filename = 'boston_model.pickle'
            model = pickle.load(open(filename,'rb'))
            data = [CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT]
            pred = model.predict([data])

            return render_template('result.html', model_re=pred)
            

        
        except Exception as e:
            print('Error ', e)
            return "something is going wrong "

    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)