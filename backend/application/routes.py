from application import app, db
from application.models import Teams, Players
from flask import render_template, request, redirect, url_for, Response, jsonify

@app.route('/create/team', methods=['POST'])
def create_team():
        package = request.json
        new_team = Teams(name=package["name"], league=package["league"])
        db.session.add(new_team)
        db.session.commit()
        return Response(f"Added team with name: {new_team.name}", mimetype='text/plain')

@app.route('/read/allTeams', methods=['GET'])
def read_teams():
    all_teams = Teams.query.all()
    teams_dict = {"teams": []}
    for team in all_teams:
        teams_dict["teams"].append(
            {
                "id": team.id,
                "name": team.name,
                "league": team.league,
            }
        )
    return jsonify(teams_dict)

@app.route('/read/team/<int:id>', methods=['GET'])
def read_team(id):
    team = Teams.query.get(id)
    teams_dict = {
                "name": team.name,
                "league": team.league,
                }
    return jsonify(teams_dict)

@app.route('/update/team/name/<int:id>', methods=['PUT'])
def update_team_name(id):
    package = request.json
    team = Teams.query.get(id)
    team.name = package["name"]
    db.session.commit()
    return Response(f"Updated team (ID: {id}) with name: {team.name}", mimetype='text/plain')

@app.route('/update/team/league/<int:id>', methods=['PUT'])
def update_team_league(id):
    package = request.json
    team = Teams.query.get(id)
    team.league = package["league"]
    db.session.commit()
    return Response(f"Updated team (ID: {id}) with league: {team.league}", mimetype='text/plain')

@app.route('/delete/team/<int:id>', methods=['DELETE'])
def delete_team(id):
    team = Teams.query.get(id)
    db.session.delete(team)
    db.session.commit()
    return Response(f"Deleted team (ID: {id})", mimetype='text/plain')


# FOOTBALL PLAYERS

@app.route('/create/player', methods=['POST'])
def create_player():
        package = request.json
        new_player = Players(name=package["name"], team_id=package["team_id"])
        db.session.add(new_player)
        db.session.commit()
        return Response(f"Added player with name: {new_player.name}", mimetype='text/plain')

@app.route('/read/allPlayers', methods=['GET'])
def read_players():
    all_players = Players.query.all()
    players_dict = {"players": []}
    for player in all_players:
        players_dict["players"].append(
            {
                "id": player.id,
                "name": player.name,
            }
        )
    return jsonify(players_dict)

@app.route('/read/player/<int:id>', methods=['GET'])
def read_player(id):
    player = Players.query.get(id)
    players_dict = {
                "name": player.name,
                }
    return jsonify(players_dict)

@app.route('/update/player/name/<int:id>', methods=['PUT'])
def update_player_name(id):
    package = request.json
    player = Players.query.get(id)
    player.name = package["name"]
    db.session.commit()
    return Response(f"Updated player (ID: {id}) with name: {player.name}", mimetype='text/plain')

@app.route('/delete/player/<int:id>', methods=['DELETE'])
def delete_player(id):
    player = Players.query.get(id)
    db.session.delete(player)
    db.session.commit()
    return Response(f"Deleted player (ID: {id})", mimetype='text/plain')