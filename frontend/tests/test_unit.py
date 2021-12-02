from flask import url_for
from flask_testing import TestCase
from application import app
from application.routes import backend_host
import requests_mock

test_team = {
                "id": 1,
                "name": "team a",
                "league": "league a"
            }

test_player = {
                "id": 1,
                "name": "player a",
                "position": "any"
            }
class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

class TestViews(TestBase):
    # Test whether we get a successful response from our routes
    def test_home_get(self):
        with requests_mock.Mocker() as m:
            all_teams = { "teams": [test_team] }
            m.get(f"http://{backend_host}/read/allTeams", json=all_teams)
            response = self.client.get(url_for('home'))
            self.assert200(response)
    
    def test_create_team(self):
        response = self.client.get(url_for('create_team'))
        self.assert200(response)

    def test_update_team(self):
        with requests_mock.Mocker() as m:
            m.get(f"http://{backend_host}/update/team/name/{id}", json=test_team)
            response = self.client.get(url_for('update_team_name', id=1))
            self.assert200(response)

class TestRead(TestBase):

    def test_read_home_teams(self):
        with requests_mock.Mocker() as m:
            all_teams = { "teams": [test_team] }
            m.get(f"http://{backend_host}/read/allTeams", json=all_teams)
            response = self.client.get(url_for('home'))
            self.assertIn(b"team a", response.data)

class TestCreate(TestBase):

    def test_create_team(self):
        with requests_mock.Mocker() as m:
            all_teams = { "teams": 
                [
                    test_team,
                    {
                        "id": 1,
                        "name": "team a",
                        "league": "league a"
                    }
                ] 
            }
            m.post(f"http://{backend_host}/create/team", text="Test response")
            m.get(f"http://{backend_host}/read/allTeams", json=all_teams)
            response = self.client.post(
                url_for('create_team'),
                json={"name": "team a"},
                follow_redirects=True
            )
            self.assertIn(b"team a", response.data)

    def test_create_player(self):
        with requests_mock.Mocker() as m:
            all_players = { "players": 
                [
                    test_player,
                    {
                        "id": 1,
                        "name": "player a",
                        "position": "any"
                    }
                ] 
            }
            m.post(f"http://{backend_host}/create/player", text="Test response")
            m.get(f"http://{backend_host}/read/allPlayers", json=all_players)
            response = self.client.post(
                url_for('create_player'),
                json={"name": "player a"},
                follow_redirects=True
            )
            self.assertIn(b"player a", response.data)
    
class TestUpdate(TestBase):

    def test_update_team_name(self):
        with requests_mock.Mocker() as m:
            m.get(f"http://{backend_host}/read/team/{id}", json=test_team)
            m.put(f"http://{backend_host}/update/team/name/{id}", text="Test response")
            test_team["name"] = "team a"
            m.get(f"http://{backend_host}/read/allTeams", json={ "teams": [test_team] })
            response = self.client.post(
                url_for('update_team_name', id=1),
                data={"name": "team a"},
                follow_redirects=True
            )
            self.assertIn(b"team a", response.data)
    
    def test_update_team_league(self):
        with requests_mock.Mocker() as m:
            m.get(f"http://{backend_host}/read/team/{id}", json=test_team)
            m.put(f"http://{backend_host}/update/team/name/{id}", text="Test response")
            test_team["league"] = "league a"
            m.get(f"http://{backend_host}/read/allTeams", json={ "teams": [test_team] })
            response = self.client.post(
                url_for('update_team_league', id=1),
                data={"league": "league a"},
                follow_redirects=True
            )
            self.assertIn(b"league a", response.data)

    def test_update_player_name(self):
        with requests_mock.Mocker() as m:
            m.get(f"http://{backend_host}/read/team/{id}", json=test_player)
            m.put(f"http://{backend_host}/update/player/name/{id}", text="Test response")
            test_player["name"] = "player a"
            m.get(f"http://{backend_host}/read/allPlayers", json={ "players": [test_player] })
            response = self.client.post(
                url_for('update_player_name', id=1),
                data={"name": "player a"},
                follow_redirects=True
            )
            self.assertIn(b"player a", response.data)
        

class TestDelete(TestBase):

    def test_delete_team(self):
        with requests_mock.Mocker() as m:
            m.delete(f"http://{backend_host}/delete/team/{id}")
            m.get(f"http://{backend_host}/read/allTeams", json={ "teams": [] })
            response = self.client.get(
                url_for('delete_team', id=1),
                follow_redirects=True
            )
            self.assertNotIn(b"team a", response.data)

    def test_delete_player(self):
        with requests_mock.Mocker() as m:
            m.delete(f"http://{backend_host}/delete/player/{id}")
            m.get(f"http://{backend_host}/read/allPlayers", json={ "players": [] })
            response = self.client.get(
                url_for('delete_player', id=1),
                follow_redirects=True
            )
            self.assertNotIn(b"player a", response.data)