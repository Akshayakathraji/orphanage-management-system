##importing modules

from tkinter import *
import base64

#initialize window
root = Tk()
root.geometry('500x300')
root.resizable(0,0)

#title of the window
root.title("Message Encrypt and Decrypt")



#label

Label(root, text ='ENCRYPT DECRYPT', font = 'arial 20 bold').pack()
#Label(root, text ='DataFlair', font = 'arial 20 bold').pack(side =BOTTOM)


#define variables

Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()


#######define function#####
#function to encode
def Encrypt(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
        
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()
#function to decode

def Decrypt(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
        
    return "".join(dec)
#function to set mode
def Mode():
    if(mode.get() == 'e'):
        Result.set(Encrypt(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decrypt(private_key.get(), Text.get()))
    else:        Result.set('Invalid Mode')



#Function to exit window
        
def Exit():
    root.destroy()

#################### Label and Button #############
#Message
Label(root, font= 'arial 12 bold', text='MESSAGE').place(x= 60,y=60)
Entry(root, font = 'arial 10', textvariable = Text, bg = 'ghost white').place(x=290, y = 60)

#key
Label(root, font = 'arial 12 bold', text ='KEY').place(x=60, y = 90)
Entry(root, font = 'arial 10', textvariable = private_key , bg ='ghost white').place(x=290, y = 90)


#mode
Label(root, font = 'arial 12 bold', text ='MODE(e-encrypt, d-decrypt)').place(x=60, y = 120)
Entry(root, font = 'arial 10', textvariable = mode , bg= 'ghost white').place(x=290, y = 120)



#result
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='ghost white').place(x=190, y = 155)

######result button
Button(root, font = 'arial 10 bold', text = 'RESULT'  ,width=6,padx =2,bg ='LightGray' ,command = Mode).place(x=160, y = 200)

#exit button
Button(root, font = 'arial 10 bold',text= 'EXIT' , width = 6, command = Exit,bg = 'LightGray', padx=2).place(x=250, y = 200)
root.mainloop()