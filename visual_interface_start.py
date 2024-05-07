import tkinter
from tkinter import *
import datetime
from time import strftime
from dateutil.relativedelta import relativedelta

bok = 0
index = 0
datum = 0
index2 = 0
# //////////////////////////////////////////////////

root = Tk()
root.title("Ev3 mindstorm controle panel")
root.state("zoomed")
# bg = PhotoImage(file="C:\\Users\\Paul Kviding\\Desktop\\21303.png")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

bild_labul = Label(root)
bild_labul.place(x=0, y=0, relwidth=1, relheight=1)

# //////////////////////////////////////////////////
# filhantering titel; ny rad ålånad (N,Y)


def ta_bort_text():
    den_fins_redan_text.place_forget()
    den_fins_inte_text.place_forget()
    den_fins_text.place_forget()
    den_har_blevit_tillagd.place_forget()
    boken_fins_men_är_utlånad.place_forget()
    boken_har_blevit_utlånad.place_forget()
    boken_har_blevit_tilbaka_leamnad.place_forget()
    boken_fins_och_är_tilbakalämnad.place_forget()


# rot.bind gör att när enter tryks så sher enter
root.bind("<Return>")

e1 = tkinter.Entry(root)


def exit():
    root.destroy()


root.bind("<Escape>", lambda x: exit())


def my_time():
    time_string = strftime("%H:%M:%S %p \n %x")  # time format
    l1.config(text=time_string)
    l1.after(1000, my_time)  # time delay of 1000 milliseconds


l1 = Label(root, font=("Helvetica", 40))

my_time()

# //////////////////////////////////////////////////
# ,command=lambda:

boken_fins_men_är_utlånad = Label(
    root,
    text="boken är tuvär utlånad",
    width=25,
    height=2,
    bg="red",
    font=("Helvetica", 25),
)

boken_fins_och_är_tilbakalämnad = Label(
    root,
    text="boken är redan tilbakalemnad",
    width=25,
    height=2,
    bg="red",
    font=("Helvetica", 25),
)

den_fins_redan_text = Label(
    root,
    text="dena book fins redan",
    width=25,
    height=2,
    bg="red",
    font=("Helvetica", 25),
)

den_fins_inte_text = Label(
    root,
    text="dena book fins inte",
    width=25,
    height=2,
    bg="red",
    font=("Helvetica", 25),
)

den_fins_text = Label(
    root, text="dena book fins", width=25, height=2, bg="green", font=("Helvetica", 25)
)

boken_har_blevit_utlånad = Label(
    root,
    text="boken har blevit utlånad till dig",
    width=25,
    height=2,
    bg="green",
    font=("Helvetica", 25),
)

boken_har_blevit_tilbaka_leamnad = Label(
    root,
    text="boken har blevit tilbaka lemnad",
    width=25,
    height=2,
    bg="green",
    font=("Helvetica", 25),
)

den_har_blevit_tillagd = Label(
    root,
    text="booken har blevit telagd",
    width=25,
    height=2,
    bg="green",
    font=("Helvetica", 25),
)

text = Label(
    root,
    text="Ev3 controle panel",
    width=25,
    height=2,
    bg="gray",
    font=("Helvetica", 50),
)

button_up = tkinter.Button(root, text="▲", font=("Helvetica", 25))

button_down = tkinter.Button(root, text="▼", font=("Helvetica", 25))

button_write = tkinter.Button(
    root,
    text="►",
    font=("Helvetica", 25),
)

button_left = tkinter.Button(root, text="◄", font=("Helvetica", 25))

buton_avsluta = tkinter.Button(
    root, text="avsluta", font=("Helvetica", 50), bg="red", command=lambda: exit()
)

# //////////////////////////////////////////////////

buton_avsluta.pack(pady=5, side=BOTTOM, anchor="ne")

button_up.place(x=screen_width // 2, y=(screen_height // 2) - 100)

button_down.place(x=screen_width // 2, y=(screen_height // 2) + 100)

button_write.place(x=(screen_width // 2) + 100, y=screen_height // 2)

button_left.place(x=(screen_width // 2) - 100, y=screen_height // 2)

text.pack()

l1.place(x=0, y=(screen_height // 1.4))


# //////////////////////////////////////////////////

root.mainloop()
