import os
import random
import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont
from settings import *


class funckiotAtado():
    def __init__(self, func):
        self.funkcio = func

    def funkc_update(self, func):
        self.funkcio = func

    def funkc_get(self):
        return self.funkcio

class SzavasOldal(ctk.CTkFrame):
    def __init__(self, parent, valaszVar, specValaszvar, eredmenyVar, mainreferencia):
        super().__init__(master = parent)

        # layout
        self.rowconfigure(0, weight = 1, uniform='szavasoldal')
        self.rowconfigure(1, weight = 6, uniform='szavasoldal')

        self.columnconfigure(0, weight = 1, uniform='szavasoldal')
        self.columnconfigure(1, weight = 3, uniform='szavasoldal')
        self.columnconfigure(2, weight = 3, uniform='szavasoldal')

        # data
        self.nyelvekLista = ['magyar', 'english', 'espanol']
        self.nyelv1Var = ctk.StringVar(value = 'magyar')
        self.nyelv2Var = ctk.StringVar(value = 'english')
        self.specVar = ctk.IntVar(value = 0)


        self.magyarkep = ctk.CTkImage(Image.open(os.getcwd()+'\\_imgs\\_zaszlo\\magyar.png'))
        self.angolkep = ctk.CTkImage(Image.open(os.getcwd()+'\\_imgs\\_zaszlo\\angol.png'))
        self.spanyolkep = ctk.CTkImage(Image.open(os.getcwd()+'\\_imgs\\_zaszlo\\spanyol.png'))

        # fonts
        macskacimFont = ctk.CTkFont(family = MAIN_FAMILY,
                                    size = MACSKACIM_SIZE)

        averageBtnFont = ctk.CTkFont(family = MAIN_FAMILY,
                                     size = AVERAGE_BUTTON_TSIZE)

        nyilFont = ctk.CTkFont(family = MAIN_FAMILY,
                               size = NYIL_SIZE)

        # widgets
        self.specialButton = ctk.CTkButton(self,
                                           text = 'Speciális',
                                           fg_color = AVERAGE_BUTTON_BG_COLOR,
                                           hover_color = AVERAGE_BUTTON_HOVER_COLOR,
                                           text_color = AVERAGE_BUTTON_TCOLOR,
                                           font = averageBtnFont,
                                           command = lambda: self.nyelvValtoztat(spec=self.specVar))

        self.cimLabel = ctk.CTkLabel(self, text = f'Macsek neve: Palánta', font = macskacimFont)

        # nyelvekFrame
        self.nyelvFrame = ctk.CTkFrame(self, fg_color = ('#dbdbdb', '#2b2b2b'))
        self.nyelvFrame.columnconfigure((0,1,2), weight = 1)
        self.nyelvFrame.rowconfigure(0, weight = 1)

        self.nyelv1 = ctk.CTkButton(self.nyelvFrame,
                                    textvariable = self.nyelv1Var,
                                    image = self.magyarkep,
                                    fg_color=AVERAGE_BUTTON_BG_COLOR,
                                    hover_color=AVERAGE_BUTTON_HOVER_COLOR,
                                    text_color=AVERAGE_BUTTON_TCOLOR,
                                    font=averageBtnFont,
                                    command = lambda: self.nyelvValtoztat(var = self.nyelv1Var,
                                                                          melyik = 1))

        self.toLabel = ctk.CTkLabel(self.nyelvFrame, text = '→', font = nyilFont)

        self.nyelv2 = ctk.CTkButton(self.nyelvFrame,
                                    textvariable = self.nyelv2Var,
                                    image = self.angolkep,
                                    fg_color=AVERAGE_BUTTON_BG_COLOR,
                                    hover_color=AVERAGE_BUTTON_HOVER_COLOR,
                                    text_color=AVERAGE_BUTTON_TCOLOR,
                                    font=averageBtnFont,
                                    command = lambda: self.nyelvValtoztat(var = self.nyelv2Var,
                                                                          melyik = 2))

        self.belsoSzoszekcio = belsoSzoszekcio(parent = self,
                                               nyelv1var = self.nyelv1Var,
                                               nyelv2var = self.nyelv2Var,
                                               spec = self.specVar,
                                               valaszVar = valaszVar,
                                               specValaszvar = specValaszvar,
                                               eredmenyVar = eredmenyVar,
                                               mainReferencia = mainreferencia)

        # nyelvgrid
        self.nyelv1.grid(row=0, column = 0)
        self.toLabel.grid(row=0, column = 1)
        self.nyelv2.grid(row=0, column = 2)


        # grid
        self.specialButton.grid(row = 0, column = 0, padx = 10)
        self.cimLabel.grid(row = 0, column = 1)
        self.nyelvFrame.grid(row = 0, column = 2, sticky = 'nsew')
        self.belsoSzoszekcio.grid(row = 1, column = 0, columnspan = 3, sticky = 'nsew', padx = 15, pady = 15)

    def nyelvValtoztat(self, var=None, spec=None, melyik=None):
        if not spec:
            self.specVar.set(0)
            index = self.nyelvekLista.index(var.get())+1
            newIndex = 0

            if index == 3:
                index = 0

            var.set(self.nyelvekLista[index])

            if self.nyelv1Var.get() == self.nyelv2Var.get():
                newIndex = self.nyelvekLista.index(var.get())+1
                if newIndex == 3:
                    newIndex = 0

                var.set(self.nyelvekLista[newIndex])

                if melyik == 1:
                    if self.nyelvekLista[newIndex] == 'magyar':
                        self.nyelv1.configure(image = self.magyarkep)

                    elif self.nyelvekLista[newIndex] == 'english':
                        self.nyelv1.configure(image = self.angolkep)

                    elif self.nyelvekLista[newIndex] == 'espanol':
                        self.nyelv1.configure(image = self.spanyolkep)

                elif melyik == 2:
                    if self.nyelvekLista[newIndex] == 'magyar':
                        self.nyelv2.configure(image=self.magyarkep)

                    elif self.nyelvekLista[newIndex] == 'english':
                        self.nyelv2.configure(image=self.angolkep)

                    elif self.nyelvekLista[newIndex] == 'espanol':
                        self.nyelv2.configure(image=self.spanyolkep)
            else:
                if melyik == 1:
                    if self.nyelvekLista[index] == 'magyar':
                        self.nyelv1.configure(image=self.magyarkep)

                    elif self.nyelvekLista[index] == 'english':
                        self.nyelv1.configure(image=self.angolkep)

                    elif self.nyelvekLista[index] == 'espanol':
                        self.nyelv1.configure(image=self.spanyolkep)

                elif melyik == 2:
                    if self.nyelvekLista[index] == 'magyar':
                        self.nyelv2.configure(image=self.magyarkep)

                    elif self.nyelvekLista[index] == 'english':
                        self.nyelv2.configure(image=self.angolkep)

                    elif self.nyelvekLista[index] == 'espanol':
                        self.nyelv2.configure(image=self.spanyolkep)



        else:
            if spec.get() in [0, 1]:
                spec.set(spec.get()+1)
            else:
                spec.set(1)


