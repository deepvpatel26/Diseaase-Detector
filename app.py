from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
 
import joblib

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
	if request.method == 'POST':
		my_Name = request.form.get('Name')
		my_Age = request.form.get('Age')
		my_gender = request.form.get('Gender')
		my_symptoms = request.form.get('Symptoms')
	return render_template('result.html',Name= my_Name ,Age= my_Age , Gender = my_gender , Symptoms = my_symptoms)



if __name__ == '__main__':
	app.run(debug=True)