# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

# Import password / encryption helper tools
from werkzeug.security import check_password_hash, generate_password_hash

# Import the database object from the main app module
# Import module forms
from app.mod_auth.forms import LoginForm
from app.mod_auth.forms import SignForm
# Import module models (i.e. User)
from app.mod_auth.models import User
from app import db
# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

# Set the route and accepted methods
@mod_auth.route('/signin/', methods=['GET', 'POST'])
def signin():
    # If sign in form is submitted
    form = LoginForm(request.form)

    # Verify the sign in form
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user and check_password_hash(user.password, form.password.data):

            session['user_id'] = user.id

            flash('Welcome %s' % user.name)

            return redirect(url_for('auth.home'))

        flash('Wrong email or password', 'error-message')

    return render_template("auth/signin.html", form=form)
@mod_auth.route('/show')
def show():
    return render_template('admin/listAdmin.html',admins=User.query.all())
# @mod_auth.route('/register/', methods=['GET', 'POST'])
# def signup():
#     form = SignForm()
#     if request.method == 'POST':
#         if form.validate() == False:
#             return render_template('admin/signup.html', form=form)
#         else:
#             newuser = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
#             db.session.add(newuser)
#             db.session.commit()
#
#             session['email'] = newuser.email
#             return redirect(url_for('profile'))
#
#     elif request.method == 'GET':
#         return render_template('admin/signup.html', form=form)

# @mod_auth.route('/create',methods=['GET','POST'])
# def create():
#     form=LoginForm(request.form)
#     if form.validate_on_submit():
#         newuser=User(form.email.data,form.password.data)
#         db.session.add(newuser)
#         db.session.commit()
#         db.session['email']=newuser.email
#         return render_template('admin/listAdmin.html')
#     return render_template('admin/signup.html')
@mod_auth.route('/signup',methods=['GET','POST'])
def signup():
    form = SignForm()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('admin/signup.html', form=form)
        else:
            newuser = User(form.name.data,form.email.data, form.password.data)
            db.session.add(newuser)
            db.session.commit()
            # db.session['email']=newuser
            return redirect(url_for('profile'))
    elif request.method == 'GET':
        return render_template('admin/signup.html', form=form)
@mod_auth.route('/edit',methods=['GET','POST'])
def edit():
    form=SignForm()