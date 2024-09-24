from tkinter import  *
from tkinter import messagebox 
import base64
import os

def main_screen():
    screen=Tk()
    screen.geometry("375x398")
    #icon
    image_icon = PhotoImage(file="keys.png")
    screen.iconphoto (False, image_icon)
    screen.title("PctApp")

    #Entrer le texte à encrypter ou à decrypter 
    Label(text="Enter text for encryption and decryption : ", fg="black", font=("calibri", 13)).place(x=10, y=10)
    texte1= Text(font="Robote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0).place(x=10, y=50, width=355, height=100)
    
    #Entrer la clé 
    Label(text="Enter secret key for encryption and decryption: ", fg="black", font=("calibri",13)).place(x=10, y=170)
    code = StringVar()
    Entry(textvariable=code,width=19,bd=0,font=("arial",25), show='*').place(x=10,y=200)
    

    #les bottoms d'encreption et de decryption
    Button(text="ENCRYPT",height="2",width=23,bg="#ed3833",fg="white",bd=0).place(x=10, y=250)
    Button(text="DECRYPT",height="2",width=23,bg="#00bd56",fg="white",bd=0).place(x=200, y=250)
    Button(text="RESET",height="2",width=50,bg="#1089ff",fg="white",bd=0).place(x=10, y=300)
    screen.mainloop()
main_screen()