import requests
import json
from tkinter import *

#функция для получения информации с entry
def func_exchange():
    code = e.get().upper()
    if code:
        answer = requests.get("https://open.er-api.com/v6/latest/RUB")
        json_info = answer.json()
        if code in json_info["rates"]:
            rez = json_info["rates"][code]
            content_l.config(text=f"1 RUB - {rez} {code}")
            content_l.config(fg="green")
        else:
            content_l.config(text=f"Кода валюты {code} не найдено")
            content_l.config(fg="red")
    else:
        content_l.config(text=f"Кода валюты не введен")
        content_l.config(fg="red")

window = Tk()
window.title("Курс валют")
window.geometry("400x400")

#Vvod valuti
e = Entry(window)
e.pack()

content_l = Label(window)
content_l.pack()

btn = Button(window, text="Получить курс рубля", command=func_exchange)
btn.pack()

window.mainloop()
