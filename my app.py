
import tkinter as tk
from tkinter import ttk

CONVERSIONS = {
    "Километры → мили": lambda value: value * 0.621371,
    "Килограммы → фунты": lambda value: value * 2.20462,
    "°C → °F": lambda value: value * 9 / 5 + 32,
}


def convert(value_entry, conversion_box, result_label):
    try:
        value = float(value_entry.get().replace(",", "."))
    except ValueError:
        result_label.config(
            text="Введите число, например 12.5"
        )
        return

    conversion_name = conversion_box.get()
    converted = CONVERSIONS[conversion_name](value)

    result_label.config(text=f"Результат: {converted:.2f}")


def main():
    root = tk.Tk()
    root.title("Моё приложение")
    root.geometry("360x180")

    value_entry = ttk.Entry(root)
    value_entry.pack(pady=6)

    conversion_box = ttk.Combobox(
        root,
        values=[
            "Километры → мили",
            "Килограммы → фунты",
            "°C → °F"
        ],
        state="readonly"
    )
    conversion_box.current(0)
    conversion_box.pack(pady=6)

    result_label = ttk.Label(
        root,
        text="Результат появится здесь"
    )
    result_label.pack(pady=6)

    convert_button = tk.Button(
        root,
        text="Конвертировать",
        command=lambda: convert(
            value_entry,
            conversion_box,
            result_label
        )
    )
    convert_button.pack(pady=8)

    root.mainloop()


if __name__ == "__main__":
    main()