import tkinter 

window = tkinter.Tk()
but1 = tkinter.Button(window, text = '1', bg = 'blue')
but2 = tkinter.Button(window, text = '2', bg = 'blue')
but3 = tkinter.Button(window, text = '3', bg = 'blue')
but1.pack()
but2.pack()
but3.pack()
window.mainloop()