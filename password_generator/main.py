import tkinter
from tkinter import messagebox
import random


def funkc_ok():
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
         'v', 'w', 'x', 'y', 'z']
    b = ["/", ".", ",", "@", "&", "*", ")", "("]
    c = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "0"]
    text = a + b + c + a + b + c
    en_pass = ""
    en_website = ""
    en_username = ""
    entrywebsite = entry_website.get()
    entrypas = entry_pas.get()
    entryusername = entry_username.get()
    for i in range(len(entrypas)):
        cc = text.index(entrypas[i]) + 3
        en_pass += text[cc]

    for i in range(len(entrywebsite)):
        dd = text.index(entrywebsite[i]) + 3
        en_website += text[dd]

    for i in range(len(entryusername)):
        gg = text.index(entryusername[i]) + 3
        en_username += text[gg]

    with open("ImePas.txt", "a") as data:
        data.write(f"{en_website}, {en_username}, {en_pass}" + "\n")


def search():
    website = entry_website.get()
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
         'v', 'w', 'x', 'y', 'z']
    b = ["/", ".", ",", "@", "&", "*", ")", "("]
    c = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", '0']
    text = a + b + c + a + b + c
    en_web = ""
    with open("ImePas.txt", 'r') as d:
        data = d.readlines()
        rev_pas = ""
        rev_user = ""

        for y in range(len(website)):
            ccc = text.index(website[y]) + 3
            en_web += text[ccc]

            for x in range(len(data)):
                fir = data[x].split(",")[0].strip()
                sec = data[x].split(",")[1].strip()
                thi = data[x].split(",")[2].strip()

                if en_web == fir:
                    for h in range(len(sec)):
                        secc = text.index(sec[h]) - 3
                        rev_user += text[secc]

                    for k in range(len(thi)):
                        third = text.index(thi[k]) - 3
                        rev_pas += text[third]
                    entry_pas.insert(0, rev_pas)
                    entry_username.insert(0, rev_user)


def gen():
    import random
    a = ["a", "b", "c", "d", "e", "f", "g", "h", "x", "y"]
    b = ["/", ".", ",", "@", "&", "*", ")", "("]
    c = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", '0']
    text = a + b + c
    password = ""
    for i in range(8):
        password += random.choice(text)
    entry_pas.delete(0, tkinter.END)
    entry_pas.insert(0, password)


screen = tkinter.Tk()
screen.geometry("300x300")
screen.title("tkinter ")

canvas = tkinter.Canvas(screen, width=210, height=190)
canvas.grid(column=0, row=1, columnspan=2)

logo_image = tkinter.PhotoImage(file="logo.png")

canvas.create_image(150, 100, anchor=tkinter.CENTER, image=logo_image)

t = tkinter.Label(text="Website: ")
t.grid(column=0, row=2)

entry_website = tkinter.Entry()
entry_website.grid(column=1, row=2)

d = tkinter.Label(text="Username: ")
d.grid(column=0, row=3)

entry_username = tkinter.Entry()
entry_username.grid(column=1, row=3)

c = tkinter.Label(text="Password: ")
c.grid(column=0, row=4)

entry_pas = tkinter.Entry()
entry_pas.grid(column=1, row=4)

ok_button = tkinter.Button(text="Search", command=search)
ok_button.grid(column=0, row=5)

save_button = tkinter.Button(text="Save", command=funkc_ok)
save_button.grid(column=1, row=5)

generate_button = tkinter.Button(text="Generate", command=gen)
generate_button.grid(column=2, row=4)

screen.mainloop()
