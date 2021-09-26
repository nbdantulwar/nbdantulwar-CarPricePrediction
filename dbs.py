from app import db

class Car(db.Model):           #db.Model --> str
    __tablename__ = 'CARPRICE'
    id=db.Column('Record_No',db.Integer,primary_key=True)
    Present_Price = db.Column('Present_Price',db.Float())
    Kms_Driven = db.Column('Kms_Driven',db.Float())
    Owner = db.Column('Owner',db.Integer())
    No_of_years = db.Column('No_of_years',db.Float())
    Fuel_Type_Diesel = db.Column('Fuel_Type_Diesel',db.Integer())
    Fuel_Type_Petrol = db.Column('Fuel_Type_Petrol',db.Integer())
    Seller_Type_Individual = db.Column('Seller_Type_Individual',db.Integer())
    Transmission_Manual = db.Column('Transmission_Manual',db.Integer())
    Selling_price = db.Column('Selling_price',db.Float())

def write_into_database(Present_Price, Kms_Driven, Owner, No_of_years,Fuel_Type_Diesel, 
    Fuel_Type_Petrol, Seller_Type_Individual,Transmission_Manual,Selling_price):
    
    db.create_all()
    loc = Car(Present_Price=Present_Price, Kms_Driven=Kms_Driven, Owner=Owner,
    No_of_years=No_of_years,Fuel_Type_Diesel=Fuel_Type_Diesel, 
    Fuel_Type_Petrol=Fuel_Type_Petrol, Seller_Type_Individual=Seller_Type_Individual,
    Transmission_Manual=Transmission_Manual,Selling_price=Selling_price)
    db.session.add(loc)
    db.session.commit()

    