from app import app, db
from flask import render_template, flash, redirect
from app.forms import SignUp, LogIn
from app.models import Logins
from flask_login import current_user, login_user
import time
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
@app.route('/login', methods=['GET','POST'])
def login():
    form = LogIn()
    if form.validate_on_submit():
        user = Logins.query.filter_by(email=form.emails.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid! Check your login details')
            return redirect("/login")
        login_user(user)
        if current_user.is_authenticated:
            flash("Logged In!")
            return redirect('/index')
    return render_template('login.html', form=form)
        
        
       
       
@app.route('/signup', methods=['GET','POST'])
def register():
    form = SignUp()
    if form.validate_on_submit():
        user = Logins(OrgName = form.OrganizationName.data, email = form.emails.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congrats! Signed Up!")
    return render_template('signup.html', form=form)
@app.route('/tampa')
def tampa():
    return render_template("tampa.html")
