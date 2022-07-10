import tkinter, time
from numpy import place

def ecovar_test():
    def test():
        print("running...")
    ecovar_window = tkinter.Tk()
    ecovar_window.title("Ecovar Testing")
    b1 = tkinter.Button(ecovar_window,text = "close loop", command = test)
    b1.place(x=10, y=10)

main_window = tkinter.Tk() # Creation of main application window 
main_window.title('EcoJoule Tester') 
button1 = tkinter.Button(main_window, text = "EcoVar Tests", command = ecovar_test)
button1.pack()

switch = tkinter.IntVar()
switch = 0
checkbox = tkinter.Checkbutton(main_window, text = 'EvoVAR Test', variable = switch)
checkbox.pack()
if switch == 1:
    print("ok")
main_window.mainloop() # Launch event controller 


