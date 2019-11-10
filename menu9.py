import tkinter as tk

window = tk.Tk()
window.title('My Listbox')
window.geometry('400x300')

l = tk.Label(window,bg='yellow',width=30,height=2,text='Empty')
l.pack()

counter = 0

def cmd():
    global counter
    print('New file command')
    counter+=1
    l.config(text='do ' + str(counter))
    return

mbar = tk.Menu(window)
filemenu = tk.Menu(mbar,tearoff=0)
mbar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New',command=cmd)
filemenu.add_command(label='Save',command=cmd)
filemenu.add_command(label='Open',command=cmd)
filemenu.add_command(label='Close',command=cmd)
filemenu.add_separator()

# 多级菜单
submenu = tk.Menu(filemenu,tearoff=0)
filemenu.add_cascade(label='Import',menu=submenu)
submenu.add_command(label='Submenu1',command=cmd)

filemenu.add_command(label='Exit',command=window.quit)


editmenu = tk.Menu(mbar,tearoff=0)
mbar.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label='Cut',command=cmd)
editmenu.add_command(label='Copy',command=cmd)
editmenu.add_command(label='Paste',command=cmd)

window.config(menu=mbar)

window.mainloop()