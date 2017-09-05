from tkinter import *
import tkinter.messagebox
from backend_bookstore import BackendBookStore

database= BackendBookStore()
#class BookStore:
def view_command():
    lstData.delete(0, END)
    for row in database.view():
        lstData.insert(END, row)

def search(title, author, year, isbn):
    return database.search(title, author, year, isbn)

def update(id, title, author, year, isbn):
    database.update(id, title, author, year, isbn)
    clear_command()
    
def insert(title, author, year, isbn):
    return database.insert(title, author, year, isbn)
def search_command():
    lstData.delete(0, END)
    result = search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    for book in result:
        lstData.insert(END, book)

def update_command():
    lstData.delete(0, END)
    update(selected[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()
def insert_command():
    lstData.delete(0, END)
    insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()

def delete_command():
    database.delete(selected[0])
    view_command()

def get_selected_row(event):
    global selected
    index=lstData.curselection()[0]
    selected=lstData.get(index)
    clear_command()
    elTitle.insert(0, selected[1])
    elAuthor.insert(0,selected[2])
    elYear.insert(0,selected[3])
    elIsbn.insert(0,selected[4])

def clear_command():
    elTitle.delete(0,END)
    elAuthor.delete(0,END)
    elYear.delete(0,END)
    elIsbn.delete(0,END)

def ask_quit():
    #if tkMessageBox.askokcancel("Quit", "You want to quit now? *sniff*"):
    window.destroy()

window = Tk()
window.wm_title("book Store")
lblTitle = Label(window, text="Title")
lblTitle.grid(row=0,column=0)
lblYear = Label(window, text="Year")
lblYear.grid(row=1,column=0)

lblAuthor = Label(window, text="Author")
lblAuthor.grid(row=0,column=2)
lblIsbn = Label(window, text="ISBN")
lblIsbn.grid(row=1,column=2)

title_text = StringVar()
elTitle = Entry(window, textvariable=title_text)
elTitle.grid(row=0, column=1)

year_text = StringVar()
elYear = Entry(window, textvariable=year_text)
elYear.grid(row=1, column=1)

author_text = StringVar()
elAuthor = Entry(window, textvariable=author_text)
elAuthor.grid(row=0, column=3)

isbn_text = StringVar()
elIsbn = Entry(window, textvariable=isbn_text)
elIsbn.grid(row=1, column=3)

lstData = Listbox(window, height=7, width=35)
lstData.grid(row=2, column=0, rowspan=6, columnspan=2)

sb=Scrollbar(window)
sb.grid(row=2,column=2, rowspan=6)

lstData.configure(yscrollcommand=sb.set)
sb.configure(command=lstData.yview)

btnView = Button(window, text="View All", width=12, command=view_command)
btnView.grid(row=2,column=3)

btnSearch = Button(window, text="Search Entry", width=12, command=search_command)
btnSearch.grid(row=3,column=3)

btnAdd = Button(window, text="Add Entry", width=12, command = insert_command)
btnAdd.grid(row=4,column=3)

btnUpdate = Button(window, text="Update", width=12, command=update_command)
btnUpdate.grid(row=5,column=3)

btnDelete = Button(window, text="Delete", width=12, command=delete_command)
btnDelete.grid(row=6,column=3)

btnClear = Button(window, text="Clear", width=12, command=clear_command)
btnClear.grid(row=7,column=3)

btnClose = Button(window, text="Close", width=12, command=ask_quit)
btnClose.grid(row=8,column=3)

lstData.bind('<<ListboxSelect>>', get_selected_row)   
        

view_command()    
window.mainloop()