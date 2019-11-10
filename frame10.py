import tkinter as tk

window = tk.Tk()
window.title('My frame')
window.geometry('400x300')

frm = tk.Frame(window)
frm.pack()

leftfrm = tk.Frame(frm, bd=2,width=100)
rightfrm = tk.Frame(frm, bg='red')

leftfrm.pack(side='left')
rightfrm.pack(side='right')

tk.Label(leftfrm,text='on the left').pack()
tk.Label(rightfrm,text='on the right').pack()
tk.Button(leftfrm,text='Button A').pack()

# what's the panel

window.mainloop()