ujFeladatfunkcio = funckiotAtado(func = None)

class belsoSzoszekcio(ctk.CTkFrame):
    def __init__(self, parent, nyelv1var, nyelv2var, spec, valaszVar, specValaszvar, eredmenyVar, mainReferencia):
        super().__init__(master = parent)

        # layout
        self.columnconfigure((0,1,2), weight = 1, uniform = 'belsoSzoszekcio')

        self.rowconfigure(0, weight = 1, uniform = 'belsoSzoszekcio')
        self.rowconfigure(1, weight = 3, uniform = 'belsoSzoszekcio')

        # data
        self.nyelv1var = nyelv1var
        self.nyelv2var = nyelv2var
        self.specVar = spec

        self.szoVar = ctk.StringVar()
        self.valaszVar = valaszVar
        self.specValaszVar = specValaszvar

        self.eredmenyVar = eredmenyVar

        self.prevnyelv1, self.prevnyelv2 = self.nyelv1var.get(), self.nyelv2var.get()

        self.szoDict = {}
        self.specSzoDict_List = {}


        # trace
        self.nyelv1var.trace('w', self.update_datas)
        self.nyelv2var.trace('w', self.update_datas)
        self.specVar.trace('w', self.update_datas)

        self.szotarbaRendez(self.nyelv1var.get(), self.nyelv2var.get())
        self.szotarJatek()

        # config, hogy enterrel is lehessen csekkolni
        mainReferencia.bind('<Return>', self.checkJoSzo)

        # fonts
        nyelvKivalasztvaFont = ctk.CTkFont(family = MAIN_FAMILY,
                                           size = NYELVKIVALASZTVA_SIZE)

        randomSzoFont = ctk.CTkFont(family = MAIN_FAMILY,
                                    size = RANDOMSZO_SZIE)

        valaszEntryFont = ctk.CTkFont(family = MAIN_FAMILY,
                                      size = VALASZ_ENTRY_SIZE)

        tudatositoFont = ctk.CTkFont(family = MAIN_FAMILY,
                                     size = TUDATOSITO_SIZE)

        submitButtonFont = ctk.CTkFont(family = MAIN_FAMILY,
                                       size = AVERAGE_BUTTON_TSIZE)

        # widgets
        self.cimLabel = ctk.CTkLabel(self,
                                     text = f'{self.nyelv1var.get()} → {self.nyelv2var.get()}',
                                     font = nyelvKivalasztvaFont)

        self.szoFrame = ctk.CTkFrame(self)
        self.szoFrame.rowconfigure((0,1,2), weight = 1, uniform = 'SzoFramee')
        self.szoFrame.columnconfigure((0,1), weight = 1, uniform = 'SzoFramee')

        self.szoLabel = ctk.CTkLabel(self.szoFrame, textvariable = self.szoVar, font = randomSzoFont)

        self.specTudatositoBaloldal = ctk.CTkLabel(self.szoFrame, text = '', font = tudatositoFont)
        self.specTudatositoJobboldal = ctk.CTkLabel(self.szoFrame, text = '', font = tudatositoFont)

        self.szoEntry = ctk.CTkEntry(self.szoFrame,
                                     textvariable = self.valaszVar,
                                     width = VALASZ_ENTRY_WIDTH,
                                     font = valaszEntryFont)

        self.specSzoEntry = ctk.CTkEntry(self.szoFrame,
                                         textvariable = self.specValaszVar,
                                         width=VALASZ_ENTRY_WIDTH,
                                         font=valaszEntryFont)

        self.szoSubmitButton = ctk.CTkButton(self.szoFrame,
                                             text = 'Ellenőríz',
                                             fg_color = AVERAGE_BUTTON_BG_COLOR,
                                             hover_color = AVERAGE_BUTTON_HOVER_COLOR,
                                             text_color = AVERAGE_BUTTON_TCOLOR,
                                             font = submitButtonFont,
                                             command = self.checkJoSzo)

        # szoGrid
        self.szoLabel.grid(row = 0, column = 0, columnspan = 3)
        self.szoEntry.grid(row = 1, column = 0, columnspan = 2)
        self.szoSubmitButton.grid(row = 2, column = 0, columnspan = 2)

        # grid
        self.cimLabel.grid(row = 0, column = 0, columnspan = 3)
        self.szoFrame.grid(row = 1, column = 0, columnspan = 3, sticky = 'nsew', padx = 10, pady = 10)

        ujFeladatfunkcio.funkc_update(self.szotarJatek)


    def update_datas(self, *args):
        self.valaszVar.set('')
        self.specValaszVar.set('')

        if not self.specVar.get(): # ha nem a speciális gombra kattintottunk
            self.cimLabel.configure(text = f'{self.nyelv1var.get()} → {self.nyelv2var.get()}')

            if (self.nyelv1var.get() != self.prevnyelv1 or self.nyelv2var.get() != self.prevnyelv2) and self.nyelv1var.get() != self.nyelv2var.get():
                self.szotarbaRendez(self.nyelv1var.get(), self.nyelv2var.get())

                self.prevnyelv1, self.prevnyelv2 = self.nyelv1var.get(), self.nyelv2var.get()

            self.specSzoEntry.grid_forget()
            self.specTudatositoBaloldal.grid_forget()
            self.specTudatositoJobboldal.grid_forget()
            self.szoEntry.grid_forget()
            self.szoSubmitButton.grid_forget()

            self.szoFrame.rowconfigure((0,1,2), weight=1, uniform='SzoFramee')

            self.szoEntry.grid(row = 1, column = 0, columnspan = 2)
            self.szoSubmitButton.grid(row = 2, column = 0, columnspan = 2)

        else:
            if self.specVar.get() == 1:  # első speciális mód
                self.cimLabel.configure(text = f'espanol → english → magyar')
                self.szotarbaRendez('', '', spec=1)

                self.specTudatositoBaloldal.configure(text = 'english')
                self.specTudatositoJobboldal.configure(text = 'magyar')

            else:  # második speciális mód
                self.cimLabel.configure(text=f'magyar → english → espanol')
                self.szotarbaRendez('', '', spec=2)

                self.specTudatositoBaloldal.configure(text='english')
                self.specTudatositoJobboldal.configure(text='espanol')

            self.szoFrame.rowconfigure((0,1,2,3), weight=1, uniform='SzoFramee')

            self.szoEntry.grid_forget()
            self.szoSubmitButton.grid_forget()

            self.specTudatositoBaloldal.grid(row = 1, column = 0)
            self.specTudatositoJobboldal.grid(row = 1, column = 1)

            self.szoEntry.grid(row=2, column=0, sticky = 'e', padx = 10)
            self.specSzoEntry.grid(row = 2, column = 1, sticky = 'w', padx = 10)

            self.szoSubmitButton.grid(row = 3, column = 0, columnspan = 2)



    def szotarbaRendez(self, nyelv1, nyelv2, spec=None):
        self.szoDict = {}
        self.specSzoDict_List = {}

        if spec == None:
            with open(f'szotar\\{nyelv1}-{nyelv2}.txt', 'r', encoding = 'utf-8') as f:
                for szopar in f:
                    szo, forditas = szopar.split('-')
                    self.szoDict[szo] = forditas.strip()

        else:
            if spec == 1:
                with open(f'szotar\\espanol-english-magyar.txt', 'r', encoding = 'utf-8') as f:
                    for szopar in f:
                        szplittelve = szopar.split('-')
                        self.specSzoDict_List[szplittelve[0]] = szplittelve[1:]
            else:
                with open(f'szotar\\magyar-english-espanol.txt', 'r', encoding = 'utf-8') as f:
                    for szopar in f:
                        szplittelve = szopar.split('-')
                        self.specSzoDict_List[szplittelve[0]] = szplittelve[1:]

        self.szotarJatek()

    def szotarJatek(self):
        if self.szoDict:
            random_szo = random.choice(list(self.szoDict.keys()))
            self.szoVar.set(random_szo)

        elif self.specSzoDict_List:
            random_szo = random.choice(list(self.specSzoDict_List.keys()))
            self.szoVar.set(random_szo)

    def checkJoSzo(self, *args):
        if self.szoDict:
            if self.szoDict[self.szoVar.get()] == self.valaszVar.get():
                self.eredmenyVar.set('1 jó')
            else:
                self.eredmenyVar.set(f'1 rossz {self.szoDict[self.szoVar.get()]}')

            self.valaszVar.set('')

        elif self.specSzoDict_List:
            jelentesek = self.specSzoDict_List[self.szoVar.get()]

            if self.valaszVar.get() == jelentesek[0] and self.specValaszVar.get() == jelentesek[1].strip():
                self.eredmenyVar.set('2 jó')
            else:
                self.eredmenyVar.set(f'2 rossz {jelentesek[0]}|{jelentesek[1]}')

            self.valaszVar.set('')
            self.specValaszVar.set('')


