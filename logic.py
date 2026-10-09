
N = 5

CONVERSIONS = {
    "Длина": {
        "Километры → мили": ("Километры", "мили", 0.621371),
        "Мили → километры": ("мили", "Километры", 1.60934),
        "Метры → футы": ("Метры", "футы", 3.28084),
        "Футы → метры": ("футы", "Метры", 0.3048),
        "Сантиметры → дюймы": ("Сантиметры", "дюймы", 0.393701),
        "Дюймы → сантиметры": ("дюймы", "Сантиметры", 2.54),
    },
    "Масса": {
        "Килограммы → фунты": ("Килограммы", "фунты", 2.20462),
        "Фунты → килограммы": ("фунты", "Килограммы", 0.453592),
        "Граммы → унции": ("Граммы", "унции", 0.035274),
        "Унции → граммы": ("унции", "Граммы", 28.3495),
    },
    "Температура": {
        "°C → °F": ("°C", "°F", None),
        "°F → °C": ("°F", "°C", None),
        "°C → K": ("°C", "K", None),
        "K → °C": ("K", "°C", None),
    },
    "Валюта": {
        "USD → KZT": ("USD", "KZT", None),
        "KZT → USD": ("KZT", "USD", None),
        "EUR → KZT": ("EUR", "KZT", None),
        "KZT → EUR": ("KZT", "EUR", None),
    },
}

# Демонстрационные курсы, не актуальные котировки
USD_TO_KZT = 540.0
EUR_TO_KZT = 590.0

CURRENCY_RATES = {
    "USD → KZT": USD_TO_KZT,
    "KZT → USD": 1 / USD_TO_KZT,
    "EUR → KZT": EUR_TO_KZT,
    "KZT → EUR": 1 / EUR_TO_KZT,
}


def convert_value(value, category, conversion_name):
    source, target, factor = CONVERSIONS[category][conversion_name]

    if category == "Температура":
        if conversion_name == "°C → °F":
            result = value * 9 / 5 + 32
        elif conversion_name == "°F → °C":
            result = (value - 32) * 5 / 9
        elif conversion_name == "°C → K":
            result = value + 273.15
        else:
            result = value - 273.15

    elif category == "Валюта":
        result = value * CURRENCY_RATES[conversion_name]

    else:
        result = value * factor

    return result, source, target


def swap_conversion(category, conversion_name):
    conversions = CONVERSIONS[category]

    if conversion_name not in conversions:
        return conversion_name

    source, target, factor = conversions[conversion_name]

    for name, data in conversions.items():
        if data[0] == target and data[1] == source:
            return name

    return conversion_name


def add_history(history, text, limit=N):
    history.insert(0, text)
    del history[limit:]