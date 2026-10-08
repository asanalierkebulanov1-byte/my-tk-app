import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Моё приложение")
    root.geometry("360x180")

    greeting = tk.Label(root, text="Привет, мир!", font=("TkDefaultFont", 18))
    greeting.pack(expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()