import tkinter as tk

window = tk.Tk()
window.title('My Listbox')
window.geometry('400x300')

l = tk.Label(window,bg='yellow',width=30,height=2,text='Empty')
l.pack()

counter = 0

def cmd():
    return

mbar = tk.Menu(window)
filemenu = tk.Menu(mbar,tearoff=0)
mbar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New',command=cmd)

window.config(menu=mbar)


window.mainloop()