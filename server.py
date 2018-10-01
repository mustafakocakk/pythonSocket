#!/usr/bin/ env python
#-*- coding: utf-8 -*-

import socket
from  Tkinter import *

pencere = Tk()
pencere.geometry("200x300")
soket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST = "localhost"
PORT = 8000
veri = 1024 
soket.bind((HOST,PORT))
print "%s:%d server başlatıldı." % (HOST,PORT)
print "Kullanıcı bekleniyor."
soket.listen(5)

baglanti , adres = soket.accept()
print "Bir bağlantı kabul edildi.", adres
def yolla_al():
        g = giden.get(1.0,END)
        baglanti.send(g)
	data=baglanti.recv(veri)
        gelen.insert(END,data)
       	giden.delete("1.0",END)

buton1=Button(text="yolla",command=yolla_al)
buton1.pack()

gelen=Text(height=10,width=20,bg="white")
gelen.pack()
 
giden =Text(height = 3,width=20,bg="blue")
giden.pack()

mainloop()
soket.close()

