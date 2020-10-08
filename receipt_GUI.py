from tkinter import *
from tkinter import messagebox

window = Tk()

window.geometry("400x400")

prices = []

def displayMsg():
    item = entryItem.get()
    price = entryPrice.get()
    price = float(price)
    prices.append(price)
    entry = "%-25s $%10.2f\n" % (item, price)
    T.insert(END, entry) 

def displayTotal():
    total = sum(prices)
    messagebox.showinfo("POS", "Total is : " + str(total))

# Create label 
l = Label(window, text = "Receipt") 
l.pack() 

# Create text widget and specify size. 
T = Text(window, height = 10, width = 42) 
T.pack()  

l1 = Label(window, text="Item name: ")
l2 = Label(window, text="Item price: ")
entryItem = Entry(window)
entryPrice = Entry(window)

#position the UI
l1.pack()  
entryItem.pack()  
l2.pack() 
entryPrice.pack()  

#create and place button
button1 = Button(window, text="Insert Item", bg="lightgreen", command=displayMsg)
button1.pack(side='top', expand=YES)

button2 = Button(window, text="Total", bg="red", command=displayTotal)
button2.pack(side='top', expand=YES)

window.mainloop()