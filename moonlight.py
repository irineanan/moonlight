from flask import Flask,render_template,flash,session,redirect,url_for
from load import MyForm, LoginForm
from user_model import User, Product
from flask_bcrypt import generate_password_hash, check_password_hash
from peewee import OperationalError
app = Flask(__name__)
app.secret_key="AsdFghJklMnOp"


@app.route('/', methods=("GET", "POST"))
def index():
    form = MyForm()
    if form.validate_on_submit():
       #everything is okay
       names = form.names.data
       email = form.email.data
       age = form.age.data
       password = form.password.data
       print("Names {0} Email {1} Age {2}".format(names,email,age))
       password = generate_password_hash(password)
       User.create(names=names, email=email, age=age, password=password)
    return render_template("index.html", form=form)

@app.route("/login",methods=("GET", "POST"))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        try:
         user = User.get(User.email == email)
         check = check_password_hash(user.password, password)
         print(check)
         if check:
             print("Logged in successfully!")
             session ["names"] = user.names
             session ["id"] = user.id
             return redirect(url_for("products"))
         else:
             flash("Wrong username or password!")
        except Exception:
             print("User does not exist")
             flash("Wrong username or password")
    return render_template("login.html", form=form)

@app.route("/products")
def products():
    if "names" not in session:
        return redirect(url_for("login"))
    else:
        products=Product.select()
        return render_template("products.html", names = session["names"], products=products)


@app.route("/logout")
def logout():
    session.pop("names")
    session.pop("id")
    return redirect(url_for("login"))


# if __name__ == '__main__':
#
#     try:
#         Product.create_table()
#     except OperationalError:
#         pass
#     try:
#      User.create_table()
#     except OperationalError:
#         pass
#     app.run(host="0.0.0.0", port=8000)
