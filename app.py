# name:Maryam Amediaz
# ID:40125420

import pymongo as pymongo
from flask import Flask, render_template, request
import csv
from pymongo import MongoClient
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Email


app = Flask(__name__)

if __name__ == '__main__':
    app.run()

@app.route('/')
def index():
    return render_template('base.html')


@app.route('/product')
def product():
    # products = productList.find()
    prefix = '/static/'
    with open('data/productList.csv') as f:
        product_list = list(csv.reader(f))
    # print(product_list)
    return render_template('product.html', doc_list=product_list, prefix=prefix)


@app.route('/about_us')
def about_us():
    return render_template('aboutUs.html')


@app.route('/contact')
def contact_form():
    return render_template('contact_form.html')


@app.route('/contact_submission', methods=['POST'])
def handle_contact_form():
    if request.method == 'POST':
        with open('data/clients_contacts.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([request.form['first_name'],request.form['last_name'],request.form['city'],request.form['email'],request.form['message']])
        return render_template('contact_validated_response.html',data=request.form)
    else:
        return render_template('base.html')


