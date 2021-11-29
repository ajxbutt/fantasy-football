from application import app, db
from application.models import Teams
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

# @app.route('/complete/task/<int:id>', methods=['PUT'])
# def complete_task(id):
#     task = Tasks.query.get(id)
#     task.completed = True
#     db.session.commit()
#     return Response(f"Task (ID:{id}) completed.")

# @app.route('/incomplete/task/<int:id>', methods=['PUT'])
# def incomplete_task(id):
#     task = Tasks.query.get(id)
#     task.completed = False
#     db.session.commit()
#     return Response(f"Task (ID:{id}) incomplete.")