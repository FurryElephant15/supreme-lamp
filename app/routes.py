from app import app, db
from flask import render_template, flash, redirect
from app.forms import SignUp, LogIn, postForm
from app.models import Logins, Posts
from flask_login import current_user, login_user, login_required, logout_user
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

@app.route('/createPost', methods=['GET','POST'])
@login_required
def createPost():
    form = postForm()
    if form.validate_on_submit():
        imageA_data = None
        imageB_data = None
        imageC_data = None

        if form.imageA.data:
            imageA_data = form.imageA.data.read()
        if form.imageB.data:
            imageB_data = form.imageB.data.read()
        if form.imageC.data:
            imageC_data = form.imageC.data.read()

        posts = Posts(title = form.title.data, description = form.description.data, city = form.city.data,ImageA = imageA_data, ImageB= imageB_data, ImageC=imageC_data, author = current_user, email = form.email.data, phone = form.phone.data) 
        db.session.add(posts)
        db.session.commit()
    return render_template("post.html", form=form)
@app.route('/post/<int:id>')
def renderPost(id):
    post = Posts.query.get(id)
    title = post.title
    description = post.description
    ImageA=post.ImageA
    ImageB=post.ImageB
    ImageC=post.ImageC
    author_name = post.author.OrgName 
    email = post.email
    phone = post.phone
    return render_template("renderPost.html", title = title, description = description,ImageA=ImageA, ImageB=ImageB, ImageC=ImageC, author_name = author_name, email = email, phone = phone)
@app.route('/tampa')
def tampa():
    posts = Posts.query.filter(Posts.city == "tampa").all()
    return render_template("city.html", posts = posts)       
@app.route('/miami')
def miami():
    posts = Posts.query.filter(Posts.city == "miami").all()
    return render_template("city.html", posts = posts)   
@app.route('/orlando')
def orlando():
    posts = Posts.query.filter(Posts.city == "orlando").all()
    return render_template("city.html", posts = posts)      
@app.route('/logout')
def logout():
    logout_user()
    return redirect('/index')
     
        
    
    
