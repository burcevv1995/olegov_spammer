import datetime
import time
import tkinter
from datetime import datetime
from threading import *

from telethon import TelegramClient, events, sync  # подключение либ
import customtkinter
from tkinter import filedialog

adresses= ""


file_name = ""

MASSAGE_COUNTER = 100
START_TIME = datetime.now()
STOP = False



def open_file(): #функция для открытия файла с говном
    global adresses
    file_name = filedialog.askopenfilename(title="Выберите файл списка чатов")
    show_input_file_label.configure(text="Путь к файлу:"+file_name)
    file = open(file_name, "r")
    adresses = file.readlines()
    for adress in adresses:
      adresses_tbox.insert("0.0", adress + "\n")
    file.close()

class Client: # класс для работы с api телеги

    def __init__(self, id: int, hash: str, number: str,):
        self.id = id
        self.hash = hash
        self.number = number
        self.cl = TelegramClient("anon", self.id, self.hash)
        self.code = 0
client = ""
def connect(): # функция, что выполняется по кнопке подключиться
    global client
    client = Client(int(id_tbox.get()), hash_entry.get(), number_tbox.get())
    client.cl.start(phone=client.number)






app = customtkinter.CTk()   #Гуишка
app.geometry("620x780")
app.title("Telegram spamer for Oleg xD")
auth_label = customtkinter.CTkLabel(text = "Авторизация", master = app)
auth_label.grid(row=0, column = 0, columnspan=2, rowspan=2)
number_label = customtkinter.CTkLabel(text = "Номер или логин", master=app)
number_label.grid(row = 2, column = 0)
id_label = customtkinter.CTkLabel(text = "ID", master= app)
id_label.grid(row = 2, column = 1)
number_tbox = customtkinter.CTkEntry(master=app)
number_tbox.insert(0, "+79969791740")
number_tbox.grid(row = 3, column = 0)
id_tbox = customtkinter.CTkEntry(master = app)
id_tbox.insert(0, "26512163" )
id_tbox.grid(row = 3, column = 1)
input_file_label = customtkinter.CTkLabel(master = app, text = "Выбор файла со списком чатов")
input_file_label.grid(row = 0, column = 3)
show_input_file_label = customtkinter.CTkLabel(master= app, text="Путь к файлу:")
show_input_file_label.grid(row = 1, column = 3, rowspan=3)
open_file_btn = customtkinter.CTkButton(master=app, text="Выбрать файл", command = open_file)
open_file_btn.grid(row = 2, column = 3, rowspan=5)
adresses_tbox = customtkinter.CTkTextbox(master=app, width=300, height=400)
adresses_tbox.grid(row = 6, column = 3, rowspan=6)
code_label= customtkinter.CTkLabel(master=app, text="Код")
code_label.grid(row=4, column=0)
hash_label = customtkinter.CTkLabel(master=app, text="Hash")
hash_label.grid(row=4, column=1)
code_entry = customtkinter.CTkEntry(app)
code_entry.grid(row=5, column = 0)
hash_entry= customtkinter.CTkEntry(master=app)
hash_entry.insert(0,"4e5efe9b46143d92b03c94d9e6f3e49d" )
hash_entry.grid(row=5, column = 1)
connect_btn = customtkinter.CTkButton(master=app, text="Подключиться", command=connect)
connect_btn.grid(row=6, column = 0)

connect_logs_tbox = customtkinter.CTkTextbox(master=app, width=300, height=100)
connect_logs_tbox.grid(row=7, column=0, columnspan=2)
null_label = customtkinter.CTkLabel(master=app, text="     ")
null_label.grid(row=0, column=2)
massage_label = customtkinter.CTkLabel(master=app, text="Сообщение")
massage_label.grid(row=8, column=0, columnspan=2)
massage_tbox = customtkinter.CTkTextbox(master=app, width=300)
massage_tbox.grid(row=9, column=0, columnspan=2)
main_logs_lable = customtkinter.CTkLabel(master=app, text="Логи работы приложения")
main_logs_lable.grid(row=16, column=0, columnspan=4)
main_logs_tbox = customtkinter.CTkTextbox(master=app)
main_logs_tbox.grid(row=17, column=0, columnspan = 4, sticky = "we")



def send_massage(): # функция, которая выполняется по кнопке старт
    global client
    global adresses
    global MASSAGE_COUNTER
    global START_TIME
    if MASSAGE_COUNTER >0:
        main_logs_tbox.insert("0.0", "Начата отправка сообщений \n")
        for adress in adresses:
            client.cl.send_message(adress, massage_tbox.get("1.0", tkinter.END))

            main_logs_tbox.insert("end", "Отправлено сообщение по адресу " + adress + "\n")
            MASSAGE_COUNTER = MASSAGE_COUNTER-1
            current_data = datetime.now()
            if START_TIME.date() < current_data.date() or START_TIME.month<current_data.month:
                MASSAGE_COUNTER = 100
                START_TIME = datetime.now



disconnect_btn = customtkinter.CTkButton(master=app, text="Старт", command=send_massage)
disconnect_btn.grid(row =6, column= 1)








if __name__ == '__main__': #запуск gui
    main_thread(app.mainloop()).start()




