from random import random, randint
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo

file = open("city.txt", "r", encoding='utf-8',)
baseline = file.readlines()
file.seek(0,0)

base = []
n = 0
a = 0
c = 0

root = Tk()
root.title("Игра Города")
root.geometry("600x300+650+350")
root.resizable(False, False)

label = ttk. Label(text = "Добро пожаловать в игру Города!")
label.pack()

def finish():
    root.destroy()
root.protocol("WM_DELETE_WINDOW", finish)

def clear_entry():
    entry.delete(0, END)

def clear_variable():
    c = 0
    base.clear()
    line = ""
    eline = ""
    e_player = ""

def poisk_goroda():
    global line, eline, e_player, a, c
    if line[-2] == player[0] or eline[-1] == player[0] or c == 1:
            base.append(player.title() + "\n")
            if e_player != "void":
                while e_player[-1].title() != line[0] or line in base:
                    line = file.readline()
                    if line == "":
                        editor.insert(END,"Компьютер проиграл!\n\
Начните игру заново!")
                        return
                file.seek(0,0)
            else:
                while player[-1].title() != line[0] or line in base:
                    line = file.readline()
                    if line == "":
                        editor.insert(END,"Компьютер проиграл!\n\
Начните игру заново!")
                        return
            file.seek(0,0)
            base.append(line)
            editor.insert(END, "Город: ")
            editor.insert(END,line)
            if line[-2] == "ы" or line[-2] == "ь":
                a = 1
                eline = line[:-2]
            else: a = 0

def proverka_player():
    global e_player, c, eline
    if c == 1:
        e_player = "void"
        if player[-1] == "ь" or player[-1] == "ы":
            e_player = player[:-1]
        bplayer = player.title() + "\n"
        poisk_goroda()
        return
    e_player = "void"
    m = 0
    if player[-1] == "ь" or player[-1] == "ы":
        e_player = player[:-1]
    bplayer = player.title() + "\n"
    if not bplayer in baseline:
        editor.insert(END, "Нет такого города в базе \n")
        m = 1
    pplayer = player.title() + "\n"
    if pplayer in base:
        editor.insert(END, "Этот город уже был назван \n")
        m = 1
    if a == 1:
        if eline[-1] != player[0]:
            editor.insert(END, "Последняя буква не совпадает с городом \n")
            m = 1
    elif line[-2] != player[0]:
            editor.insert(END, "Последняя буква не совпадает с городом \n")
            m = 1
    if m == 0: poisk_goroda()

def show_console():
    global player
    player = entry.get()
    editor.configure(state='normal')
    editor.insert(END, "Ваш город: ")
    editor.insert(END, player + "\n")
    proverka_player()
    editor.configure(state='disabled')
    editor.see("end")
    clear_entry()

def show_console_enter(self):
    global player
    player = entry.get()
    editor.configure(state='normal')
    editor.insert(END, "Ваш город: ")
    editor.insert(END, player + "\n")
    proverka_player()
    editor.configure(state='disabled')
    editor.see("end")
    clear_entry()

button_ready = ttk.Button(text="Готово", command = show_console)
button_ready.place(x = 500, y = 250)
entry = ttk.Entry()
entry.place(x = 60 , y = 252, width = 410)
entry.bind("<Return>", show_console_enter)
label_1 = ttk.Label(text = "Поле :")
label_1.place(x = 10, y = 20)
label_2 = ttk.Label(text = "Строка:")
label_2.place(x = 10, y = 252)
con_text = StringVar()
editor = Text(state = DISABLED, background = "white", foreground = "black",
              font = 14, wrap = "word")
editor.place(x = 60, y = 20, height = 200, width=410)
editor.configure(state='normal')
editor.insert("1.0", "Чтобы начать игру нажмите <<Начать>> \n\
Вводите города с маленькими буквами!!!")
editor.configure(state='disabled')
yscroll = ttk.Scrollbar(orient = "vertical", command = editor.yview)
yscroll.place(x = 460, y = 20, height = 200)
editor["yscrollcommand"] = yscroll.set

def open_info(): 
    showinfo(title="Правила", message = "Игра для нескольких человек, в \
которой каждый участник в свою очередь называет реально существующий \
город России, название которого начинается на ту букву, которая \
оканчивается названием предыдущего города. \nЕсли последняя буква города \
ь или ы, то берется предпоследняя буква.")

info_button = ttk.Button(text="Правила", command=open_info)
info_button.place(x = 500, y = 60 )

def open_lose():
    showinfo(title="Проигрыш", message = "Вы проиграли, начните завново!")
    clear_entry()
    clear_variable()
    clear_con()
    editor.configure(state='normal')
    editor.insert("1.0", "Чтобы начать игру нажмите <<Начать>> \n\
Вводите города с маленькими буквами!!!")
    editor.configure(state='disabled')

def random():
    global a, n, line, eline
    r = randint(0, 1116)
    while n != r:
        line = file.readline()
        n += 1
    n = 0
    base.append(line)
    file.seek(0,0)
    if line[-2] == "ы" or line[-2] == "ь":
        a = 1
        eline = line[:-2]
    else: a = 0

def but_start_1():
    editor.configure(state='normal')
    random()
    editor.insert(END, "Компьютер начинает свой ход: ")
    editor.insert(END, line)
    editor.insert(END, "Введите город: \n")
    editor.configure(state='disabled')
    start.destroy()

def but_start_2():
    global line, eline, c
    editor.configure(state='normal')
    editor.insert(END, "Игрок начинает свой ход \nВведите Город: \n")
    line = "void"
    eline = "void"
    c = 1
    editor.configure(state='disabled')
    start.destroy()

def clear_con():
    clear_variable()
    editor.configure(state='normal')
    editor.delete("1.0", END)
    editor.configure(state='disabled')

def clear_sbros():
    clear_con()
    clear_variable()
    editor.configure(state='normal')
    editor.insert("1.0", "Чтобы начать игру нажмите <<Начать>> \n\
Вводите города с маленькими буквами!!!")
    editor.configure(state='disabled')

def open_start():
    global start
    clear_variable()
    start = Tk()
    start.geometry("500x150+700+420")
    start.title("Выбор хода")
    start.resizable(False, False)
    label_in_start = ttk.Label(start, text = "Кто будет начинать первым?",
                               font = 16)
    label_in_start.pack()
    button_in_start_1 = ttk.Button (start, text="Компьютер",
                                    command = but_start_1)
    button_in_start_1.place(x = 80, y = 60, height = 40, width=100)
    button_in_start_2 = ttk.Button (start, text="Игрок", command = but_start_2)
    button_in_start_2.place(x = 340, y = 60,height = 40, width=100)
    clear_con()
    
button_start = ttk.Button(text="Начать", command = open_start)
button_start. place (x = 500, y = 20)
button_start = ttk.Button(text="Сдаться", command = open_lose)
button_start. place (x = 500, y = 140)
button_clear = ttk.Button(text = "Сбросить", command = clear_sbros)
button_clear.place(x = 500, y = 100)

root.option_add("*tearOff", FALSE)
main_menu = Menu()
file_menu = Menu()
file_menu.add_command(label="Выход", command = finish)
main_menu.add_cascade(label = "Файл", menu=file_menu)
root.config(menu = main_menu)

root.mainloop()
