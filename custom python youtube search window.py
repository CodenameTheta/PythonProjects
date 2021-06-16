from tkinter import *
import webbrowser


root = Tk()
root.title("ThetaSearch")
e = Entry(root, width=50)
e.pack()

def searchClick():
    tabUrl = "https://youtube.com/results?search_query="
    term = e.get()

    webbrowser.open(tabUrl+term, new=0)

aLabel = Label(root, text="search youtube for something:")
aLabel.pack()
aButton = Button(root, text="search", command=searchClick)
aButton.pack()

root.mainloop()
