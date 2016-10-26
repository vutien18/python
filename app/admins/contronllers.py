from _ast import mod
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from flask import Blueprint,render_template,url_for,flash,redirect,request,session,jsonify
from app.admins.models import User
from app.admins.forms import SigupForm
from  app.admins.forms import LoginForm
model_admin = Blueprint('admin', __name__, url_prefix='/admin')
import logging


@model_admin.route('/')
def index():
    if 'email' not in session:
        return redirect(url_for('admin.login'))
    user = User.query.filter_by(email=session['email']).first()
    if user is None:
            return redirect(url_for('admin.login'))
    return render_template('admin/index.html',lists=User.query.all())

@model_admin.route('/add/',methods=['GET', 'POST'])
def add():
    form = SigupForm()
    if request.method == 'POST':
        logging.error('_____________')
        logging.error(request.form)
        if not form.validate():
            logging.error(form.errors)
            return render_template('admin/index.html',form=form)
        else:
            new_user = User(form.username.data, form.email.data, form.password.data,form.role.data)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('admin.index'))
    elif request.method == 'GET':
        return render_template('admin/add.html', form=form)
@model_admin.route('/delete',methods=['POST'])
def delete():
     id=request.form['ids']
     User.query.filter_by(id=id).delete()
     db.session.commit()
     return redirect(url_for('admin.index'))
@model_admin.route('/edit/<int:id>',methods=['GET','POST'])
def edit(id):
    # admin = User.query.filter_by(username == 'admin').update(dict(email='my_new_email@example.com')))
    # db.session.commit()
    admin = User.query.filter_by(id=id).first()
    username=request.form['username']
    email=request.form['email']
    password=request.form['password']
    role=request.form['role']
    admin.email = 'my_new_email@example.com'
    db.session.commit()
    return render_template('admin/edit.html',info=User.query.filter_by(id=id).first())
@model_admin.route('/login/',methods=['GET','POST'])
def login():
        form = LoginForm()
        if request.method=='POST':
            user = User.query.filter_by(username=form.username.data).first()
            if user and check_password_hash(user.password, form.password.data):
                session['email'] = user.email
                flash('Welcome %s' % user.username)
                return redirect(url_for('admin.index'))
            flash('Wrong email or password', 'error-message')
        return render_template("admin/login.html", form=form)
@model_admin.route('/logout')
def logout():
    if 'email' not in session:
        return redirect('admin.login')
    session.pop('email', None)
    redirect('admin.index')





