import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('My login')
window.geometry('300x150')


tk.Label(window,text="UserName:").place(x=40,y=30)
tk.Label(window,text="Password:").place(x=40,y=60)
var_username = tk.StringVar()
var_password = tk.StringVar()
var_username.set('lenovo')

tk.Entry(window,width=20,textvariable=var_username).place(x=120,y=30)
tk.Entry(window,width=20,textvariable=var_password,show='*').place(x=120,y=60)


def login():
    if var_username.get()=='lenovo' and var_password.get()=='key':
        print('ok')
        messagebox.showinfo('Login','Welcome to this application')
    else:
        print('No')
        messagebox.showwarning('Login','Sorry,bad password')


    return


tk.Button(window,text='Login',width=10,command=login).place(x=120,y=90)

window.mainloop()