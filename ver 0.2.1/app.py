from tkinter import *
from database import *
from tkinter import messagebox
from cornell import main
    
def delete_page():
    for frame in main_frame.winfo_children():
        frame.destroy()

def data_page(frame):
    
    data_frame = Frame(frame)
    data_frame.pack(fill=BOTH, expand=True)
    
    def back():
        delete_page()
        notes_page(frame)
    
    def convert():
        delete_page()
        convert_page(frame)
        # try:
        #     building(data)
        #     messagebox.showinfo(title="convert", message="convert sucsess :)")
        # except:
        #     messagebox.showerror(title="error", message="ERROROROROROOROROR")
    
    data = reveal()
    for item in data:
        if item[2] == 1:
            cond = "Berlangsung"
        else:
            cond = "Menunggu"
        myLabel1 = Label(data_frame, text=f"Notes = {item[0]}, keynote= {item[1]}, Condition = {cond}, time = {time_convert(time=item[3])}")
        myLabel1.grid(column=0, columnspan=3)
    
    back_btn= Button(data_frame, text="back", command= back, padx=30, pady=5)
    back_btn.grid(sticky=W)
    convert_btn = Button(data_frame, text="Convert to docx", command=convert)
    convert_btn.grid()

def notes_page(frame):
    def showdata():
        delete_page()
        data_page(frame)
        
    def submit():
        note_data = e_note.get()
        keynote_data = e_keynote.get()
        
        if note_data == "" and keynote_data == "":
            messagebox.showinfo(title="error", message="Input kosong")
        else:
            add(note_data, keynote_data, current_time)
            print("Data berhasil ditambahkan")
            e_note.delete(0, END)
            e_keynote.delete(0, END)

    note_frame = Frame(frame)
    note_frame.pack()
    
    l_title = Label(note_frame, text="Input Notes")
    l_title.grid(row=0, column=0, columnspan=2)
    l_note = Label(note_frame, text="Catatan")
    l_note.grid(row=1, column=0)
    l_keynote = Label(note_frame, text="Kata Kunci")
    l_keynote.grid(row=2, column=0)

    e_note = Entry(note_frame, width=30)
    e_note.grid(row=1, column=1)
    e_keynote = Entry(note_frame, width=30)
    e_keynote.grid(row=2, column=1)

    b_submit = Button(note_frame, text="Submit", padx=30, pady=5, command=submit)
    b_submit.grid(row=3, column=0, columnspan=2)

    b_showall = Button(note_frame, text="show all data",  padx=15, pady=5, command=showdata)
    b_showall.grid(row=4, column=0, columnspan=2)

def convert_page(frame):
    convert_frame = Frame(frame)
    convert_frame.pack(fill=BOTH, expand=True)
    
    def back():
        delete_page()
        data_page(frame)
    
    def create():
        if title_e.get() == "" or sub_e.get() == "" or source_e.get() == "":
            messagebox.showerror(title="error", message="Data Kosong")
        else:
            data = reveal()
            title = title_e.get()
            sub = sub_e.get()
            source = source_e.get()
            title_e.delete(0, END)
            sub_e.delete(0, END)
            source_e.delete(0, END)
            
            main(data, title, sub, source)
            messagebox.showinfo(title="info", message="succses")
        
            # messagebox.showerror(title="error", message="ERROROROROROR")
            
    
    title_lb = Label(convert_frame, text="Subject")
    title_lb.grid(row=0, column=0)
    sub_lb = Label(convert_frame, text="Sub Subject")
    sub_lb.grid(row=1, column=0)
    source_lb = Label(convert_frame, text="Qr Source")
    source_lb.grid(row=2, column=0)
    
    title_e = Entry(convert_frame, width=30)
    source_e = Entry(convert_frame, width=30)
    sub_e = Entry(convert_frame, width=30)
    title_e.grid(row=0, column=1)
    source_e.grid(row=2, column=1)
    sub_e.grid(row=1, column=1)
    
    cancel_btn = Button(convert_frame, text="Kembali", command=back, padx=20)
    cancel_btn.grid(row=3, column=0, pady=10, padx=5)
    
    create_btn = Button(convert_frame, text="Create", command=create, padx=20)
    create_btn.grid(row=3, column=1, pady=10, padx=5)
    
def home_page(frame):
    home_frame = Frame(frame)
    home_frame.pack(fill=BOTH, expand=True)
    
    def newfile():
        delete_page()
        notes_page(frame)
        
    def load():
        print("loaded")
    
    main_frame = Frame(home_frame, height=50, width=100)
    main_frame.pack()
    
    new_btn = Button(main_frame, text="New File", pady=10, padx=25, command=newfile)
    new_btn.pack(pady=5)
    load_btn = Button(main_frame, text="Load File", pady=10, padx=25, command=load)
    load_btn.pack(pady=5)
    
    history_frame= Frame(home_frame, height=200, width=100)
    history_frame.pack()
    
    
    
if __name__ == "__main__":
    root = Tk()
    root.title("gmsaw tools")
    make_tables()
    
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=True)
    
    home_page(main_frame)
    
    root.mainloop()