import tkinter
from tkinter import *
from tkinter import ttk
import mysql.connector  # import mysql module

class Product:
    def __init__(self, root):
        self.window = root
        self.window.geometry('1300x600+100+50')
        self.window.update_idletasks()
        self.window.resizable(True,True)  # Ativar a redimensionamento da janela. Para desativá-la: (0,0)
        self.window.wm_iconbitmap('template/M6_p2_icon.ico')
        self.window.title('App Product Manager')
        frame = LabelFrame(self.window, text = 'Registr new Product')
        frame.grid(row=3, column=3, columnspan= 5, pady=20)
        # Label Nome
        self.nameLabel = Label(frame, text="Name: ")# Label belongs to frame
        self.nameLabel.grid(row=1, column=0)# Possition
        # input Name
        self.name = Entry(frame)# input belongs to frame
        self.name.focus()# Para que o foco do rato vá a esta Entry no início
        self.name.grid(row=1, column=1) #Possition
        # Label Price
        self.priceLabel = Label(frame, text='Price') # Labal belongs to frame
        self.priceLabel.grid(row=2, column=0)# Possition
        # Input Price
        self.price = Entry(frame)# input belongs to frame
        self.price.grid(row=2, column=1)# possition
        #Button SAVE
        self.buttonSave = Button(frame,text='Save', width=20)
        self.buttonSave.grid(row=1, column=2, padx=20)


if __name__ == '__main__':
    root = Tk()
    app = Product(root)
    root.mainloop()
