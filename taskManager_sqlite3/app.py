from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database/tasks.db'
db = SQLAlchemy(app) # Cursor para a base de dados SQLite

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    taskName = db.Column(db.String(50))
    taskIsDone = db.Column(db.Boolean)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    allTasks = Tasks.query.all()
    return render_template('index.html', tasksList = allTasks)

@app.route('/criar-tarefa', methods=['POST'])
def criar():
    # tarefa é um objeto da classe Tarefa (uma instância da classe)
    tarefa = Tasks(taskName=request.form['conteúdo_tarefa'], taskIsDone=False)
    db.session.add(tarefa) # Adicionar o objeto da Tarefa à base de dados
    db.session.commit() # Executar a operação pendente da base de dados
    return redirect(url_for('home'))

@app.route('/delTask/<id>')
def delTask(id):
    task = Tasks.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/doneTask/<id>')
def doneTask(id):
    task = Tasks.query.filter_by(id=int(id)).first()
    task.taskIsDone = not(task.taskIsDone)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True) # O debug=True faz com que cada vez que reiniciemos o servidor ou modifiquemos o código, o servidor de Flask reinicia-se sozinho

