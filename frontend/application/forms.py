from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class TeamForm(FlaskForm):
    name = StringField("Team Name", validators=[DataRequired()])
    league = StringField("League")
    submit = SubmitField("Submit")

class PlayerForm(FlaskForm):
    name = StringField("Player Name", validators=[DataRequired()])
    position = StringField("Position", validators=[DataRequired()])
    submit = SubmitField("Submit")