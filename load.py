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

class ProductForm(FlaskForm):
    names = StringField("Product name", validators=[DataRequired(message="Enter Product Name please!"), Length(min=4)])
    quantity  = IntegerField("Quantity", validators=[DataRequired(message="Enter Quantity"), NumberRange(min=1, max=1000, message="Quantity must be between 1 and 1000")])
    price  = IntegerField("Price", validators=[DataRequired(message="Enter Price"), NumberRange(min=1, max=1000, message="Price must be between 1 and 1000")])
