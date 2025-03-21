#!/usr/bin/python3

from tkinter import *
import requests
import json
from datetime import datetime


def TS2Data(Value):
    if Value != None :
        date_time = datetime.fromtimestamp(int(Value))
        Value = date_time.strftime("%d/%m/%Y %H:%M:%S")
    else:
        Value = "Mai"
    return Value

def ReadFile():
    Sito.set("{url}/player_api.php?username={usr}&password={pwd}".format(url=url.get(), usr=usr.get(), pwd=pwd.get()))
    SitoPV.set("{url}/panel_api.php?username={usr}&password={pwd}".format(url=url.get(), usr=usr.get(), pwd=pwd.get()))
    SitoGV.set("{url}/get.php?username={usr}&password={pwd}&type=m3u_plus&output=ts".format(url=url.get(), usr=usr.get(), pwd=pwd.get()))
    User_InfoTxt = requests.Session().get(Sito.get()).text
    TxtMsg.delete("1.0", END)
    TxtMsg.insert(END,User_InfoTxt)
    User_Info = json.loads(User_InfoTxt)
    creatoIl = TS2Data(User_Info['user_info']["created_at"])
    Creato.config(text = creatoIl)
    scadeIl = TS2Data(User_Info['user_info']["exp_date"])
    Scade.config(text = scadeIl)

    try:
        return 1
    except:
        return 0


WinMain = Tk()
WinMain.title("M3u test")
WinMain.geometry('900x600')

Width  = 900
LabelW = 20
InputW = 45
PadX   = 5
PadY   = 5

furl = Frame(WinMain)
furl.pack(side=TOP, fill=X, padx=PadX, pady=PadY)
lurl = Label(furl, width=LabelW, text="Sito", anchor="w", borderwidth=2, relief="sunken").pack(side=LEFT)
url  = Entry(furl, width=InputW)
url.pack(side=RIGHT, expand=YES, fill=X)
url.insert(1,"http://login.lionboxtv.xyz:80")
fusr = Frame(WinMain)
fusr.pack(side=TOP, fill=X, padx=PadX, pady=PadY)
lusr = Label(fusr, width=LabelW, text="User", anchor="w", borderwidth=2, relief="sunken")
lusr.pack(side=LEFT)
usr  = Entry(fusr, width=InputW)
usr.pack(side=RIGHT, expand=YES, fill=X)
usr.insert(1,"12unioniptv12")
fpwd = Frame(WinMain)
fpwd.pack(side=TOP, fill=X, padx=PadX, pady=PadY)
lpwd = Label(fpwd, width=LabelW, text="Password", anchor="w", borderwidth=2, relief="sunken")
lpwd.pack(side=LEFT)
pwd  = Entry(fpwd, width=InputW)
pwd.pack(side=RIGHT, expand=YES, fill=X)
pwd.insert(1,"RhXNL2W8vU54")

fButton = Frame(WinMain)
fButton.pack(side=TOP, fill=X, padx=PadX, pady=PadY)
Button(fButton, width=15, text='Esegui', command=ReadFile).pack(side=LEFT, pady=30)

fSito = Frame(WinMain)
fSito.pack(side=TOP, fill=X, padx=PadX, pady=PadY)
Sito = StringVar()
SitoV = Entry(fSito, textvariable=Sito, width=Width)
SitoV.pack(side=LEFT)
fSitoP = Frame(WinMain)
fSitoP.pack(side=TOP, fill=X, padx=PadX, pady=PadY)
SitoPV = StringVar()
SitoP = Entry(fSitoP, textvariable=SitoPV, width=Width)
SitoP.pack(side=LEFT)
fSitoG = Frame(WinMain)
fSitoG.pack(side=TOP, fill=X, padx=PadX, pady=PadY)
SitoGV = StringVar()
SitoG = Entry(fSitoG, textvariable=SitoGV, width=Width)
SitoG.pack(side=LEFT)
fCreato = Frame(WinMain)
fCreato.pack(side=TOP, fill=X, padx=PadX, pady=PadY)
lCreato = Label(fCreato, width=LabelW, text="Creato", anchor="w", borderwidth=2, relief="sunken")
lCreato.pack(side=LEFT)
Creato  = Label(fCreato, width=LabelW, text="creato", anchor="w", borderwidth=2, relief="raised")
Creato.pack(side=LEFT, fill=X, padx=PadX, pady=PadY)
lScade = Label(fCreato, width=LabelW, text="Scade", anchor="w", borderwidth=3, relief="sunken")
lScade.pack(side=LEFT)
Scade  = Label(fCreato, width=LabelW, text="scade", anchor="w", borderwidth=2, relief="raised")
Scade.pack(side=LEFT, fill=X, padx=PadX, pady=PadY)

TxtMsg = Text(WinMain, width=Width, height=10)
TxtMsg.pack(side=TOP, padx=PadX, pady=PadY)


WinMain.mainloop( )

