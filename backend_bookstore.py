import sqlite3

class BackendBookStore:

    def conn(self):
        return sqlite3.connect("book_store.db")

    def __init__(self):
        self._conn = sqlite3.connect("book_store.db")
        self.cur = self._conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS  books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER,  isbn INTEGER)")
        self._conn.commit()

    def insert(self, title,author, year, isbn):
        self.cur.execute("INSERT INTO books VALUES (NULL, ?,?,?,?)", (title.lower(), author.lower(), year, isbn))
        self._conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM books")
        rows = self.cur.fetchall()
        return rows

    def search(self,title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM books where title=?  OR author = ? OR year=? OR isbn=?", (title.lower(), author.lower(), year, isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM books WHERE id = ?", (id,)) #ensure there is comma at the end when you have just one param in the placeholder
        self._conn.commit()

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id)) #ensure there is comma at the end when you have just one param in the placeholder
        self._conn.commit()
        

    def __del__(self):
        self._conn.close()
        
# delete(1)
#update(1, "c# for dummies", "Skuvkov Obiora", 2009,19800)
# insert("You dont know js", "Obiora",  2005, 90078)
#print(view()) 
#print(search( author="obiora"))