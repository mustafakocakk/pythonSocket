#!/usr/bin/ env python
#-*- coding: utf-8 -*-

from Tkinter import *
import socket
pencere = Tk()
pencere.geometry("400x600")
soket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST = "localhost"
PORT = 8000

soket.connect((HOST,PORT))


def yolla():
        data=soket.recv(1024)
	al.insert(END,data)
        a=yolla.get("1.0",END)
        soket.send(a)
	#data = soket.recv(1024)
        #yolla.insert(END,data)
    	yolla.delete("1.0",END)		


buton1 = Button(text="yolla",command = yolla)
buton1.pack()	
al = Text(height=10 ,width=20 ,bg="yellow")
al.pack()


yolla= Text(height=3,width=20,bg="blue")
yolla.pack()


mainloop()
soket.close()
