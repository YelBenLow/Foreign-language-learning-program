import os
import customtkinter as ctk
from elements import *


class Szotanulo(ctk.CTk):
    def __init__(self):
        super().__init__()

        # appearance mode
        ctk.set_appearance_mode('dark')

        # window settings
        self.title('Szótanulás - Formáld a Világod!')
        self.geometry('1200x600')
        self.minsize(1200, 600)
        self.maxsize(1200, 600)
        self.iconbitmap(os.getcwd()+'\\_imgs\\_icon\\icon.ico')

        # layout
        self.rowconfigure(0, weight = 1, uniform = 'mainapp')
        self.columnconfigure(0, weight = 2, uniform = 'mainapp')
        self.columnconfigure(1, weight = 1, uniform = 'mainapp')

        # data
        self.valaszVar = ctk.StringVar()
        self.specValaszVar = ctk.StringVar()
        self.eredmeny = ctk.StringVar()
        self.tap = 0

        with open('adatok.adatok', 'r', encoding = 'utf-8', buffering = 1) as f:
            self.tap = f.readline().strip()
            self.tap = int(self.tap) if self.tap else 0

        # widgets
        szavasOldal = SzavasOldal(self, self.valaszVar, self.specValaszVar, self.eredmeny, self)
        cicusOldal = CicusOldal(self, self.valaszVar, self.specValaszVar, self.eredmeny, self.tap, self)

        # grid
        szavasOldal.grid(row = 0, column = 0, sticky = 'nsew')
        cicusOldal.grid(row = 0, column = 1, sticky = 'nsew')


if __name__ == '__main__':
    app = Szotanulo()
    app.mainloop()
