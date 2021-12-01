from application import app, db
from application.models import Teams, Players
from flask import render_template, request, redirect, url_for, Response, jsonify

@app.route('/create/team', methods=['POST'])
def create_team():
        json = request.json
        new_team = Teams(name=json["name"], league=json["league"])
        db.session.add(new_team)
        db.session.commit()
        return Response(f"Added team with name: {new_team.name}", mimetype='text/plain')

@app.route('/create/player/<int:team_id>', methods=['POST'])
def create_player(team_id):
        json = request.json
        new_player = Players(name=json["name"], team_id=team_id)
        db.session.add(new_player)
        db.session.commit()
        return Response(f"Added player with name: {new_player.name}", mimetype='text/plain')

@app.route('/read/allTeams', methods=['GET'])
def read_teams():
    all_teams = Teams.query.all()
    json = {"teams": []}
    for team in all_teams:
        players = []
        for player in team.players:
            players.append(
                {
                    "id": player.id,
                    "name": player.name,
                    "team_id": player.team_id,
                }
            )
        json["teams"].append(
            {
                "id": team.id,
                "name": team.name,
                "league": team.league,
                "players": players
            }
        )
    return jsonify(json)

@app.route('/read/allPlayers', methods=['GET'])
def read_players():
    all_players = Players.query.all()
    json = {"players": []}
    for player in all_players:
        json["players"].append(
            {
                "id": player.id,
                "name": player.name,
                "team_id": player.team_id,
            }
        )
    return jsonify(json)

@app.route('/read/team/<int:id>', methods=['GET'])
def read_team(id):
    team = Teams.query.get(id)
    json = {
                "name": team.name,
                "league": team.league,
                }
    return jsonify(json)

@app.route('/read/team/<int:id>/players', methods=["GET"])
def get_players(id):
    players = Teams.query.get(id).players
    json = {"players": []}
    for player in players:
        json["players"].append(
            {
                "id": player.id,
                "name": player.name,
                "team_id": player.team_id,
            }
        )
    return jsonify(json)

@app.route('/update/team/name/<int:id>', methods=['PUT'])
def update_team_name(id):
    json = request.json
    team = Teams.query.get(id)
    team.name = json["name"]
    db.session.commit()
    return Response(f"Updated team (ID: {id}) with name: {team.name}", mimetype='text/plain')

@app.route('/update/team/league/<int:id>', methods=['PUT'])
def update_team_league(id):
    json = request.json
    team = Teams.query.get(id)
    team.league = json["league"]
    db.session.commit()
    return Response(f"Updated team (ID: {id}) with league: {team.league}", mimetype='text/plain')

@app.route('/delete/team/<int:id>', methods=['DELETE'])
def delete_team(id):
    team = Teams.query.get(id)
    db.session.delete(team)
    db.session.commit()
    return Response(f"Deleted team (ID: {id})", mimetype='text/plain')

@app.route('/delete/player/<int:id>', methods=['DELETE'])
def delete_player(id):
    player = Players.query.get(id)
    db.session.delete(player)
    db.session.commit()
    return Response(f"Deleted player (ID: {id})", mimetype='text/plain')

# FOOTBALL PLAYERS

# @app.route('/create/player', methods=['POST'])
# def create_player():
#         package = request.json
#         new_player = Players(name=package["name"], team_id=package["team_id"])
#         db.session.add(new_player)
#         db.session.commit()
#         return Response(f"Added player with name: {new_player.name}", mimetype='text/plain')

# @app.route('/create/player/<int:team_id>', methods=['POST'])
# def create_player(team_id):
#         package = request.json
#         new_player = Players(name=package["name"], team_id=team_id)
#         db.session.add(new_player)
#         db.session.commit()
#         return Response(f"Added player with name: {new_player.name}", mimetype='text/plain')

# @app.route('/read/allPlayers', methods=['GET'])
# def read_players():
#     all_players = Players.query.all()
#     players_dict = {"players": []}
#     for player in all_players:
#         players_dict["players"].append(
#             {
#                 "id": player.id,
#                 "name": player.name,
#                 "team_id": player.team_id,
#             }
#         )
#     return jsonify(players_dict)

# @app.route('/read/player/<int:id>', methods=['GET'])
# def read_player(id):
#     player = Players.query.get(id)
#     players_dict = {
#                 "name": player.name,
#                 "team_id": player.team_id,
#                 }
#     return jsonify(players_dict)

# @app.route('/update/player/name/<int:id>', methods=['PUT'])
# def update_player_name(id):
#     package = request.json
#     player = Players.query.get(id)
#     player.name = package["name"]
#     db.session.commit()
#     return Response(f"Updated player (ID: {id}) with name: {player.name}", mimetype='text/plain')

# @app.route('/delete/player/<int:id>', methods=['DELETE'])
# def delete_player(id):
#     player = Players.query.get(id)
#     db.session.delete(player)
#     db.session.commit()
#     return Response(f"Deleted player (ID: {id})", mimetype='text/plain')