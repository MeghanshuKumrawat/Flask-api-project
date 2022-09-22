from flask import Blueprint, jsonify, request
from ..db.models import Book, Transaction
import pandas as pd
import random

# define the blueprint
db_populate = Blueprint(name="db_populate", import_name=__name__)


@db_populate.route('/db-populate', methods=['GET'])
def database_populate():
    data = pd.read_csv('https://gist.githubusercontent.com/jaidevd/23aef12e9bf56c618c41/raw/c05e98672b8d52fa0cb94aad80f75eb78342e5d4/books.csv')
    for i in range(20):
        temp = data.loc[i].to_dict()
        book = Book(name=temp["Title"], category=temp["Genre"], rent=random.randrange(100, 1000, 3))
        book.save()
    
    return {"data":"Database Polulated!"}
