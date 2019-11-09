import tkinter as tk

window = tk.Tk()
window.title('My Listbox')
window.geometry('400x300')


var1 = tk.StringVar()

l = tk.Label(window,bg='yellow',width=20,height=2,text='Empty')
l.pack()


def radio_command():
    l.config(text='you have selected ' + var1.get())
    return


r1 = tk.Radiobutton(window,text='Optiion A',variable=var1,value='A',command=radio_command)
r1.pack()

r2 = tk.Radiobutton(window,text='Optiion B',variable=var1,value='B',command=radio_command)
r2.pack()

r3 = tk.Radiobutton(window,text='Optiion C',variable=var1,value='C',command=radio_command)
r3.pack()


tk.Radiobutton(window,text='Optiion D',variable=var1,value='D',indicatoron=0,command=radio_command).pack()
tk.Radiobutton(window,text='Optiion E',variable=var1,value='E',indicatoron=0,command=radio_command).pack()

window.mainloop()