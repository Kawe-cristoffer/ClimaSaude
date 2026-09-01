import tkinter as tk

from interface import ClimaSaudeApp


def main():

    janela = tk.Tk()

    ClimaSaudeApp(janela)

    janela.mainloop()


if __name__ == "__main__":
    main()