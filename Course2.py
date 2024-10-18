import requests
import json
from tkinter import *
from tkinter import ttk

def generation_list_rates():
    list_currency = []
    answer = requests.get("https://open.er-api.com/v6/latest/RUB")
    json_info = answer.json()
    # i in json_info["rates"].keys():
    #    list_currency.append(i)
    list_currency = list(json_info["rates"].keys())
    return list_currency

#функция для получения информации с entry
def func_exchange():
    code = combo.get().upper()
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

#list_currency = ["RUB", "EUR", "USD", "GBP", "JPY", "CNY", "CHF", "CAD", "AUD", "NZD", "SEK", "NOK", "BRL", "INR", "KRW", "MXN"]
sp_currency = generation_list_rates()

t_m = Label(window, text="Выберите код валюты:")
t_m.pack(pady = [10,10])

combo = ttk.Combobox(window, values=sp_currency)
combo.pack(pady = [10,10])

content_l = Label(window)
content_l.pack(pady = [10,10])

btn = Button(window, text="Получить курс рубля", command=func_exchange)
btn.pack(pady = [10,10])

window.mainloop()

print(sp_currency)