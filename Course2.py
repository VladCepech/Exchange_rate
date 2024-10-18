import requests
import json
from tkinter import *
from tkinter import ttk

def generation_list_rates():
    #list_currency = []
    #code_base = combo_from.get()
    answer = requests.get(f"https://open.er-api.com/v6/latest/RUB")
    json_info = answer.json()
    #for i in json_info["rates"].keys():
    #    list_currency.append(i)
    list_currency = list(json_info["rates"].keys())
    return list_currency

#функция для получения информации с entry
def func_exchange():
    code_target = combo_to.get()
    code_base = combo_from.get()
    if code_base and code_target:
        answer = requests.get(f"https://open.er-api.com/v6/latest/{code_base}]")
        json_info = answer.json()
        if code_target in json_info["rates"]:
            rez = json_info["rates"][code_target]
            content_l.config(text=f"1 {code_base} - {rez} {code_target}")
            content_l.config(fg="green")
        else:
            content_l.config(text=f"Кода валюты {code_target} не найдено")
            content_l.config(fg="red")
    else:
        content_l.config(text=f"Кода валюты не введен")
        content_l.config(fg="red")

window = Tk()
window.title("Курс валют")
window.geometry("400x400")

#list_currency = ["RUB", "EUR", "USD", "GBP", "JPY", "CNY", "CHF", "CAD", "AUD", "NZD", "SEK", "NOK", "BRL", "INR", "KRW", "MXN"]
sp_currency = generation_list_rates()

t_m_from = Label(window, text="Выберите код базовой валюты:")
t_m_from.pack(pady = [10,10])

combo_from = ttk.Combobox(window, values=sp_currency)
combo_from.pack(pady = [10,10])

t_m_to = Label(window, text="Выберите код валюты перевода:")
t_m_to.pack(pady = [10,10])

combo_to = ttk.Combobox(window, values=sp_currency)
combo_to.pack(pady = [10,10])

content_l = Label(window)
content_l.pack(pady = [10,10])

btn = Button(window, text="Конвертировать валюту", command=func_exchange)
btn.pack(pady = [10,10])

window.mainloop()
