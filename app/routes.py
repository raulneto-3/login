from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import User
from flask import Blueprint

# Cria um Blueprint para as rotas
main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and user.verify_password(password):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Login falhou. Verifique seu email e senha.')

    return render_template('login.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))

    if request.method == 'POST':
        email = request.form['email']
        cpf_cnpj = request.form['cpf_cnpj']
        nome = request.form['nome']
        password = request.form['password']
        user = User(email=email, cpf_cnpj=cpf_cnpj, nome=nome, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Registro realizado com sucesso!')
        return redirect(url_for('main.login'))

    return render_template('register.html')

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@main.route('/users')
@login_required
def users():
    if not current_user.is_admin:
        return redirect(url_for('main.dashboard'))

    all_users = User.query.all()
    return render_template('users.html', users=all_users)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))