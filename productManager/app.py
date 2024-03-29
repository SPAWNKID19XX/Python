from tkinter import ttk
from tkinter import *
import  sqlite3

class Product():
    db = 'database/product.db' #connecting DB i sqlite3

    #method for executing sql queries
    def db_consulta(self, consulta, parametros = ()):
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()
            resultado = cursor.execute(consulta, parametros)
            connection.commit()
        return resultado

    #method printing table in DB
    def get_all_products(self):
        registos_tabela = self.table.get_children()
        for linha in registos_tabela:
            self.table.delete(linha)

        query = "SELECT * FROM product ORDER BY name DESC"
        registos = self.db_consulta(query)
        for linha in registos:
            print(linha)
            self.table.insert('', 0, text = linha[1], values = linha[2])

    #2 method validation input
    def validation_name(self):
        insertedName = self.name.get()
        return len(insertedName) != 0
    def validation_price(self):
        insertedPrice = self.price.get()
        return len(insertedPrice) != 0
    #method add new product
    def add_product(self):
        if self.validation_price() and self.validation_name():
            query = 'INSERT INTO product VALUES(NULL,?,?)'
            parametros = (self.name.get(), self.price.get())
            self.db_consulta(query, parametros)
            print(self.name.get())
            print(self.price.get())
            self.msgLabel['text'] = 'Product {} has been added'.format(self.name.get())
            self.name.delete(0, END)
            self.price.delete(0, END)
        elif self.validation_price() == False and self.validation_name():
            self.msgLabel['text'] = 'Price must be enterred'
        elif self.validation_price() and self.validation_name() == False:
            self.msgLabel['text'] = 'Name must be enterred'
        else:
            self.msgLabel['text'] = 'Name and Price must be enterred'
        self.get_all_products()

    
    #method delete product
    def delProd(self):
        self.msgLabel['text'] = ''
        try:
            print(self.table.item(self.table.selection())['text'][0])
        except IndexError as erro:
            self.msgLabel['text'] = 'You should select some item'
            return
        
        self.msgLabel['text'] = ''
        selectItem = self.table.item(self.table.selection())['text']
        query = "DELETE FROM product WHERE name = ?"
        self.db_consulta(query, (selectItem,))
        self.msgLabel['text'] = '{} has been deleted'.format(selectItem)
        self.get_all_products()
        
    #new window edit product
    def editProd(self):
        self.msgLabel['text'] = ''
        try:
            pass
        except IndexError as erro:
            self.msgLabel['text'] = 'You should select some item'
            return
        
        oldName = self.table.item(self.table.selection())['text']
        oldPrice = self.table.item(self.table.selection())['values'][0]
        
        self.editWindow = Toplevel()
        self.editWindow.title('Edit product')
        self.editWindow.resizable(1,1)
        self.editWindow.wm_iconbitmap('template/icon.ico')
        self.editWindow.geometry('400x500')
        
        titleEditWindow = Label(self.editWindow, text='Edit Product', font=('calibri', 50, 'bold'))
        titleEditWindow.grid(row=0, column=0)
        
        frameEdit = LabelFrame(self.editWindow, text='Edit Product', font=('Calibri', 16, 'bold'))
        frameEdit.grid(row=1, column=0, columnspan=20,pady=20)
        
        self.lblOldName = Label(frameEdit, text='Old Name: ', font=('Calibri', 13))
        self.lblOldName.grid(row=1, column=0)
        self.lblOldNameValue = Entry(frameEdit, text = oldName, textvariable=StringVar(self.editWindow, value=oldName), state='readonly', font=('Calibri', 13))
        self.lblOldNameValue.grid(row=1, column=1)
        
        self.lblNewName = Label(frameEdit, text='New Name: ', font=('Calibri', 13))
        self.lblNewName.grid(row=2, column=0)
        self.newNameValue = Entry(frameEdit, font=('Calibri', 13))
        self.newNameValue.grid(row=2, column=1)
        
        
        self.lblOldPrice = Label(frameEdit, text='Old Price: ', font=('Calibri', 13))
        self.lblOldPrice.grid(row=3, column=0)
        self.lblOldPriceValue = Entry(frameEdit, text = oldPrice, textvariable=StringVar(self.editWindow, value=oldPrice), state='readonly', font=('Calibri', 13))
        self.lblOldPriceValue.grid(row=3, column=1)
        
        self.lblNewPrice = Label(frameEdit, text='New Price: ', font=('Calibri', 13))
        self.lblNewPrice.grid(row=4, column=0)
        self.newPriceValue = Entry(frameEdit, font=('Calibri', 13))
        self.newPriceValue.grid(row=4, column=1)
        
        self.seveChangeButton = ttk.Button(frameEdit, text='Seve Change', style='my.TButton', command=lambda: 
            self.editProduct(
                self.newNameValue.get(), 
                self.lblOldNameValue.get(), 
                self.newPriceValue.get(),
                self.lblOldPriceValue.get()
                )
            )
        s = ttk.Style() 
        s.configure('my.TButton', font=('Calibri', 14, 'bold'))
        
        self.seveChangeButton.grid(row=5, columnspan=2,sticky=W+E)

    #method editProduct
    def editProduct(self, newName, oldName, newPrice, oldPrice):
        productEditable = False
        query = "UPDATE product SET name = ?, price = ? WHERE name = ? and price = ?"
        if newName!='' and newPrice != '':
            parametrs = (newName, newPrice, oldName, oldPrice)
            productEditable = True
            print('newName and newPrice are not empty')
        elif newName!='' and newPrice=='':
            parametrs = (newName, oldPrice, oldName, oldPrice)
            productEditable = True
            print('newName is not empty, but newPrice is ampty')
        elif newName=='' and newPrice != '':
            parametrs = (oldName, newPrice, oldName, oldPrice)
            productEditable = True
            print('newName is empty, but newPrice is not ampty')
            
        if productEditable:
            self.db_consulta(query, parametrs)
            self.editWindow.destroy()
            self.msgLabel['text'] = '{} edited'.format(oldName)
            self.get_all_products()
        else:
            self.editWindow.destroy()
            self.msgLabel['text'] = '{} not edited'.format(oldName)
            
        
            
    #mainWindow
    def __init__(self, root):
        self.window = root
        self.window.title("App Product Manager") # Título da janela
        self.window.resizable(1,1) # Ativar a redimensionamento da janela. Para desativá-la: (0,0)
        self.window.wm_iconbitmap('template/icon.ico')

        frame = LabelFrame(self.window, text="Add New Product", font=('Calibri', 16, 'bold'))
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20, padx=20)

        self.lName = Label(frame, text='Name')
        self.lName.grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=1, column=1)

        self.lPrice = Label(frame, text='Price')
        self.lPrice.grid(row=2, column=0)
        self.price = Entry(frame)
        self.price.focus()
        self.price.grid(row=2, column=1)

        self.msgLabel = Label(text='', fg='red')
        self.msgLabel.grid(row = 3,column = 0, columnspan = 2, sticky= W + E)

        s = ttk.Style()        
        s.configure('my.TButton', font=('Calibri', 14, 'bold'))
        self.buttonAdd = ttk.Button(frame, text='Add Product', command=self.add_product, style='my.TButton')
        self.buttonAdd.grid(row=3, columnspan=2, sticky=W+E)

        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri',11))  # Modifica-se a fonte da tabela
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13, 'bold')) # Modifica-se a fonte das cabeceiras
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Eliminar as bordas

        self.table = ttk.Treeview(height=20, columns=2, style="mystyle.Treeview")
        self.table.grid(row=4, column=0, columnspan=2)
        self.table.heading('#0', text='Name', anchor=CENTER)  # Cabeçalho 0
        self.table.heading('#1', text='Price', anchor=CENTER)  # Cabeçalho 1

        self.get_all_products()

        # Botões de Eliminar e Editar
        s = ttk.Style() 
        s.configure('my.TButton', font=('Calibri', 14, 'bold'))
        botao_eliminar = ttk.Button(text = 'ELIMINAR', command=self.delProd, style='my.TButton')
        botao_eliminar.grid(row = 5, column = 0, sticky = W + E)
        botao_editar = ttk.Button(text='EDITAR', command=self.editProd, style='my.TButton')
        botao_editar.grid(row = 5, column = 1, sticky = W + E)

if __name__ == '__main__':
    root = Tk()
    root.geometry("400x650") #windows size
    app = Product(root)
    root.mainloop()