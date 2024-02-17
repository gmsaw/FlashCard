import sqlite3
from time import time
from datetime import datetime

conn = sqlite3.connect('database.db')
c = conn.cursor()
current_time= time()

pos = 0

def create_note_table():
    c.execute(f"""CREATE TABLE notes_{pos} (
                text_note TEXT,
                keynote TEXT,
                status BOOLEAN DEFAULT TRUE,
                date REAL)""")

def create_file_table():
     c.execute("""CREATE TABLE FILE(
                title_page TEXT,
                date REAL,
                connection TEXT)""")

def new_file(title, current_time, pos):
    c.execute(f"INSERT INTO FILE (title_page, date, connection) VALUES (?,?,?)", (title, current_time, pos))
    print(f"File {title} pada {time_convert(current_time)} untuk {pos}, Berhasil")
    conn.commit()
    
def new_data():
    global pos  # Specify pos as a global variable
    loop = True
    while loop:
        try:
            create_note_table()
            loop = False
        except sqlite3.OperationalError:  # Catch the specific exception for table creation failure
            pos += 1
            loop = True  # Recursively try creating the table again with the updated pos value
    print(f"Tabel note_{pos} berhasil dibuat")
    conn.commit()
    return pos

def make_tables():
    def file_tabel():
        c.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='file' ''')
        try:
            create_file_table()
            print('Tabel file berhasil dibuat.')
        except:
            print('Tabel file sudah ada.')
    def note_tabel():
        # Cek apakah tabel sudah ada
        c.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='notes' ''')
        
        # Jika tabel sudah ada, lewati pembuatan tabel
            # Buat tabel jika belum ada
        try:
            c.execute(f"""CREATE TABLE notes_{pos} (
                    text_note TEXT,
                    keynote TEXT,
                    status BOOLEAN DEFAULT TRUE,
                    date REAL)""")
            print('Tabel note berhasil dibuat.')
            
        except: 
            print('Tabel note sudah ada.')
    file_tabel()
    note_tabel()

# def add(data, current_time):
#     for key,value in data.items():
#         c.execute("INSERT INTO notes (text_note, keynote, date) VALUES (?,?,?)", (value, key, current_time))

def add(pos, note, key, current_time):
    c.execute(f"INSERT INTO notes_{pos} (text_note, keynote, date) VALUES (?,?,?)", (note, key, current_time))
    conn.commit()
        
def note_reveal(pos):
    c.execute(f"SELECT * FROM notes_{pos}")
    return c.fetchall()

def file_reveal():
    c.execute(f"SELECT rowid, * FROM FILE")
    return c.fetchall()

def time_convert(time):
    convert_date = datetime.fromtimestamp(time)
    time_format = convert_date.strftime("%d %B %Y")
    return time_format

def colectalldata():
    data = reveal()
    for item in data:
        for note, key in zip(item[0], item[1]):
            print(note, key)

def delete_file(rowid):
    c.execute(f"DELETE from FILE WHERE rowid={rowid}")
    conn.commit()

if __name__ == "__main__":
    colectalldata()