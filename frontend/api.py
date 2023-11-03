from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
import random
import mysql.connector

app = Flask(__name__, 
        static_url_path='/static',
        static_folder='static',
        template_folder='templates')

game_id = ''
for i in range(15):
    game_id += str(random.randint(0, 9))

app.config['SESSION_TYPE'] = 'filesystem'

app.secret_key = game_id

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/howtoplay')
def howtoplay():
    return render_template('howtoplay.html')

@app.route('/pregame')
def pregame():
    return render_template('pregame.html')

@app.route('/scoreboard')
def scoreboard():
    return render_template('scoreboard.html')



# @app.route('/insert')
# def insert(name):
#     cnx = mysql.connector.connect(user='webapp', password='masterminds1', host='db', database='MasterMinds')
#     cursor = cnx.cursor(buffered=True)

#     query = "INSERT into PlayerData (name) VALUES ("+ name +");"

#     cursor.execute(query)

#     cnx.commit()

#     return "Welcome, " + name

@app.route('/lookup')
def direct_form():
    return render_template('lookup.html')

@app.route('/player', methods = ['POST'])
def lookup():
    cnx = mysql.connector.connect(user='webapp', password='masterminds1', host='db', database='MasterMinds')
    cursor = cnx.cursor(buffered=True)
    form_data = request.form
    player_name = form_data['name']
    
    query = "SELECT name, gameID, moves, attempts, gameComplete FROM PlayerData WHERE name = '" + player_name + "'";
    
    q_list = query.split(';')
    for q in q_list:
        if (len(q) > 2):
            cursor.execute(q) 

    cnx.commit()

    output_str = ""
    for data in cursor:
        for item in data:
            output_str = output_str + str(item) + ",   "
        output_str = output_str + "\n"

    return render_template('player.html', output = output_str)

app.run(host='0.0.0.0', port=5500)