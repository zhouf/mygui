import tkinter as tk

window = tk.Tk()
window.title('My Listbox')
window.geometry('400x300')


var1 = tk.StringVar()

l = tk.Label(window,bg='yellow',width=10,height=2,textvariable=var1)
l.pack()

def cmd1():
    str = lbox.get(lbox.curselection())
    var1.set(str)
    return


btn1=tk.Button(window,text='print selection',width=25,height=2,command=cmd1)
btn1.pack()

var2 = tk.StringVar()
var2.set((11,22,33,44,55,66,'hhh'))
lbox = tk.Listbox(window,listvariable=var2)
lbox.insert('end','hello')
list_items = [1,2,3,4]
for item in list_items:
    lbox.insert('end',item)

lbox.pack()

window.mainloop()