from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from PIL import ImageTk,Image

hunians = []
hunians.append(Apartemen("Nelly Joy", 3, 3, "apartemen.jpg", "Monstadt, Teyvat"))
hunians.append(Rumah("Sekar MK", 5, 2, "rumah.png", "Narukami Island, Inazuma, Teyvat"))
hunians.append(Indekos("Bp. Romi", "Cahya", "indekos.png", "Liyue, Teyvat"))
hunians.append(Rumah("Satria", 1, 4, "rumah2.png", "Spring Vale, Monstadt, Teyvat"))

def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    image_path = "img/" + hunians[index].get_image()
    image = Image.open(image_path).resize((300, 200))
    photo = ImageTk.PhotoImage(image)
    img_label = Label(d_frame, image=photo)
    img_label.photo = photo
    img_label.pack()

    d_summary = Label(d_frame, text="Summary\n" + hunians[index].get_detail()+ hunians[index].get_alamat() + hunians[index].get_summary() + "\n" + hunians[index].get_dokumen(), anchor="w", justify=LEFT)
    d_summary.pack()

    btn = LabelFrame(top, padx=0, pady=0)
    btn.pack(padx=10, pady=10)
    b_close = Button(btn, text="Close", command=top.destroy)
    b_close.grid(row=0, column=0)


def mainpage():
    landing_window.destroy()
    root = Tk()
    root.title("Praktikum DPBO Python")

    img = Image.open("img/inazuma.jpg")
    img = img.resize((500, 300))
    photo = ImageTk.PhotoImage(img)
    img_main = Label(root, image=photo)
    img_main.pack()
    
    frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    opts = LabelFrame(root, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    b_add = Button(opts, text="Add Data", state="disabled")
    b_add.grid(row=0, column=0)

    b_exit = Button(opts, text="Exit", command=root.quit)
    b_exit.grid(row=0, column=1)

    for index, h in enumerate(hunians):
        idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index, column=1)

        if h.get_jenis() != "Indekos": 
            name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)
        else:
            name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)

        b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
        b_detail.grid(row=index, column=3)
    root.mainloop()
    



landing_window = Tk()
landing_window.title("Landing Page")

image = Image.open("img/hutao.png")
photo = ImageTk.PhotoImage(image)
img_landing = Label(landing_window, image=photo)
img_landing.pack()

title_landing = Label(landing_window, text="This is Landing Page", font=("Arial", 25), pady=10)
title_landing.pack()

enter_button = Button(landing_window, text="Cek data Residen", command=mainpage)
enter_button.pack(pady=10)

landing_window.mainloop()