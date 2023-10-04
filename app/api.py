from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
import mysql.connector

app = Flask(__name__, 
        static_url_path='',
        static_folder='static',
        template_folder='templates')


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/rules')
def rules():
    return render_template('rules.html')



# @app.route('/insert')
# def insert(first, last):
#     cnx = mysql.connector.connect(user='webapp', password='novovoom1web', host='db', database='NovoVoom')
#     cursor = cnx.cursor(buffered=True)

#     query = "INSERT into Players (first, last) VALUES ("+ first +", "+ last +");"

#     cursor.execute(query)
# 
#     cnx.commit()

#     return "Successfully Inserted Matt Lepinski"

app.run(host='0.0.0.0', port=5000)