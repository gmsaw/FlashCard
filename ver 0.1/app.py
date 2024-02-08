from tkinter import *
from database import *

root = Tk()
root.title("FlashCard")
make_tables()

def showdata():
    data_root = Tk()
    data_root.title("Data")
    data = reveal()
    for item in data:
        if item[2] == 1:
            cond = "Berlangsung"
        else:
            cond = "Menunggu"
        myLabel1 = Label(data_root, text=f"Notes = {item[0]}, keynote= {item[1]}, Condition = {cond}, time = {time_convert(time=item[3])}")
        myLabel1.grid(column=0, columnspan=3)
    data_root.mainloop()
    
def submit():
    note_data = e_note.get()
    keynote_data = e_keynote.get()
    add(note_data, keynote_data, current_time)
    print("Data berhasil ditambahkan")
    e_note.delete(0, END)
    e_keynote.delete(0, END)

l_title = Label(root, text="Input Notes")
l_title.grid(row=0, column=0, columnspan=2)
l_note = Label(root, text="Catatan")
l_note.grid(row=1, column=0)
l_keynote = Label(root, text="Kata Kunci")
l_keynote.grid(row=2, column=0)

e_note = Entry(root, width=30)
e_note.grid(row=1, column=1)
e_keynote = Entry(root, width=30)
e_keynote.grid(row=2, column=1)

b_submit = Button(root, text="Submit", padx=30, pady=5, command=submit)
b_submit.grid(row=3, column=0, columnspan=2)

b_showall = Button(root, text="show all data",  padx=15, pady=5, command=showdata)
b_showall.grid(row=4, column=0, columnspan=2)

root.mainloop()