from app import db
from flask import Blueprint,render_template,url_for,flash,redirect,request,session
from app.category.models import category
from app.category.forms import CategoryForm
model_category = Blueprint('category', __name__, url_prefix='/category')


@model_category.route('/add/',methods=['GET','POST'])
def add():
    form = CategoryForm()
    if request.method == 'POST':
            newcategory = category(form.name.data, form.category_id.data, form.postion.data)
            db.session.add(newcategory)
            db.session.commit()
            return "[1] Create a new user [2] sign in the user [3] redirect to the user's profile"
    elif request.method == 'GET':
        return render_template('category/add.html', form=form)
@model_category.route('/')
def index():
    return render_template('category/index.html',listcategorys=category.query.all())


# @model_admin.route('/logout')
# def logout():
#     if 'email' not in session:
#         return redirect('admin.login')
#     session.pop('email', None)
#     redirect('admin.index')
#
#     def index():
#         if 'email' not in session:
#             return redirect(url_for('admin.login'))
#         user = User.query.filter_by(email=session['email']).first()
#         if user is None:
#             return redirect(url_for('admin.login'))
#         return render_template('admin/index.html', lists=User.query.all())