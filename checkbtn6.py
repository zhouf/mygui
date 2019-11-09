import tkinter as tk

window = tk.Tk()
window.title('My Listbox')
window.geometry('400x300')


l = tk.Label(window,bg='yellow',width=30,height=2,text='Empty')
l.pack()

def cmd1():
    v1 = var1.get()
    v2 = var2.get()
    print(v1,"-",v2)
    if (v1==1) & (v2==1):
        l.config(text='I love both')
    elif (v1==1) & (v2==0):
        l.config(text='I love python')
    elif (v1==0) & (v2==1):
        l.config(text='I love java')
    else:
        l.config(text='I do not love either')
    return


var1 = tk.IntVar()
var2 = tk.IntVar()
cbtn1 = tk.Checkbutton(window,text='Python',variable=var1,onvalue=1,offvalue=0,command=cmd1)
cbtn2 = tk.Checkbutton(window,text='Java',variable=var2,onvalue=1,offvalue=0,command=cmd1)
cbtn1.pack()
cbtn2.pack()

window.mainloop()