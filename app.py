#Libraries
import tkinter as tk
from tkinter import *
from tkinter import ttk



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


window.mainloop()
