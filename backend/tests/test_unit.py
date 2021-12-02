from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Teams

test_team = {
                "id": 1,
                "name": "team a",
                "league": "league a",
            }
test_player = {
                "id": 1,
                "name": "player a",
                "position": "st",
            }

class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        # Will be called before every test
        db.create_all()
        db.session.add(Teams(name="team a"))
        db.session.commit()

    def tearDown(self):
        # Will be called after every test
        db.session.remove()
        db.drop_all()


class TestCreate(TestBase):

    def test_create_team(self):
        response = self.client.post(
            url_for('create_team'),
            json={"name": "team a", "league": None},
            follow_redirects=True
        )
        self.assertEquals(b"Added team with name: team a", response.data)
        self.assertEquals(Teams.query.get(1).name, "team a")

    def test_create_player(self, team_id):
        response = self.client.post(
            url_for('create_player'),
            json={"name": "team a", "position": "ST"},
            follow_redirects=True
        )
        self.assertEquals(b"Added team with name: team a", response.data)
        self.assertEquals(Teams.query.get(1).name, "team a")
    
class TestRead(TestBase):

    def test_read_all_teams(self):
        response = self.client.get(url_for('read_teams'))
        all_teams = { "teams": [{'id': 1, 'league': None, 'name':'team a', 'players':[]}] }
        self.assertEquals(all_teams, response.json)

    def test_read_all_players(self):
        response = self.client.get(url_for('read_players'))
        all_teams = { "teams": [{'id': 1, 'league': None, 'name':'team a', 'players':[]}] }
        self.assertEquals(all_teams, response.json)
    
    def test_read_team(self):
        response = self.client.get(url_for('read_team', id=1))
        json = {'league': None, 'name': 'team a'}
        self.assertEquals(test_team, response.json)

    def test_read_team_players(self):
        response = self.client.get(url_for('get_players'))
        all_teams = { "teams": [{'id': 1, 'league': None, 'name':'team a', 'players':[]}] }
        self.assertEquals(all_teams, response.json)

    def test_read_player(self):
        response = self.client.get(url_for('read_player'))
        all_teams = { "teams": [{'id': 1, 'league': None, 'name':'team a', 'players':[]}] }
        self.assertEquals(all_teams, response.json)

class TestUpdate(TestBase):

    def test_update_team(self):
        response = self.client.put(
            url_for('update_team_name', id=1),
            json={"name": "team a"}
        )
        self.assertEquals(b"Updated team (ID: 1) with name: team a", response.data)
        self.assertEquals(Teams.query.get(1).name, "team a")
    
    def test_update_league(self):
        response = self.client.put(
            url_for('update_team_league', id=1),
            json={"league": "league a"}
        )
        self.assertEquals(b"Updated team (ID: 1) with league: league a", response.data)
        self.assertEquals(Teams.query.get(1).league, "league a")
        
    def test_update_player_name(self):
        response = self.client.put(
            url_for('update_player_name', id=1),
            json={"name": "team a"}
        )
        self.assertEquals(b"Updated player (ID: 1) with name: team a", response.data)
        self.assertEquals(Teams.query.get(1).league, "league a")

class TestDelete(TestBase):

    def test_delete_team(self):
        response = self.client.delete(url_for('delete_team', id=1))
        self.assertEquals(b"Deleted team (ID: 1)", response.data)
        self.assertIsNone(Teams.query.get(1))

    def test_delete_player(self):
        response = self.client.delete(url_for('delete_player', id=1))
        self.assertEquals(b"Deleted player (ID: 1)", response.data)
        self.assertIsNone(Teams.query.get(1))