class CicusOldal(ctk.CTkFrame):
    def __init__(self, parent, valaszVar, specValaszVar, eredmenyVar, pont, mainReferencia):
        super().__init__(master = parent)

        # layout
        self.columnconfigure(0, weight = 1, uniform = 'mainCicus')

        self.rowconfigure(0, weight = 1, uniform = 'mainCicus')
        self.rowconfigure(1, weight = 2, uniform = 'mainCicus')

        # data
        self.valaszVar = valaszVar
        self.specValaszVar = specValaszVar
        self.eredmenyVar = eredmenyVar

        self.pont = pont

        self.animateFrame = 0
        self.animating = False
        self.animateSpeed = 500
        self.last_clicked_btnSpeed = None
        self.rosszAnimaciosKep = False

        self.imgAnimationList = ['alap.png', 'szerkesztett.png']

        self.cicaText = ''
        self.image = Image.open('_imgs\\_cica\\dark\\alap.png')
        self.image_tk = ImageTk.PhotoImage(self.image)


        # trace
        self.eredmenyVar.trace('w', self.update_cicus)

        # fonts
        animacioCimFont = ctk.CTkFont(family = MAIN_FAMILY,
                                      size = ANIMACIO_CIM_SIZE)

        animacioBtnFont = ctk.CTkFont(family = MAIN_FAMILY,
                                      size = AVERAGE_BUTTON_TSIZE)

        tapKiiroFont = ctk.CTkFont(family = MAIN_FAMILY,
                                   size = TAP_KIIRO_CIM_SIZE)

        # widgets
        self.felsoReszFrame = ctk.CTkFrame(self)
        self.felsoReszFrame.rowconfigure(0, weight = 1, uniform = 'felsoReszFrame')
        self.felsoReszFrame.rowconfigure(1, weight = 1, uniform = 'felsoReszFrame')
        self.felsoReszFrame.rowconfigure(2, weight = 3, uniform = 'felsoReszFrame')

        self.felsoReszFrame.columnconfigure((0,1,2,3), weight = 1)

        self.tajekoztato = ctk.CTkLabel(self.felsoReszFrame, text = 'Animáció sebessége', font = animacioCimFont)


        self.nagyonlassuBtn = ctk.CTkButton(self.felsoReszFrame,
                                            text = 'Nagyon lassú',
                                            fg_color=AVERAGE_ANIMACIO_BUTTON_BG_COLOR,
                                            hover_color=AVERAGE_BUTTON_HOVER_COLOR,
                                            text_color=AVERAGE_BUTTON_TCOLOR,
                                            text_color_disabled=AVERAGE_DISABLED_TCOLOR,
                                            font = animacioBtnFont,
                                            width = 205,
                                            command = lambda: self.change_animation_speen('nagyonlassu'))

        self.lassuBtn = ctk.CTkButton(self.felsoReszFrame,
                                      text = 'Lassú',
                                      fg_color=AVERAGE_ANIMACIO_BUTTON_BG_COLOR,
                                      hover_color=AVERAGE_BUTTON_HOVER_COLOR,
                                      text_color=AVERAGE_BUTTON_TCOLOR,
                                      text_color_disabled=AVERAGE_DISABLED_TCOLOR,
                                      font=animacioBtnFont,
                                      command = lambda: self.change_animation_speen('lassu'))

        self.kozepesBtn = ctk.CTkButton(self.felsoReszFrame,
                                        text = 'Közepes',
                                        fg_color=AVERAGE_ANIMACIO_BUTTON_BG_COLOR,
                                        hover_color=AVERAGE_BUTTON_HOVER_COLOR,
                                        text_color=AVERAGE_BUTTON_TCOLOR,
                                        text_color_disabled=AVERAGE_DISABLED_TCOLOR,
                                        font=animacioBtnFont,
                                        command = lambda: self.change_animation_speen('kozep'))

        self.gyorsBtn = ctk.CTkButton(self.felsoReszFrame,
                                      text = 'Gyors',
                                      fg_color=AVERAGE_ANIMACIO_BUTTON_BG_COLOR,
                                      hover_color=AVERAGE_BUTTON_HOVER_COLOR,
                                      text_color=AVERAGE_BUTTON_TCOLOR,
                                      text_color_disabled=AVERAGE_DISABLED_TCOLOR,
                                      font=animacioBtnFont,
                                      command = lambda: self.change_animation_speen('gyors'))

        self.tapod = ctk.CTkLabel(self.felsoReszFrame, text = f'Táp: {self.pont}', font = tapKiiroFont)

        self.changeThemeBtn = ctk.CTkButton(self.felsoReszFrame,
                                            text = 'Mód: Sötét',
                                            fg_color=AVERAGE_ANIMACIO_BUTTON_BG_COLOR,
                                            hover_color=AVERAGE_BUTTON_HOVER_COLOR,
                                            text_color=AVERAGE_BUTTON_TCOLOR,
                                            font=animacioBtnFont,
                                            width = 200,
                                            command = self.changeMode)

        self.cicusCanvas = tk.Canvas(self, background = '#333', bd = 0, highlightthickness = 0, relief = 'ridge')
        self.cicusCanvas.create_image(self.image_tk.width()/2,
                                      self.image_tk.height()/2,
                                      image=self.image_tk)

        # felso grid
        self.tajekoztato.grid(row = 0, column = 0, columnspan = 4)
        self.nagyonlassuBtn.grid(row = 1, column = 0)
        self.lassuBtn.grid(row = 1, column = 1, padx = 5)
        self.kozepesBtn.grid(row = 1, column = 2, padx = 5)
        self.gyorsBtn.grid(row = 1, column = 3, padx = 5)
        self.tapod.grid(row = 2, column = 0, columnspan = 2)
        self.changeThemeBtn.grid(row = 2, column = 2)

        # grid
        self.felsoReszFrame.grid(row = 0, column = 0, sticky = 'nsew')
        self.cicusCanvas.grid(row = 1, column = 0, sticky = 'nsew')


        # ablak lezaraskor mentes
        self.mainref = mainReferencia
        self.mainref.protocol("WM_DELETE_WINDOW", self.close_window)

    def close_window(self):
        with open('adatok.adatok', 'w', encoding = 'utf-8', buffering = 1) as f:
            f.write(str(self.pont))

        self.mainref.destroy()

    def changeMode(self):
        if 'Világos' in self.changeThemeBtn.cget('text'):
            self.changeThemeBtn.configure(text = 'Mód: Sötét')
            ctk.set_appearance_mode('Dark')

            self.cicusCanvas.configure(background = '#333')

            self.cicusCanvas.delete('all')

            if not self.rosszAnimaciosKep:
                self.image = Image.open('_imgs\\_cica\\dark\\alap.png')
            else:
                self.image = Image.open('_imgs\\_cica\\dark\\rosszKinyitSzerkesztett.png')
            self.image_tk = ImageTk.PhotoImage(self.image)

            self.cicusCanvas.create_image(self.image_tk.width() / 2,
                                          self.image_tk.height() / 2,
                                          image=self.image_tk)


        else:
            self.changeThemeBtn.configure(text='Mód: Világos')
            ctk.set_appearance_mode('Light')

            self.cicusCanvas.configure(background = CICUSCANVAS_BGCOLOR)

            self.cicusCanvas.delete('all')

            if not self.rosszAnimaciosKep:
                self.image = Image.open('_imgs\\_cica\\light\\alap.png')
            else:
                self.image = Image.open('_imgs\\_cica\\light\\rosszKinyitSzerkesztett.png')

            self.image_tk = ImageTk.PhotoImage(self.image)

            self.cicusCanvas.create_image(self.image_tk.width() / 2,
                                          self.image_tk.height() / 2,
                                          image=self.image_tk)


    def update_cicus(self, *args):
        if not self.animating:
            self.cicusCanvas.delete('all')

            self.imgAnimationList = ['alap.png', 'szerkesztett.png']

            if 'Világos' in self.changeThemeBtn.cget('text'):
                self.image = Image.open('_imgs\\_cica\\light\\kinyit.png')
            else:
                self.image = Image.open('_imgs\\_cica\\dark\\kinyit.png')

            self.cicaText = self.valaszVar.get() if '1' in self.eredmenyVar.get() else f'{self.valaszVar.get()} | {self.specValaszVar.get()}'
            cicaszaj = ImageDraw.Draw(self.image)
            font = ImageFont.truetype('font\\OpenSans-Regular.ttf', 24)
            cicaszaj.text((65, 250), self.cicaText, fill='#000', font=font)

            if 'Világos' in self.changeThemeBtn.cget('text'):
                self.image.save('_imgs\\_cica\\light\\szerkesztett.png')
            else:
                self.image.save('_imgs\\_cica\\dark\\szerkesztett.png')

            if 'jó' in self.eredmenyVar.get():
                self.imgAnimationList.append('jo.png')
                self.pont += 1
                self.imgAnimationList.append('alap.png')

                self.rosszAnimaciosKep = False

            elif 'rossz' in self.eredmenyVar.get():
                self.imgAnimationList.append('rossz.png')
                self.pont -= 1

                for mode in ['light', 'dark']:
                    self.image = Image.open(f'_imgs\\_cica\\{mode}\\rosszKinyit.png')

                    if len(self.eredmenyVar.get().split()) == 3:
                        self.cicaText = self.eredmenyVar.get().split()[-1]
                    else:
                        self.cicaText = ' '.join(self.eredmenyVar.get().split()[-2:])

                    cicaszaj = ImageDraw.Draw(self.image)
                    font = ImageFont.truetype('font\\OpenSans-Regular.ttf', 24)
                    cicaszaj.text((65, 250), self.cicaText, fill='#FF0000', font=font)

                    self.image.save(f'_imgs\\_cica\\{mode}\\rosszKinyitSzerkesztett.png')

                self.imgAnimationList.append('rosszKinyitSzerkesztett.png')

                self.rosszAnimaciosKep = True

            self.animate()


    def animate(self):
        self.animating = True
        if self.animateFrame < len(self.imgAnimationList):
            if 'Világos' in self.changeThemeBtn.cget('text'):
                self.image = Image.open(f'_imgs\\_cica\\light\\{self.imgAnimationList[self.animateFrame]}')
            else:
                self.image = Image.open(f'_imgs\\_cica\\dark\\{self.imgAnimationList[self.animateFrame]}')

            self.image_tk = ImageTk.PhotoImage(self.image)

            self.cicusCanvas.create_image(self.image_tk.width() / 2,
                                          self.image_tk.height() / 2,
                                          image=self.image_tk)

            self.animateFrame += 1

            if self.animateFrame != len(self.imgAnimationList)-1:
                self.cicusCanvas.after(self.animateSpeed, self.animate)
            else:
                self.cicusCanvas.after(self.animateSpeed+200, self.animate)


        else:
            self.animateFrame = 0
            self.animating = False
            self.tapod.configure(text=f'Táp: {self.pont}')
            ujFeladatfunkcio.funkc_get()()

    def change_animation_speen(self, speed):
        if speed == 'nagyonlassu':
            self.animateSpeed = 2500

            self.nagyonlassuBtn.configure(state = 'disabled')

            if self.last_clicked_btnSpeed:
                self.last_clicked_btnSpeed.configure(state = 'normal')

            self.last_clicked_btnSpeed = self.nagyonlassuBtn

        elif speed == 'lassu':
            self.animateSpeed = 1500

            self.lassuBtn.configure(state = 'disabled')

            if self.last_clicked_btnSpeed:
                self.last_clicked_btnSpeed.configure(state='normal')

            self.last_clicked_btnSpeed = self.lassuBtn

        elif speed == 'kozep':
            self.animateSpeed = 500

            self.kozepesBtn.configure(state = 'disabled')

            if self.last_clicked_btnSpeed:
                self.last_clicked_btnSpeed.configure(state='normal')

            self.last_clicked_btnSpeed = self.kozepesBtn

        elif speed == 'gyors':
            self.animateSpeed = 200

            self.gyorsBtn.configure(state = 'disabled')

            if self.last_clicked_btnSpeed:
                self.last_clicked_btnSpeed.configure(state='normal')

            self.last_clicked_btnSpeed = self.gyorsBtn
