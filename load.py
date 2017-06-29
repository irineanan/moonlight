from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField
from wtforms.validators import Email, DataRequired, Length, NumberRange

class MyForm(FlaskForm):
    names = StringField("Names", validators=[DataRequired(message="Enter Names please!"), Length(min=4)])
    email = StringField("Email", validators=[DataRequired(message="Enter your email address please!"), Email(message="Invalid Email!")])
    age  = IntegerField("Age", validators=[DataRequired(message="Enter Age"), NumberRange(min=1, max=100, message="Age must be between 1 and 100")])
    password = PasswordField("Password", validators=[DataRequired(message="Enter Password"), Length(min=6)])

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(message="Enter your email address please!"),Email(message="Invalid Email!")])
    password = PasswordField("Password", validators=[DataRequired(message="Enter Password")])
