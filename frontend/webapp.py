from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
import random
import mysql.connector
import game_logic
from flask import jsonify

app = Flask(__name__, 
        static_url_path='/static',
        static_folder='static',
        template_folder='templates')

game_id = ''
for i in range(15):
    game_id += str(random.randint(0, 9))

app.config['SESSION_TYPE'] = 'filesystem'

app.secret_key = game_id

# loads the home page
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


# loads the "how to play" page for general game rules and instructions
@app.route('/howtoplay')
def howtoplay():
    return render_template('howtoplay.html')

# loads game creation page, for starting a new game or continuing an unfinished game
@app.route('/pregame')
def creategame():
    return render_template('pregame.html')

# Loads the game page, for playing a unique game of Mastermind
@app.route('/game')
def game():
    return render_template('game.html')

# Retrieves data about each player from the DB, transforms it into a readable format and renders the scoreboard page
# Implemented by Aidan Roessler from team Vaas
@app.route('/scoreboard')
def scoreboard():
    # TODO Rotate password and store in an environment variable to not expose it to the FE
    cnx = mysql.connector.connect(user='webapp', password='masterminds1', host='db', database='MasterMinds')
    cursor = cnx.cursor(buffered=True)
    
    query = "SELECT name, gameID, attempts FROM PlayerData WHERE gameComplete = TRUE"
    
    cursor.execute(query) 

    cnx.commit()

    results = cursor.fetchall()
    columns = cursor.column_names
    
    # Create a list of dictionaries where in each dictionary each key corresponds
    # to a column, (eg. Name) and each value for that key is the value for that row 
    list_of_players = []
    for row in results:
        row_dict = {}
        for i in range(len(columns)):
            column_name = columns[i]
            column_value = row[i]
            row_dict[column_name] = column_value
        list_of_players.append(row_dict)  

    cursor.close()
    cnx.close()

    return render_template('scoreboard.html', list_of_players = list_of_players)

# This loads a test page to make sure the HTML form of the player's guess
# is correct and can be parsed for the game logic
@app.route('/testdisplay', methods = ['GET'])
def testdisplay():
    playerguess = []
    num = 1
    for i in request.args:
        playerguess.append(request.args.get("color" + str(num)))
        num += 1
    
    cur_game = game_logic.guess_checker(playerguess)
    # guess = jsonify(cur_game)
    if cur_game == 0:
        return render_template('win.html')
    return render_template('testdisplay.html', playerguess=cur_game)

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

# @app.route('/player', methods = ['POST'])
# def lookup():
#     cnx = mysql.connector.connect(user='webapp', password='masterminds1', host='db', database='MasterMinds')
#     cursor = cnx.cursor(buffered=True)
#     form_data = request.form
#     player_name = form_data['name']
    
#     query = "SELECT name, gameID, moves, attempts, gameComplete FROM PlayerData WHERE name = '" + player_name + "'";
    
#     q_list = query.split(';')
#     for q in q_list:
#         if (len(q) > 2):
#             cursor.execute(q) 

#     cnx.commit()

#     output_str = ""
#     for data in cursor:
#         for item in data:
#             output_str = output_str + str(item) + ",   "
#         output_str = output_str + "\n"

#     return render_template('player.html', output = output_str)

app.run(host='0.0.0.0', port=5500)