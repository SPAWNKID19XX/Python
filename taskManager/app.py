import mysql.connector
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
connect = mysql.connector.connect(
    user = 'Boris',
    password = 'root',
    host = '127.0.0.1'
)
print('Conected to DB:',connect.is_connected())

cursor = connect.cursor()
cursor.execute('CREATE DATABASE if not exists taskManager')
cursor.execute('USE taskManager')
cursor.execute('CREATE TABLE if not exists tasks(id int NOT NULL AUTO_INCREMENT,taskDescription varchar(100),isDone smallint,PRIMARY KEY (id));')
connect.commit()

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Boris:root@127.0.0.1/taskManager'
db = SQLAlchemy(app)

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    taskDescription = db.Column(db.String(100))
    isDone = db.Column(db.Boolean)


@app.route('/')
def home():
    taskList = Task.query.all()
    return render_template('index.html', tasksList = taskList)


@app.route('/addTask', methods=['GET', 'POST'])
def addTask():
    task = Task(taskDescription = request.form['target-descrition'], isDone=False)
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/delTask/<id>')
def deleteTask(id):
    task = Task.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/taskDone/<id>')
def taskDone(id):
    task = Task.query.filter_by(id=int(id)).first()
    task.isDone = not(task.isDone)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)