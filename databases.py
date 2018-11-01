from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product(name,price,quantity,shipping,color):
  product_object = Product(
      name=name,
      price=price,
      quantity=quantity,
      shipping=shipping,
      color=color)
  session.add(product_object)
  session.commit()


def update_product(id,quantity,price):
  product_object = session.query(Product).filter_by(id=id).first()
  product_object.quantity=quantity
  product_object = session.query(Product).filter_by(id=id).first()
  product_object.price=price
  session.commit()


def delete_product(id):
  session.query(Product).filter_by(id=id).delete()
  session.commit()
  
def get_product(id):
  pass
