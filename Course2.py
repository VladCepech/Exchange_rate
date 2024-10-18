import requests
from tkinter import *
from tkinter import ttk

currency_dict = {
    "RUB": "Российский рубль",
    "AED": "Дирхам ОАЭ",
    "AFN": "Афгани",
    "ALL": "Албанский лек",
    "AMD": "Армянский драм",
    "ANG": "Нидерландский антильский гульден",
    "AOA": "Ангольская кванза",
    "ARS": "Аргентинское песо",
    "AUD": "Австралийский доллар",
    "AWG": "Арубанский флорин",
    "AZN": "Азербайджанский манат",
    "BAM": "Конвертируемая марка Боснии и Герцеговины",
    "BBD": "Барбадосский доллар",
    "BDT": "Бангладешская така",
    "BGN": "Болгарский лев",
    "BHD": "Бахрейнский динар",
    "BIF": "Бурундийский франк",
    "BMD": "Бермудский доллар",
    "BND": "Брунейский доллар",
    "BOB": "Боливийский боливиано",
    "BRL": "Бразильский реал",
    "BSD": "Багамский доллар",
    "BTN": "Бутанский нгултрум",
    "BWP": "Ботсванская пула",
    "BYN": "Белорусский рубль",
    "BZD": "Белизский доллар",
    "CAD": "Канадский доллар",
    "CDF": "Конголезский франк",
    "CHF": "Швейцарский франк",
    "CLP": "Чилийское песо",
    "CNY": "Китайский юань",
    "COP": "Колумбийское песо",
    "CRC": "Костариканский колон",
    "CUP": "Кубинское песо",
    "CVE": "Эскудо Кабо-Верде",
    "CZK": "Чешская крона",
    "DJF": "Франк Джибути",
    "DKK": "Датская крона",
    "DOP": "Доминиканское песо",
    "DZD": "Алжирский динар",
    "EGP": "Египетский фунт",
    "ERN": "Эритрейская накфа",
    "ETB": "Эфиопский быр",
    "EUR": "Евро",
    "FJD": "Доллар Фиджи",
    "FKP": "Фунт Фолклендских островов",
    "FOK": "Фарерская крона",
    "GBP": "Британский фунт стерлингов",
    "GEL": "Грузинский лари",
    "GGP": "Фунт Гернси",
    "GHS": "Ганский седи",
    "GIP": "Гибралтарский фунт",
    "GMD": "Гамбийский даласи",
    "GNF": "Гвинейский франк",
    "GTQ": "Гватемальский кетсаль",
    "GYD": "Гайанский доллар",
    "HKD": "Гонконгский доллар",
    "HNL": "Гондурасская лемпира",
    "HRK": "Хорватская куна",
    "HTG": "Гаитянский гурд",
    "HUF": "Венгерский форинт",
    "IDR": "Индонезийская рупия",
    "ILS": "Израильский шекель",
    "IMP": "Фунт Острова Мэн",
    "INR": "Индийская рупия",
    "IQD": "Иракский динар",
    "IRR": "Иранский риал",
    "ISK": "Исландская крона",
    "JEP": "Фунт Джерси",
    "JMD": "Ямайский доллар",
    "JOD": "Иорданский динар",
    "JPY": "Японская иена",
    "KES": "Кенийский шиллинг",
    "KGS": "Киргизский сом",
    "KHR": "Камбоджийский риель",
    "KID": "Доллар Кирибати",
    "KMF": "Франк Комор",
    "KRW": "Южнокорейская вона",
    "KWD": "Кувейтский динар",
    "KYD": "Доллар Каймановых островов",
    "KZT": "Казахстанский тенге",
    "LAK": "Лаосский кип",
    "LBP": "Ливанский фунт",
    "LKR": "Шри-ланкийская рупия",
    "LRD": "Либерийский доллар",
    "LSL": "Лоти Лесото",
    "LYD": "Ливийский динар",
    "MAD": "Марокканский дирхам",
    "MDL": "Молдавский лей",
    "MGA": "Малагасийский ариари",
    "MKD": "Северомакедонский динар",
    "MMK": "Мьянманский кьят",
    "MNT": "Монгольский тугрик",
    "MOP": "Патака Макао",
    "MRU": "Мавританская угия",
    "MUR": "Маврикийская рупия",
    "MVR": "Мальдивская руфия",
    "MWK": "Малавийская квача",
    "MXN": "Мексиканское песо",
    "MYR": "Малайзийский ринггит",
    "MZN": "Мозамбикский метикал",
    "NAD": "Намибийский доллар",
    "NGN": "Нигерийская найра",
    "NIO": "Никарагуанская кордоба",
    "NOK": "Норвежская крона",
    "NPR": "Непальская рупия",
    "NZD": "Новозеландский доллар",
    "OMR": "Оманский риал",
    "PAB": "Панамский бальбоа",
    "PEN": "Перуанский соль",
    "PGK": "Кина Папуа-Новой Гвинеи",
    "PHP": "Филиппинское песо",
    "PKR": "Пакистанская рупия",
    "PLN": "Польский злотый",
    "PYG": "Парагвайский гуарани",
    "QAR": "Катарский риал",
    "RON": "Румынский лей",
    "RSD": "Сербский динар",
    "RWF": "Франк Руанды",
    "SAR": "Саудовский риал",
    "SBD": "Доллар Соломоновых островов",
    "SCR": "Сейшельская рупия",
    "SDG": "Суданский фунт",
    "SEK": "Шведская крона",
    "SGD": "Сингапурский доллар",
    "SHP": "Фунт Святой Елены",
    "SLE": "Леоне Сьерра-Леоне",
    "SLL": "Сьерра-леонский леоне",
    "SOS": "Сомалийский шиллинг",
    "SRD": "Суринамский доллар",
    "SSP": "Южносуданский фунт",
    "STN": "Добра Сан-Томе и Принсипи",
    "SYP": "Сирийский фунт",
    "SZL": "Свазилендский лилангени",
    "THB": "Тайский бат",
    "TJS": "Таджикский сомони",
    "TMT": "Туркменский манат",
    "TND": "Тунисский динар",
    "TOP": "Паанга Тонга",
    "TRY": "Турецкая лира",
    "TTD": "Доллар Тринидада и Тобаго",
    "TVD": "Доллар Тувалу",
    "TWD": "Тайваньский доллар",
    "TZS": "Танзанийский шиллинг",
    "UAH": "Украинская гривна",
    "UGX": "Угандийский шиллинг",
    "USD": "Доллар США",
    "UYU": "Уругвайское песо",
    "UZS": "Узбекский сум",
    "VES": "Венесуэльский боливар",
    "VND": "Вьетнамский донг",
    "VUV": "Вату Вануату",
    "WST": "Тала Самоа",
    "XAF": "Франк КФА BEAC",
    "XCD": "Восточно-карибский доллар",
    "XDR": "СПЗ (Специальные права заимствования)",
    "XOF": "Франк КФА BCEAO",
    "XPF": "Французский тихоокеанский франк",
    "YER": "Йеменский риал",
    "ZAR": "Южноафриканский рэнд",
    "ZMW": "Замбийская квача",
    "ZWL": "Зимбабвийский доллар"
}

