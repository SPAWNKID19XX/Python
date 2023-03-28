#python 3.10.8
#working with DB(exercise)
#DB = MariaDB(OpenServer)

def prt(arr):
    for obj in arr:
        print('\t',obj)

author = [
    {'firstName': 'Jorge', 'lastName' : 'Martin', 'isAlive': True},
    {'firstName': 'Dan', 'lastName' : 'Brawn', 'isAlive': True},
    {'firstName': 'Joanne', 'lastName' :  'Rowling', 'isAlive': True},
    {'firstName': 'William', 'lastName' :  'Shakespeare', 'isAlive': False},
    {'firstName': 'Andre', 'lastName' :  'Cruz', 'isAlive': False}
]

book = [
    {'isbn' : '0-553-10354-7', 'title': 'A game of throns', 'publisher' : 'Bantam Spectra', 'publYear': 1996},
    {'isbn' : '9781408855652', 'title': 'Harry Potter', 'publisher' : 'Bloomsbury', 'publYear': 1997},
    {'isbn' : '0-385-50420-9', 'title': 'The Da Vinci Code', 'publisher' : 'АСТ', 'publYear': 2003},
    {'isbn' : '0-385-50420-9', 'title': 'The Legend of Sleepy Hollow', 'publisher' : 'The Sketch Book of Geoffrey Crayon', 'publYear': 1820}
]


user = [
    {'firstName': 'Aaron', 'lastName' : 'Isac', 'loan': 25},
    {'firstName': 'Boris', 'lastName' : 'Isac', 'loan': 4},
    {'firstName': 'Emily', 'lastName' :  'Isac','loan':15}
]

import mysql.connector #import mysql module
#Connecting to DB
#first should create new user('Boris')global privilage in SQL
connect = mysql.connector.connect(
    user='Boris',
    password='root',
    host='127.0.0.1',
)
#confirm connecting
print('Connected to DB:',connect.is_connected())

cursor = connect.cursor()
#create cursor
cursor.execute("CREATE DATABASE if not exists library")
#select tablr library
cursor.execute('use library')
#create table author
cursor.execute('CREATE TABLE if not exists author( id int NOT NULL AUTO_INCREMENT,FirstName varchar(50),LastName varchar(50) NOT NULL,isAlive BIT(1),PRIMARY KEY (id));')
cursor.execute('CREATE TABLE if not exists book( isbn varchar(20) NOT NULL,title varchar(75),publisher varchar(50) NOT NULL,yearPubl int);')
cursor.execute('CREATE TABLE if not exists user( id int NOT NULL AUTO_INCREMENT,FirstName varchar(50),LastName varchar(50) NOT NULL,Loan int,PRIMARY KEY (id));')

#insert to author
for obj in author:
    query = "INSERT INTO author ( FirstName, LastName, isAlive ) VALUES ('{}','{}',{});".format(obj['firstName'], obj['lastName'], int(obj['isAlive']))
    #print(query)
    cursor.execute(query)

#insert to book
for obj in book:
    query = "INSERT INTO book ( isbn, title, publisher,yearPubl ) VALUES ('{}','{}','{}', {});".format(obj['isbn'], obj['title'], obj['publisher'], obj['publYear'])
    #print(query)
    cursor.execute(query)

#insert to user
for obj in user:
    query = "INSERT INTO user ( FirstName, LastName, Loan ) VALUES ('{}','{}',{});".format(obj['firstName'], obj['lastName'], obj['loan'])
    #print(query)
    cursor.execute(query)
connect.commit()
print('Tables were created and filled')

print('authors'.upper())
cursor.execute('select * from author')
authors = cursor.fetchall()
prt(authors)

print('Alive authors'.upper())
cursor.execute('select * from author where isAlive != 0')
authors = cursor.fetchall()
prt(authors)




print('books'.upper())
cursor.execute('select * from book')
books = cursor.fetchall()
prt(books)

print('Books published after 1900'.upper())
cursor.execute('select * from book where yearPubl > 1900')
books = cursor.fetchall()
prt(books)

print('users'.upper())
cursor.execute('select * from user')
users = cursor.fetchall()
prt(users)

print('users with loan>10'.upper())
cursor.execute('select * from user where Loan > 10')
users = cursor.fetchall()
prt(users)