from flask import render_template, session, request, redirect, url_for, flash
from shop import app, db, bcrypt
from .adm_form import RegistrationForm, LoginForm
from .adm_db_form import User
from shop.products.pro_db_form import Addproduct, Category, Brand

@app.route('/admin')
def admin():
    products = Addproduct.query.all()
    return render_template('admin/index.html', title='Control Page', products=products)

@app.route('/brands')
def brands():
    brands = Brand.query.order_by(Brand.id.desc()).all()
    return render_template('admin/brand.html', title='Бренд', brands=brands)


@app.route('/categories')
def categories():
    categories = Category.query.order_by(Category.id.desc()).all()
    return render_template('admin/brand.html', title='Категории', categories=categories)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, username=form.username.data, email=form.email.data,
                    password=hash_password)
        db.session.add(user)
        flash(f'Добро пожаловал {form.name.data} на наш сайт. Спасибо за вашу регистрацию', 'success')
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('admin/register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'Добро пожаловать {form.email.data}, Вы успешно вошли', 'success')
            return redirect(url_for('admin'))
        else:
            flash(f'Неверный пароль и почта', 'success')
            return redirect(url_for('login'))
    return render_template('admin/login.html', title='Вход', form=form)