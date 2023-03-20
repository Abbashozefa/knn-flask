from flask import Flask,request,render_template
import pickle

model=pickle.load(open('model.pkl','rb'))


app=Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predicts',methods=['POST','GET'])
def predict():
    alcohol=float(request.form['alcohol'])
    malic_acid=float(request.form['malic_acid'])
    ash=float(request.form['ash'])
    alcalinity_of_ash=float(request.form['alcalinity_of_ash'])
    magnesium=float(request.form['magnesium'])
    total_phenols=float(request.form['total_phenols'])
    flavanoids=float(request.form['flavanoids'])
    nonflavanoid_phenols=float(request.form['nonflavanoid_phenols'])
    proanthocyanins=float(request.form['proanthocyanins'])
    color_intensity=float(request.form['color_intensity'])
    hue=float(request.form['hue'])
    od=float(request.form['od280/od315_of_diluted_wines'])
    proline=float(request.form['proline'])
    
    prediction=model.predict([[alcohol, malic_acid, ash, alcalinity_of_ash, magnesium, total_phenols, flavanoids, nonflavanoid_phenols, proanthocyanins, color_intensity, hue, od, proline]])
    if(prediction[0] == 0):
        output='A'
    elif(prediction[0] == 1):
        output='B'
    else:
        output='C'
    return render_template('index.html',prediction_text=f'THE WINE IS OF CLASS {output}')       

    

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000)

