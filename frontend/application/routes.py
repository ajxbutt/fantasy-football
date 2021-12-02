from application import app
from application.forms import TeamForm, PlayerForm
from flask import render_template, request, redirect, url_for, jsonify
import requests

backend_host = "fantasy-football-backend:5000"

@app.route('/')
@app.route('/home')
def home():
    all_teams = requests.get(f"http://{backend_host}/read/allTeams").json()
    app.logger.info(f"Teams: {all_teams}")
    return render_template('index.html', title="Home", all_teams=all_teams["teams"])

@app.route('/create/team', methods=['GET','POST'])
def create_team():
    form = TeamForm()

    if request.method == "POST":
        response = requests.post(f"http://{backend_host}/create/team", json={"name": form.name.data, "league": form.league.data})
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for('home'))

    return render_template("create_team.html", title="Create a new team", form=form)

@app.route('/create/player', methods=['GET','POST'])
def create_player():
    form = PlayerForm()
    # all_teams = requests.get(f"http://{backend_host}/read/allTeams").json()
    # for team in all_teams["teams"]:
    #     form.team.choices.append((team["id"], team["name"]))

    if request.method == "POST":
        response = requests.post(f"http://{backend_host}/create/player/1", json={"name": form.name.data, "position": form.position.data}) #, "team_id": form.team.data})
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for('home'))

    return render_template("create_player.html", title="Create a new player", form=form)

@app.route('/update/team/name/<int:id>', methods=['GET','POST'])
def update_team_name(id):
    form = TeamForm()
    team = requests.get(f"http://{backend_host}/read/team/{id}").json()
    app.logger.info(f"Team: {team}")

    if request.method == "POST":
        response = requests.put(f"http://{backend_host}/update/team/name/{id}", json={"name": form.name.data})
        return redirect(url_for('home'))

    return render_template('update_team.html', team=team, form=form)

@app.route('/update/team/league/<int:id>', methods=['GET','POST'])
def update_team_league(id):
    form = TeamForm()
    team = requests.get(f"http://{backend_host}/read/team/{id}").json()
    app.logger.info(f"Team: {team}")

    if request.method == "POST":
        response = requests.put(f"http://{backend_host}/update/team/league/{id}", json={"league": form.league.data})
        return redirect(url_for('home'))

    return render_template('update_league.html', team=team, form=form)

@app.route('/delete/team/<int:id>')
def delete_team(id):
    response = requests.delete(f"http://{backend_host}/delete/team/{id}")
    app.logger.info(f"Response: {response.text}")
    return redirect(url_for('home'))






@app.route('/update/player/name/<int:id>', methods=['GET','POST'])
def update_player_name(id):
    form = PlayerForm()
    player = requests.get(f"http://{backend_host}/read/player/{id}").json()
    app.logger.info(f"Player: {player}")

    if request.method == "POST":
        response = requests.put(f"http://{backend_host}/update/player/name/{id}", json={"name": form.name.data})
        return redirect(url_for('home'))

    return render_template('update_player.html', player=player, form=form)

@app.route('/delete/player/<int:id>')
def delete_player(id):
    response = requests.delete(f"http://{backend_host}/delete/player/{id}")
    app.logger.info(f"Response: {response.text}")
    return redirect(url_for('home'))