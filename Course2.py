import requests
import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb


# Функция для получения списка кодов валют
def generation_list_rates():
    answer = requests.get(f"https://open.er-api.com/v6/latest/RUB")
    json_info = answer.json()
    list_currency = list(json_info["rates"].keys())
    return list_currency


# Функция конвертации
def func_exchange():
    code_target = combo_to.get()
    code_base = combo_from.get()
    code_base_second = combo_from_second.get()
    if code_target and code_base and code_base_second:
        answer = requests.get(f"https://open.er-api.com/v6/latest/{code_base}")
        answer_second = requests.get(f"https://open.er-api.com/v6/latest/{code_base_second}")
        json_info = answer.json()
        json_info_second = answer_second.json()
        if code_target in json_info["rates"] and code_target in json_info_second["rates"]:
            rez = json_info["rates"][code_target]
            rez_second = json_info_second["rates"][code_target]
            content_l.config(
                text=f"1 {code_base} - {rez} {code_target} \n 1 {code_base_second} - {rez_second} {code_target} ")
            content_l.config(fg="green")
        else:
            content_l.config(text=f"Кода валюты {code_target} не найдено")
            content_l.config(fg="red")
    else:
        content_l.config(text=f"Код валюты не выбран")
        content_l.config(fg="red")


# Функция для обновления данных всех лэйблов при смене валют
def update_from_label(event):
    code_1 = combo_from.get()
    curr_from_name.config(text=currency_dict.get(code_1, 'неизвестное название'))
    code_2 = combo_from_second.get()
    curr_from_name_second.config(text=currency_dict.get(code_2, 'неизвестное название'))
    code_3 = combo_to.get()
    curr_to_name.config(text=currency_dict.get(code_3, 'неизвестное название'))


try:
    with open('currency_dict.txt', encoding='utf-8') as file:
        content = file.read()
        currency_dict = json.loads(content)
except FileNotFoundError:
    currency_dict = {'RUB': 'Российский рубль', 'USD': 'Доллар США', 'EUR': 'Евро',}
    mb.showerror('Ошибка!', 'Не найден файл с названиями валют!')


window = Tk()
window.title("Курс валют")
window.geometry("400x500")

# Запускаем функцию создания списка из кодов валют - в переменную sp_currency
sp_currency = generation_list_rates()

# Лэйбл для отображения текста для выбора базовой валюты
t_m_from = Label(window, text="Выберите код базовой валюты 1:")
t_m_from.pack(pady=(10, 10))

# Выпадающий список для выбора базовой валюты
combo_from = ttk.Combobox(window, values=sp_currency)
combo_from.current(146)
combo_from.pack(pady=(10, 0))
combo_from.bind("<<ComboboxSelected>>", update_from_label)

# Лэйбл для отображения названия выбранной базовой валюты
curr_from_name = Label(window)
curr_from_name.pack(pady=(0, 10))

# Лэйбл для отображения текста для выбора базовой валюты
t_m_from_second = Label(window, text="Выберите код базовой валюты 2:")
t_m_from_second.pack(pady=(10, 10))

# Выпадающий список для выбора базовой валюты
combo_from_second = ttk.Combobox(window, values=sp_currency)
combo_from_second.current(43)
combo_from_second.pack(pady=(10, 0))
combo_from_second.bind("<<ComboboxSelected>>", update_from_label)

# Лэйбл для отображения названия выбранной базовой валюты
curr_from_name_second = Label(window)
curr_from_name_second.pack(pady=(0, 10))

# Лэйбл для отображения текста для выбора целевой валюты
t_m_to = Label(window, text="Выберите код целевой валюты:")
t_m_to.pack(pady=(10, 10))

# Выпадающий список для выбора валюты в которую переводим
combo_to = ttk.Combobox(window, values=sp_currency)
combo_to.current(0)
combo_to.pack(pady=(10, 0))
combo_to.bind("<<ComboboxSelected>>", update_from_label)

# Лэйбл для отображения названия выбранной целевой валюты
curr_to_name = Label(window)
curr_to_name.pack(pady=(0, 10))

# Лэйбл для отображения результата конвертации
content_l = Label(window)
content_l.pack(pady=(10, 10))

# Кнопка для конвертации
btn = Button(window, text="Конвертировать валюту", command=func_exchange)
btn.pack(pady=(10, 10))

update_from_label(event=True)

window.mainloop()
