from tkinter import  *
from tkinter import messagebox 
import base64
import os

    #la fonction decrypt
def decrypt():
    print("")

    #la fonction encrypt
def encrypt():
    passeword=code.get()
    if passeword=="1234":
        screen1=Toplevel(screen)
        screen1.title("encryption")
        screen.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message=texte1.get(1.0, END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        Label(screen1,text="ENCRYPT",font="arial",fg="white",bg="#ed3833").place(x=10,y=0)
        text2=Text(screen1,font="Rpbote",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)

        text2.insert(END,encrypt)
    elif passeword=="":
        messagebox.showerror("encryption", "Input Passeword")
    elif passeword !="1234":
        messagebox.showerror("encryption","Invalid Passeword")
    
def main_screen():

    global screen
    global code
    global texte1

    screen=Tk()
    screen.geometry("375x398")
    #icon
    image_icon = PhotoImage(file="keys.png")
    screen.iconphoto (False, image_icon)
    screen.title("PctApp")

    #La fonction de supression
    def reset():
        code.set("")
        texte1.delete('1.0',END)
    
    #Entrer le texte à encrypter ou à decrypter 
    Label(text="Enter text for encryption and decryption : ", fg="black", font=("calibri", 13)).place(x=10, y=10)
    texte1= Text(font="Robote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    texte1.place(x=10, y=50, width=355, height=100)
    
    #Entrer la clé 
    Label(text="Enter secret key for encryption and decryption: ", fg="black", font=("calibri",13)).place(x=10, y=170)
    code = StringVar()
    Entry(textvariable=code,width=19,bd=0,font=("arial",25), show='*').place(x=10,y=200)
    

    #les bottoms d'encreption et de decryption
    Button(text="ENCRYPT",height="2",width=23,bg="#ed3833",fg="white",bd=0,command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT",height="2",width=23,bg="#00bd56",fg="white",bd=0,command=decrypt).place(x=200, y=250)
    Button(text="RESET",height="2",width=50,bg="#1089ff",fg="white",bd=0,command=reset).place(x=10, y=300)
    screen.mainloop()
main_screen()