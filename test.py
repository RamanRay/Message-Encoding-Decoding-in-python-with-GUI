from tkinter import *
from tkinter import messagebox
import base64
import os



def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
        
    return "".join(dec)


def button_decode():
    screen2=Toplevel(screen)
    screen2.title("decode")
    screen2.geometry("400x200")
    screen2.resizable(0,0)
    screen2.configure(bg="#00bd56")

    Label(screen2,text="DECODE",font="arial",fg="white",bg="#00bd56").place(x=10,y=0)
    text2=Text(screen2,font="Rpbote 10", bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text2.place(x=10,y=40,width=380,height=150)

    text2.insert(END,Decode(key1.get(),text1.get(1.0,END)))

def Encode(key,message):
    
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
        
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def button_encode():
    screen1=Toplevel(screen)
    screen1.title("encode")
    screen1.geometry("400x200")
    screen1.resizable(0,0)
    screen1.configure(bg="#ed3833")
    Label(screen1,text="ENCODE",font="arial",fg='white',bg="#ed3833").place(x=10,y=0)
    text2=Text(screen1,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text2.place(x=10,y=40,width=380,height=150)

    text2.insert(END,Encode(key1.get(),text1.get(1.0,END)))

def main_screen():

    global screen
    global key1
    global text1
    
    screen=Tk()
    screen.geometry("375x398")
    screen.resizable(0,0)
    #icon
    image_icon=PhotoImage(file="key.png")
    screen.iconphoto(False,image_icon)
    screen.title("Encoding/Decoding")

    def reset():
        key1.set("")
        text1.delete(1.0,END)
    text1=StringVar()
    Label(text="Enter text for encoding and decoding",fg="black",font=("calbrti",13)).place(x=10,y=10)
    text1=Text(screen,bd=0,font="Robote 20",bg="white",wrap=WORD)
    text1.place(x=10,y=50,width=355,height=100)

    Label(text="Enter secret key for encoding and decoding",fg="black",font=("calibri",13)).place(x=10,y=170)

    key1=StringVar()
    Entry(textvariable=key1,width=19,bd=0,font=("arial",25),show="*").place(x=10,y=200)

    Button(text="ENCODE",height="2",width=23,bg="#ed3833",fg="white",bd=0,command=button_encode).place(x=10,y=250)
    Button(text="DECODE",height="2",width=23,bg="#00bd56",fg="white",bd=0,command=button_decode).place(x=200,y=250)
    Button(text="RESET",height="2",width=50,bg="#1089ff",fg="white",bd=0,command=reset).place(x=10,y=300)
    



    screen.mainloop()



main_screen()