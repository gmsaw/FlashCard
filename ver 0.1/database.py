import sqlite3
from data import *
from time import time
from datetime import datetime

conn = sqlite3.connect('database.db')
c = conn.cursor()
current_time= time()

def make_tables():
    # Cek apakah tabel sudah ada
    c.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='notes' ''')
    
    # Jika tabel sudah ada, lewati pembuatan tabel
    if c.fetchone()[0] == 1:
        print('Tabel sudah ada.')
    else:
        # Buat tabel jika belum ada
        c.execute("""CREATE TABLE notes (
                text_note TEXT,
                keynote TEXT,
                status BOOLEAN DEFAULT TRUE,
                date REAL
            )""")
        print('Tabel berhasil dibuat.')

# def add(data, current_time):
#     for key,value in data.items():
#         c.execute("INSERT INTO notes (text_note, keynote, date) VALUES (?,?,?)", (value, key, current_time))

def add(note, key, current_time):
    c.execute("INSERT INTO notes (text_note, keynote, date) VALUES (?,?,?)", (note, key, current_time))
    conn.commit()
        
def reveal():
    c.execute("SELECT * FROM notes")
    return c.fetchall()

def time_convert(time):
    convert_date = datetime.fromtimestamp(time)
    time_format = convert_date.strftime("%d %B %Y")
    return time_format

if __name__ == "__main__":
    make_tables()
    data_dict= input_data()
    add(data=data_dict, current_time= current_time)
    reveal()

    conn.commit()
    conn.close()