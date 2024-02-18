from tkinter import *
from database import *
from tkinter import messagebox
from cornell import main
    
def delete_page():
    for frame in main_frame.winfo_children():
        frame.destroy()

def data_page(frame, pos):
    
    data_frame = Frame(frame)
    data_frame.pack(fill=BOTH, expand=True)
    print(pos)
    
    def back():
        delete_page()
        notes_page(frame, pos)
    
    def convert():
        delete_page()
        convert_page(frame, pos)
        # try:
        #     building(data)
        #     messagebox.showinfo(title="convert", message="convert sucsess :)")
        # except:
        #     messagebox.showerror(title="error", message="ERROROROROROOROROR")
    
    data = note_reveal(pos)
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

def notes_page(frame, pos):
    def back_home():
        delete_page()
        home_page(frame)
        
    def showdata():
        delete_page()
        data_page(frame, pos)
        
    def submit():
        note_data = e_note.get()
        keynote_data = e_keynote.get()
        
        if note_data == "" and keynote_data == "":
            messagebox.showinfo(title="error", message="Input kosong")
        else:
            add(pos, note_data, keynote_data, current_time)
            print("Data berhasil ditambahkan")
            e_note.delete(0, END)
            e_keynote.delete(0, END)

    print(pos)
    
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
    
    b_home = Button(note_frame, text="Back to Home", command=back_home, pady=5, padx=5)
    b_home.grid(row=5, column=0, columnspan=2, pady=30)

def convert_page(frame, pos):
    convert_frame = Frame(frame)
    convert_frame.pack(fill=BOTH, expand=True)
    
    def select(event):
        select_label = clicked.get()  # Mendapatkan label yang dipilih
        for item in template:
            if item[0] == select_label:  # Mencari label yang sesuai di list template
                source = item[1]  # Mengambil path file yang sesuai
                print(source)
                return source  # Mengembalikan path file yang dipilih
        return None  # Jika tidak ada template yang dipilih, mengembalikan None

    def back():
        delete_page()
        data_page(frame, pos)
    
    def create():
        tmpltpath = select(None)  # Memanggil fungsi select tanpa event
        if tmpltpath is None or tmpltpath == "./":
            messagebox.showerror(title="error", message="Mohon Pilih Template")
        elif title_e.get() == "" or sub_e.get() == "" or source_e.get() == "":
            messagebox.showerror(title="error", message="Data Kosong")
        else:
            data = note_reveal(pos)
            title = title_e.get()
            sub = sub_e.get()
            source = source_e.get()
            title_e.delete(0, END)
            sub_e.delete(0, END)
            source_e.delete(0, END)
            
            main(data, title, sub, source, tmpltpath)
            messagebox.showinfo(title="info", message="succses")
        
    template_lb = Label(convert_frame, text="Template")
    template_lb.grid(row=0, column=0)
    title_lb = Label(convert_frame, text="Subject")
    title_lb.grid(row=1, column=0)
    sub_lb = Label(convert_frame, text="Sub Subject")
    sub_lb.grid(row=2, column=0)
    source_lb = Label(convert_frame, text="Qr Source")
    source_lb.grid(row=3, column=0)
    
    template = [
        ["Pilih Template", "./"],
        ["Cornell Template", "./template/cornell.docx"]
    ]
    
    clicked = StringVar()
    clicked.set(f"{template[0][0]}")
    
    template_o = OptionMenu(convert_frame, clicked, *[item[0] for item in template], command=select)
    template_o.grid(row=0, column=1)
    title_e = Entry(convert_frame, width=30)
    source_e = Entry(convert_frame, width=30)
    sub_e = Entry(convert_frame, width=30)
    title_e.grid(row=1, column=1)
    sub_e.grid(row=2, column=1)
    source_e.grid(row=3, column=1)
    
    cancel_btn = Button(convert_frame, text="Kembali", command=back, padx=20)
    cancel_btn.grid(row=4, column=0, pady=10, padx=5)
    
    create_btn = Button(convert_frame, text="Create", command=create, padx=20)
    create_btn.grid(row=4, column=1, pady=10, padx=5)
    
def home_page(frame):
    home_frame = Frame(frame)
    home_frame.pack(fill=BOTH, expand=True)
    
    def newfile():
        delete_page()
        file_info(frame)
        
    def load():
        delete_page()
        load_page(frame)
    
    main_frame = Frame(home_frame, height=50, width=100)
    main_frame.pack()
    
    new_btn = Button(main_frame, text="New File", pady=10, padx=25, command=newfile)
    new_btn.pack(pady=5)
    load_btn = Button(main_frame, text="Load File", pady=10, padx=25, command=load)
    load_btn.pack(pady=5)
    
    history_frame= Frame(home_frame, height=200, width=100)
    history_frame.pack()
    
def file_info(frame):
    def submit():
        title = e_filename.get()
        if title == "":
            messagebox.showinfo(title="error", message="File Name Kosong")
        else:
            delete_page()
            pos = new_data()
            new_file(title, current_time, pos)
            notes_page(frame, pos)
    
    def back():
        delete_page()
        home_page(frame)
    
    file_frame = Frame(frame, height=100)
    file_frame.pack()
    
    l_filename = Label(file_frame, text="File Name: ")
    l_filename.pack()
    e_filename = Entry(file_frame, width=30)
    e_filename.pack()
    
    b_submit = Button(file_frame, text="Submit", command=submit, pady=5, padx=15)
    b_submit.pack()
    
    b_back = Button(file_frame, text="Back", command= back, padx=20, pady=5)
    b_back.pack()
    
def load_page(frame):
    def back():
        delete_page()
        home_page(frame)
        
    def load(pos):
        delete_page()
        notes_page(frame, pos)
        print(f"loaded {pos}")
    
    def delete(rowid):
        respond = messagebox.askyesno(title="commit", message="Are You Sure?")
        print(f"user say {respond}")
        if respond == True:
            print(f"Deleted {rowid}")
            delete_file(rowid, item[3])
            delete_page()
            load_page(frame)
    
    load_frame = Frame(frame)
    load_frame.pack(fill=BOTH, expand=True)
    file_list_frame = Frame(load_frame, padx=100)
    file_list_frame.pack()
    command_frame = Frame(load_frame)
    command_frame.pack()
    
    data = file_reveal()
    for item in data:
        rowid = item[0]
        file_item_frame = Frame(file_list_frame, pady=10)
        file_item_frame.pack()
        
        file_item1 = Label(file_item_frame, text=f"{item[1]}", padx=20)
        file_item1.grid(row=0, column=0)
        file_item2 = Label(file_item_frame, text=f"{time_convert(time=item[2])}", padx= 20)
        file_item2.grid(row=0, column=1)
        file_load_command = Button(file_item_frame, text="Load", command=lambda pos=item[3]: load(pos))
        file_load_command.grid(row=0, column=2, sticky="e")
        file_delete_command = Button(file_item_frame, text="Delete", command=lambda rowid=rowid: delete(rowid))
        file_delete_command.grid(row=0, column=3)
        
    back_button = Button(command_frame, text="Back", command=back)
    back_button.pack()
    
if __name__ == "__main__":
    root = Tk()
    root.title("gmsaw tools")
    # make_tables()
    
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=True)
    
    home_page(main_frame)
    
    root.mainloop()