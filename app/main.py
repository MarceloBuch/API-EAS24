from flask import Flask, jsonify
from models import Player

app = Flask(__name__)


@app.route('/players/id/<id_player>')
def get_player_by_id(id_player):
    results = Player.query.filter_by(id = id_player)
    for r in results:
        return r.__repr__() 


@app.route('/players/nation/<nation_name>', methods = ['GET'])
def get_players_by_nation(nation_name):
    result_list = []  
    list = Player.query.filter(Player.Nation.like(f'%{nation_name}%')).all()
    for r in list:
        result_list.append(r.__repr__())
    return jsonify(result_list)
     

@app.route('/players/position/<position>', methods = ['GET'])
def get_players_by_position(position):
    result_list = []  
    list = Player.query.filter(Player.Position.like(f'%{position}%')).all()
    for r in list:
        result_list.append(r.__repr__())
    return jsonify(result_list)
    

@app.route('/players/club/<club_name>', methods = ['GET'])
def get_players_by_club(club_name):
    result_list = []  
    list = Player.query.filter(Player.Club.like(f'%{club_name}%')).all()
    for r in list:
        result_list.append(r.__repr__())
    return jsonify(result_list)
    

@app.route('/players/best', methods = ['GET'])
def get_best_players():
    result_list = []  
    list = Player.query.order_by(Player.Overall.desc()).limit(50).all()
    for r in list:
        result_list.append(r.__repr__())
    return jsonify(result_list)
    

if __name__ == '__main__':
    app.run(debug=True)