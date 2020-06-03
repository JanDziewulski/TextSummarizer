#Libraries
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import*
import tkinter.filedialog



# Web Scraping Pkg



window = Tk()
window.title('Sumarize GUI')
window.geometry('700x500')

#Style
style = ttk.Style(window)
style.configure('lefttab.TNotebook', tabposition = 'wn')

#Tabs
tab_control = ttk.Notebook(window, style = 'lefttab.TNotebook')
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)

#Add tabs to notebook
tab_control.add(tab1, text = f'{"Home":^20s}')
tab_control.add(tab2, text = f'{"File":^20s}')
tab_control.add(tab3, text = f'{"URL":^20s}')
tab_control.add(tab4, text = f'{"Comparer":^20s}')

#Labels
label1 = Label(tab1, text = 'Summaryzer', padx = 5, pady = 5)
label1.grid(column = 0, row = 0)
label2 = Label(tab2, text = 'File Processing', padx = 5, pady = 5)
label2.grid(column = 0, row = 0)
label3 = Label(tab3, text = 'URL', padx = 5, pady = 5)
label3.grid(column = 0, row = 0)
label4 = Label(tab4, text = 'Comparer', padx = 5, pady = 5)
label4.grid(column = 0, row = 0)

tab_control.pack(expand = 1, fill ='both')

#Functions


#Main Home Tab
l1 = Label(tab1, text = 'Enter Text to Summarize', padx = 5, pady = 5)
l1.grid(column = 0, row = 1)
entry = ScrolledText(tab1, height = 10)
entry.grid(row = 2, column = 0, columnspan = 2, pady = 5, padx = 5)

#Buttons
button1 = Button(tab1, text = 'Reset', width = 12,
                 bg = '#25d366', fg = '#fff')
button1.grid(row = 4, column = 0, pady = 10, padx = 10)

button1 = Button(tab1, text = 'Save', width = 12,
                 bg = '#', fg = '#fff')
button1.grid(row = 4, column = 0, pady = 10, padx = 10)

button1 = Button(tab1, text = 'Reset', width = 12,
                 bg = '#25d366', fg = '#fff')
button1.grid(row = 4, column = 0, pady = 10, padx = 10)

button1 = Button(tab1, text = 'Reset', width = 12,
                 bg = '#25d366', fg = '#fff')
button1.grid(row = 4, column = 0, pady = 10, padx = 10)

button1 = Button(tab1, text = 'Reset', width = 12,
                 bg = '#25d366', fg = '#fff')
button1.grid(row = 4, column = 0, pady = 10, padx = 10)
#File Processing Tab

window.mainloop()
