# Importar bibliotecas
import os
import sqlite3
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# Configurações
DATABASE = 'flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# criar e inicializar a aplicação
app = Flask(__name__)
app.config.from_object(__name__)

# Conectar com banco de dados
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

# Inicializar o banco de dados
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# Incluir ações pré-requisições
@app.before_request
def before_request():
    g.db = connect_db()

# Incluir ações teardown-request
@app.teardown_request
def teardown_request(exception):
    g.db.close()

# Criar view show_entries
@app.route('/')
def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0],text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html',entries=entries)

# Criar view add_entry
@app.route('/add',methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title,text) values (?,?)',[request.form['title'],request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

# Criar view login
@app.route('/login',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error='Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error='Invalid password'
        else:
            session['logged_in']=True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html',error=error)

# Criar view logout
@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

if __name__ == '__main__':
    if not os.path.exists(app.config['DATABASE']):
        with app.app_context():
            init_db()
    app.run(debug=True,port=5000)