from app import db
from flask import Blueprint,render_template,url_for,flash,redirect,request,session
from app.category.models import category
from app.category.forms import CategoryForm
import logging
model_category = Blueprint('category', __name__, url_prefix='/category')
@model_category.route('/add/',methods=['GET', 'POST'])
def add():
    form = CategoryForm()
    if request.method == 'POST':
        if not form.validate():
            return render_template('category/index.html',form=form)
        else:
            newcategory = category(form.name.data, form.category_id.data, form.postion.data)
            db.session.add(newcategory)
            db.session.commit()
            return redirect(url_for('category.index'))
    elif request.method == 'GET':
        return render_template('category/add.html', form=form,infos=category.query.all())

@model_category.route('/')
def index():
    return render_template('category/index.html',listcategorys=category.query.all())

