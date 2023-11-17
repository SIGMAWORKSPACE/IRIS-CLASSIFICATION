from flask import Flask,render_template,request
import pickle

app=Flask(__name__)
model=pickle.load(open('saved_model.sav','rb'))
@app.route('/')
def home():
    result = ''
    return render_template('index.html',**locals())


@app.route('/predict', methods=['POST'])
def predict():
    sepal_length = float(request.form.get('sepal_length', 0.0))
    sepal_width = float(request.form.get('sepal_width', 0.0))
    petal_length = float(request.form.get('petal_length', 0.0))
    petal_width = float(request.form.get('petal_width', 0.0))

    result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]
    return render_template('index.html', result=result)



if __name__=='__main__':
    app.run(debug=True)
