from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TeamForm(FlaskForm):
    name = StringField("Team Name", validators=[DataRequired()])
    league = StringField("League")
    submit = SubmitField("Add Team")