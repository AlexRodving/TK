from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Python32')

# root.iconbitmap('icon.ico')

root.geometry('400x400+800+300')
root.resizable(0,0)

root.config(bg='black')

def click():
    if txt['text'] == 'Текст':
        txt['text'] = 'New txt'
    else:
       txt['text'] = 'Текст' 
    

btn = Button(root, text="Кнопка", command=click, width=10,
font=("Comics Sans MS", 20, "italic")).pack()

btn2 = Button(root, text='Btn2', width=10).pack()

txt = Label(root, text='Текст')
txt.pack(fill=X)


img = PhotoImage(file='./logo.png', width=200,height=200, format='png')
l_img = ttk.Label(root, image=img, text="Python", compound='top')
l_img.pack()


root.mainloop()