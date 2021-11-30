from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Teams

test_team = {
                "id": 1,
                "name": "Run unit tests",
                "league": "Run unit tests",
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
        db.session.add(Teams(name="Run unit tests"))
        db.session.commit()

    def tearDown(self):
        # Will be called after every test
        db.session.remove()
        db.drop_all()

class TestRead(TestBase):

    def test_read_all_teams(self):
        response = self.client.get(url_for('read_teams'))
        all_teams = { "teams": [team_teams] }
        self.assertEquals(all_teams, response.json)
    
    def test_read_team(self):
        response = self.client.get(url_for('read_team', id=1))
        self.assertEquals(test_team, response.json)

class TestCreate(TestBase):

    def test_create_team(self):
        response = self.client.post(
            url_for('create_team'),
            json={"description": "Testing create functionality"},
            follow_redirects=True
        )
        self.assertEquals(b"Added team with name: Testing create functionality", response.data)
        self.assertEquals(Teams.query.get(2).name, "Testing create functionality")
    
class TestUpdate(TestBase):

    def test_update_team(self):
        response = self.client.put(
            url_for('update_team_name', id=1),
            json={"name": "Testing update functionality"}
        )
        self.assertEquals(b"Updated team (ID: 1) with name: Testing update functionality", response.data)
        self.assertEquals(Teams.query.get(1).name, "Testing update functionality")
    
    def test_update_league(self):
        response = self.client.put(
            url_for('update_team_league', id=1),
            json={"league": "Testing update functionality"}
        )
        self.assertEquals(b"Updated team (ID: 1) with league: Testing update functionality", response.data)
        self.assertEquals(Teams.query.get(1).league, "Testing update functionality")
        

class TestDelete(TestBase):

    def test_delete_team(self):
        response = self.client.delete(url_for('delete_team', id=1))
        self.assertEquals(b"Deleted team with ID: 1", response.data)
        self.assertIsNone(Teams.query.get(1))