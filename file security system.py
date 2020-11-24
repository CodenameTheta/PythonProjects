from tkinter import *
import webbrowser
import os

root = Tk()

e = Entry(root, width=40)
e.pack()
inputpass = "please"
password = "YOU DIDN'T SAY THE MAGIC WORD!!!"

def myclick():
    if e.get() == inputpass:
        print("ACCESS GRANTED")
        os.startfile(r"folder location of hidden stuff goes here")
    else:
        for i in range(20):
            print(password)
        webbrowser.open("https://www.youtube.com/watch?v=g_vZasFzMN4&ab_channel=modusbeke", new=0)
        
myLabel = Label(root, text="input the password")
myLabel.pack()
myButton = Button(root, text="submit", command=myclick)
myButton.pack()

root.mainloop()
