from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
import random
import mysql.connector

app = Flask(__name__, 
        static_url_path='',
        static_folder='static',
        template_folder='templates')

game_id = ''
for i in range(15):
    game_id += str(random.randint(0, 9))

app.config['SESSION_TYPE'] = 'filesystem'

app.secret_key = game_id

# def generate_game_id():
#     return 0 # temporary

# def create_game():
#     max_password_len = ""
#     max_password_attempts = ""
#     allow_repeats = False 
#     allow_empty_inputs = ""

#     game_id = ""

#     rules = []

#     return 0 # temporary



# #Creates a randomized list of colors to act as the game's password
# def password_generator(max_len, allow_repeats):
#     password = []
#     if(allow_repeats):
#         password = random.sample(COLOR_MASTER, max_len)
#     else:
#         for i in range(max_len):
#             password.append(random.choice(COLOR_MASTER))
    
#     return password
    


# def valid_moves(move, max_len):
#     pass

# def guess_checker():
#     pass

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