# NBD comment added in 2023
from flask import Flask,render_template,jsonify,request
from flask_sqlalchemy import SQLAlchemy
import pymysql
from dbs import *
import numpy as np
import pickle

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mauli143@localhost/carprediction'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO']=True
db = SQLAlchemy(app)

with open('random_forest_regression_model.pkl','rb') as file:
    model=pickle.load(file)

@app.route('/',methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/price_prediction',methods=['POST'])
def price_prediction():
    if request.method=='POST':
        data=request.form
        print(data)
         #[('Present_Price', '5.59'), ('Kms_Driven', '27000'), ('Owner', '0'), ('No_of_years', '7'), 
         # ('Fuel_Type', 'Petrol'), ('Seller_Type', 'Dealer'), ('Transmission', 'Manual')])
        Present_Price=data['Present_Price']
        Kms_Driven=int(data['Kms_Driven'])
        Owner=int(data['Owner'])
        Year=int(data['Year'])
        No_of_years=2020-Year
        if data['Fuel_Type']=='Petrol':
            Fuel_Type_Diesel=0   
            Fuel_Type_Petrol=1
        else:
            Fuel_Type_Diesel=1   
            Fuel_Type_Petrol=0
        if data['Seller_Type']=='Dealer':
            Seller_Type_Individual=0
        else:
            Seller_Type_Individual=1
        if data['Transmission']=='Manual':
            Transmission_Manual=1
        else:
            Transmission_Manual=0

    output=np.round(model.predict([[Present_Price, Kms_Driven, Owner, No_of_years,Fuel_Type_Diesel, 
    Fuel_Type_Petrol, Seller_Type_Individual,Transmission_Manual]]),2)
    Selling_price=output[0]
    data=write_into_database(Present_Price, Kms_Driven, Owner, No_of_years,Fuel_Type_Diesel, 
    Fuel_Type_Petrol, Seller_Type_Individual,Transmission_Manual,Selling_price)
    return render_template('home.html',prediction_text=f'Car Price is {Selling_price}')

if __name__=='__main__':
    app.run(debug=True)
    #print(db.fetchall())