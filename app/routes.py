from app import app, db
from flask import render_template, flash, redirect
from app.forms import SignUp, LogIn, postForm
from app.models import Logins, Posts
from flask_login import current_user, login_user, login_required, logout_user
import time
from werkzeug.utils import secure_filename


def index():
    return render_template("index.html", current_user=current_user) 
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
            time.sleep(3)
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
        return redirect('/')
    return render_template('signup.html', form=form)

@app.route('/createPost', methods=['GET','POST'])
@login_required
def createPost():
    form = postForm()
    if form.validate_on_submit():
        imageA_data = form.imageA.data
        imageB_data = form.imageB.data
        imageC_data = form.imageC.data
        filenameA = None
        filenameB = None
        filenameC = None
        if form.imageA.data:
            filenameA = secure_filename(imageA_data.filename)
            imageA_data.save('app/static/'+filenameA)
        if form.imageB.data:
            filenameB = secure_filename(imageB_data.filename)
            imageB_data.save('app/static/'+filenameB)

        if form.imageC.data:
            filenameC = secure_filename(imageC_data.filename)
            imageC_data.save('app/static/'+filenameC)


        posts = Posts(title = form.title.data, description = form.description.data, city = form.city.data,ImageA = filenameA, ImageB= filenameB, ImageC=filenameC, author = current_user, email = form.email.data, phone = form.phone.data) 
        db.session.add(posts)
        db.session.commit()
        return redirect('/index')

        
    return render_template("post.html", form=form)
@app.route('/post/<int:id>', methods=['GET'])
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
@app.route('/')
@app.route('/index')
def tampa():
    posts = Posts.query.filter(Posts.city == "tampa").all()
    return render_template("city.html", posts = posts, city = "Tampa")       
@app.route('/miami')
def miami():
    posts = Posts.query.filter(Posts.city == "miami").all()
    return render_template("city.html", posts = posts, city = "Miami")   
@app.route('/orlando')
def orlando():
    posts = Posts.query.filter(Posts.city == "orlando").all()
    return render_template("city.html", posts = posts, city = "Orlando")      
@app.route('/logout')
def logout():
    logout_user()
    return redirect('/index')
     
        
    
    