#Функция для получения списка кодов валют
def generation_list_rates():
    answer = requests.get(f"https://open.er-api.com/v6/latest/RUB")
    json_info = answer.json()
    list_currency = list(json_info["rates"].keys())
    return list_currency

#Функция конвертации
def func_exchange():
    code_target = combo_to.get()
    code_base = combo_from.get()
    code_base_second = combo_from_second.get()
    sum_f = float(sum_from.get())
    sum_fs = float(sum_from_second.get())
    if code_target and code_base and code_base_second:
        answer = requests.get(f"https://open.er-api.com/v6/latest/{code_base}")
        answer_second = requests.get(f"https://open.er-api.com/v6/latest/{code_base_second}")
        json_info = answer.json()
        json_info_second = answer_second.json()
        if code_target in json_info["rates"] and code_target in json_info_second["rates"]:
            rez = json_info["rates"][code_target]
            sum_rez = float(rez) * sum_f
            rez_second = json_info_second["rates"][code_target]
            sum_rez_second = float(rez_second) * sum_fs
            content_l.config(text=f"{sum_f} {code_base} - {sum_rez} {code_target} \n {sum_fs} {code_base_second} - {sum_rez_second} {code_target} ")
            content_l.config(fg="green")
        else:
            content_l.config(text=f"Кода валюты {code_target} не найдено")
            content_l.config(fg="red")
    else:
        content_l.config(text=f"Код валюты не выбран")
        content_l.config(fg="red")

