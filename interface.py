from logic import CONVERSIONS

# Теперь функцию можно вызывать напрямую:


import tkinter as tk
from tkinter import ttk, messagebox
import math

from logic import (
    N,
    CONVERSIONS,
    convert_value,
    swap_conversion,
    add_history,
)


def main():
    root = tk.Tk()
    root.title("Универсальный конвертер")
    root.geometry("500x540")
    root.resizable(False, False)

    history = []

    category_var = tk.StringVar(value="Длина")
    conversion_var = tk.StringVar()
    value_var = tk.StringVar()

    ttk.Label(
        root,
        text="Универсальный конвертер",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    ttk.Label(root, text="Категория:").pack()

    category_box = ttk.Combobox(
        root,
        textvariable=category_var,
        values=list(CONVERSIONS.keys()),
        state="readonly",
        width=30
    )
    category_box.pack(pady=5)

    ttk.Label(root, text="Преобразование:").pack()

    conversion_box = ttk.Combobox(
        root,
        textvariable=conversion_var,
        state="readonly",
        width=30
    )
    conversion_box.pack(pady=5)

    ttk.Label(root, text="Введите значение:").pack()

    value_entry = ttk.Entry(
        root,
        textvariable=value_var,
        width=33
    )
    value_entry.pack(pady=5)

    result_label = ttk.Label(
        root,
        text="Результат появится здесь",
        font=("Arial", 11, "bold"),
        wraplength=450
    )
    result_label.pack(pady=10)

    def update_conversions(event=None):
        names = list(CONVERSIONS[category_var.get()].keys())
        conversion_box["values"] = names
        conversion_var.set(names[0])
        result_label.config(text="Результат появится здесь")

    def convert():
        try:
            raw_value = value_var.get().strip().replace(",", ".")

            if not raw_value:
                raise ValueError("Введите число.")

            value = float(raw_value)

            if not math.isfinite(value):
                raise ValueError("Введите конечное число.")

            category = category_var.get()
            conversion_name = conversion_var.get()

            result, source, target = convert_value(
                value, category, conversion_name
            )

            text = f"{value:g} {source} = {result:.2f} {target}"
            result_label.config(text=text)

            add_history(history, text)

            history_list.delete(0, tk.END)
            for item in history:
                history_list.insert(tk.END, item)

        except ValueError as error:
            result_label.config(text="Не удалось выполнить конвертацию")
            messagebox.showerror("Ошибка", str(error))

    def swap_units():
        category = category_var.get()
        current = conversion_var.get()

        conversion_var.set(swap_conversion(category, current))
        result_label.config(
            text="Единицы изменены. Выполните конвертацию."
        )

    category_box.bind(
        "<<ComboboxSelected>>",
        update_conversions
    )

    conversion_box.bind(
        "<<ComboboxSelected>>",
        lambda event: result_label.config(
            text="Нажмите «Конвертировать»"
        )
    )

    ttk.Button(
        root,
        text="Конвертировать",
        command=convert
    ).pack(pady=4)

    ttk.Button(
        root,
        text="Поменять единицы местами",
        command=swap_units
    ).pack(pady=4)

    ttk.Label(
        root,
        text=f"История конвертаций (последние {N}):"
    ).pack(pady=5)

    history_list = tk.Listbox(
        root,
        width=58,
        height=5
    )
    history_list.pack(pady=5)

    update_conversions()
    root.mainloop()


if __name__ == "__main__":
    main()