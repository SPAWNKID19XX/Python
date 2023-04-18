import tkinter
from tkinter import *
from tkinter import ttk
import mysql.connector  # import mysql module

productList = [{'name':'Impressora 3D','price':1000},{'name':'Arduino','price':20},{'name':'Raspberry Pi 4','price':50}]


class Product:
    def __init__(self, root):
        self.window = root
        self.window.geometry('1300x600+100+50')
        self.window.update_idletasks()
        self.window.resizable(True,True)  # Ativar a redimensionamento da janela. Para desativá-la: (0,0)
        self.window.wm_iconbitmap('template/M6_p2_icon.ico')
        self.window.title('App Product Manager')
        frame = LabelFrame(self.window, text = 'Registr new Product')
        frame.grid(row=3, column=3, columnspan= 2, pady=20)
        # Label Nome
        self.nameLabel = Label(frame, text="Name: ")# Label belongs to frame
        self.nameLabel.grid(row=1, column=0)# Possition
        # input Name
        self.name = Entry(frame)# input belongs to frame
        self.name.focus()# Para que o foco do rato vá a esta Entry no início
        self.name.grid(row=1, column=1) #Possition
        # Label Price
        self.priceLabel = Label(frame, text='Price') # Labal belongs to frame
        self.priceLabel.grid(row=2, column=1)# Possition
        # Input Price
        self.price = Entry(frame)# input belongs to frame
        self.price.grid(row=2, column=1)# possition
        #Button SAVE
        self.buttonSave = Button(frame,text='Save', width=20)
        self.buttonSave.grid(row=1, column=2, padx=20)

        # Tabela de Produtos
        # Estilo personalizado para a tabela
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))
        # Modifica-se a fonte da tabela
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13, 'bold'))
        # Modifica-se a fonte das cabeceiras
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])
        # Eliminar as bordas
        # Estrutura da tabela
        self.tabela = ttk.Treeview(height=20, columns=2, style="mystyle.Treeview")
        self.tabela.grid(row=4, column=3, columnspan=2)
        self.tabela.heading('#0', text='Nome', anchor=CENTER)  # Cabeçalho 0
        self.tabela.heading('#1', text='Preço', anchor=CENTER)  # Cabeçalho 1


#create Database and table
connect = mysql.connector.connect(
    host='127.0.0.1',
    user = 'Boris',
    password = 'root'
)

print('Connection:',connect.is_connected())

cursor = connect.cursor()

#create DataBase
query = "CREATE DATABASE if not exists dsktopApp"
cursor.execute(query)
#Create table
query = "USE dsktopApp"
a = cursor.execute(query)
query = "CREATE TABLE if not exists products(id int NOT NULL AUTO_INCREMENT,name TEXT NOT NULL,price FLOAT NOT NULL,PRIMARY KEY (id));)"
cursor.execute(query)

query = 'SELECT * FROM products'
cursor.execute(query)



'''
if __name__ == '__main__':
    root = Tk()
    app = Product(root)
    root.mainloop()
'''