#Функция для обновления данных лейбла при выборе базовой валюты
def update_from_label(event):
    # Получаем полное название базовой валюты из словаря и обновляем метку
    code = combo_from.get()
    if code in currency_dict:
        name = currency_dict[code]
        curr_from_name.config(text=name)
    else:
        curr_from_name.config(text="Код валюты не найден")

def update_from_label_second(event):
    # Получаем полное название базовой валюты из словаря и обновляем метку
    code = combo_from_second.get()
    if code in currency_dict:
        name = currency_dict[code]
        curr_from_name_second.config(text=name)
    else:
        curr_from_name_second.config(text="Код валюты не найден")

def update_to_label(event):
    # Получаем полное название целевой валюты из словаря и обновляем метку
    code = combo_to.get()
    if code in currency_dict:
        name = currency_dict[code]
        curr_to_name.config(text=name)
    else:
        curr_to_name.config(text="Код валюты не найден")

window = Tk()
window.title("Курс валют")
window.geometry("400x500")

#Запускаем функцию создания списка из кодов валют - в переменную sp_currency
sp_currency = generation_list_rates()

#Лэйбл для отображения текста для выбора базовой валюты
t_m_from = Label(window, text="Выберите код базовой валюты 1:")
t_m_from.pack(pady = [10,10])

#Выпадающий список для выбора базовой валюты
combo_from = ttk.Combobox(window, values=sp_currency)
combo_from.pack(pady = [10,0])
combo_from.bind("<<ComboboxSelected>>", update_from_label)

#Лэйбл для отображения текста для ввода суммы базовой валюты
t_m_from = Label(window, text="Введите сумму базовой валюты 1:")
t_m_from.pack(pady = [10,10])
#Ввод суммы для первой базовой валюты для конвертации
sum_from = Entry(window)
sum_from.pack()

#Лэйбл для отображения названия выбранной базовой валюты
curr_from_name = Label(window)
curr_from_name.pack(pady = [0,10])

#Лэйбл для отображения текста для выбора базовой валюты 2
t_m_from_second = Label(window, text="Выберите код базовой валюты 2:")
t_m_from_second.pack(pady = [10,10])

#Выпадающий список для выбора базовой валюты
combo_from_second = ttk.Combobox(window, values=sp_currency)
combo_from_second.pack(pady = [10,0])
combo_from_second.bind("<<ComboboxSelected>>", update_from_label_second)

#Лэйбл для отображения текста для ввода суммы базовой валюты 2
t_m_from = Label(window, text="Введите сумму базовой валюты 2:")
t_m_from.pack(pady = [10,10])
#Ввод суммы для второй базовой валюты для конвертации
sum_from_second = Entry(window)
sum_from_second.pack()

#Лэйбл для отображения названия выбранной базовой валюты
curr_from_name_second = Label(window)
curr_from_name_second.pack(pady = [0,10])

#Лэйбл для отображения текста для выбора целевой валюты
t_m_to = Label(window, text="Выберите код целевой валюты:")
t_m_to.pack(pady = [10,10])

#Выпадающий список для выбора валюты в которую переводим
combo_to = ttk.Combobox(window, values=sp_currency)
combo_to.pack(pady = [10,0])
combo_to.bind("<<ComboboxSelected>>", update_to_label)

#Лэйбл для отображения названия выбранной целевой валюты
curr_to_name = Label(window)
curr_to_name.pack(pady = [0,10])

#Лэйбл для отображения результата конвертации
content_l = Label(window)
content_l.pack(pady = [10,10])

#Кнопка для конвертации
btn = Button(window, text="Конвертировать валюту", command=func_exchange)
btn.pack(pady = [10,10])

window.mainloop()
