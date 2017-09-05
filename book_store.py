from tkinter import *
import tkinter.messagebox
from backend_bookstore import BackendBookStore


class BookStore:
    
    def __init__(self):
        self.database= BackendBookStore()
        lblTitle = Label(window, text="Title")
        lblTitle.grid(row=0,column=0)
        lblYear = Label(window, text="Year")
        lblYear.grid(row=1,column=0)

        lblAuthor = Label(window, text="Author")
        lblAuthor.grid(row=0,column=2)
        lblIsbn = Label(window, text="ISBN")
        lblIsbn.grid(row=1,column=2)

        title_text = StringVar()
        self.elTitle = Entry(window, textvariable=title_text)
        self.elTitle.grid(row=0, column=1)

        year_text = StringVar()
        self.elYear = Entry(window, textvariable=year_text)
        self.elYear.grid(row=1, column=1)

        author_text = StringVar()
        self.elAuthor = Entry(window, textvariable=author_text)
        self.elAuthor.grid(row=0, column=3)

        isbn_text = StringVar()
        self.elIsbn = Entry(window, textvariable=isbn_text)
        self.elIsbn.grid(row=1, column=3)

        self.lstData = Listbox(window, height=7, width=35)
        self.lstData.grid(row=2, column=0, rowspan=6, columnspan=2)

        sb=Scrollbar(window)
        sb.grid(row=2,column=2, rowspan=6)

        self.lstData.configure(yscrollcommand=sb.set)
        sb.configure(command=self.lstData.yview)

        btnView = Button(window, text="View All", width=12, command=self.view_command)
        btnView.grid(row=2,column=3)

        btnSearch = Button(window, text="Search Entry", width=12, command=self.search_command)
        btnSearch.grid(row=3,column=3)

        btnAdd = Button(window, text="Add Entry", width=12, command = self.insert_command)
        btnAdd.grid(row=4,column=3)

        btnUpdate = Button(window, text="Update", width=12, command=self.update_command)
        btnUpdate.grid(row=5,column=3)

        btnDelete = Button(window, text="Delete", width=12, command=self.delete_command)
        btnDelete.grid(row=6,column=3)

        btnClear = Button(window, text="Clear", width=12, command=self.clear_command)
        btnClear.grid(row=7,column=3)

        btnClose = Button(window, text="Close", width=12, command=self.ask_quit)
        btnClose.grid(row=8,column=3)

        self.lstData.bind('<<ListboxSelect>>', self.get_selected_row)   
                
    def view_command(self):
        self.lstData.delete(0, END)
        for row in self.database.view():
            self.lstData.insert(END, row)

    def search(self, title, author, year, isbn):
        return self.database.search(title, author, year, isbn)

    def update(self, id, title, author, year, isbn):
        self.database.update(id, title, author, year, isbn)
        self.clear_command()
        
    def insert(self, title, author, year, isbn):
        return self.database.insert(title, author, year, isbn)
    def search_command(self):
        self.lstData.delete(0, END)
        result = self.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
        for book in result:
            self.lstData.insert(END, book)

    def update_command(self):
        self.lstData.delete(0, END)
        self.update(selected[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
        self.view_command()
    def insert_command(self):
        self.lstData.delete(0, END)
        self.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
        self.view_command()

    def delete_command(self):
        self.database.delete(selected[0])
        self.view_command()

    def get_selected_row(self, event):
        global selected
        index=lstData.curselection()[0]
        selected=self.lstData.get(index)
        self.clear_command()
        self.elTitle.insert(0, selected[1])
        self.elAuthor.insert(0,selected[2])
        self.elYear.insert(0,selected[3])
        self.elIsbn.insert(0,selected[4])

    def clear_command(self):
        self.elTitle.delete(0,END)
        self.elAuthor.delete(0,END)
        self.elYear.delete(0,END)
        self.elIsbn.delete(0,END)

    def ask_quit(self):
        window.destroy()

window = Tk()
window.wm_title("book Store")
app =BookStore()
app.view_command()    
window.mainloop()