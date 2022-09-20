from fnmatch import translate
from tkinter import *
from tkinter import ttk,messagebox
import googletrans 
from googletrans import Translator
import pyttsx3


root=Tk()
root.title("Google Translate")
root.geometry("1100x500")
root.resizable(False,False)
root.configure(bg="white")
#icon
root.iconbitmap("trans.ico")


engine=pyttsx3.init()

def speaknow1():
    txt1=text1.get(1.0,END)
    for voice in engine.getProperty('voices'):
        print(f"Voice: {voice.name}")
    engine.setProperty('voice', voice.id)    
    engine.say(txt1)
    engine.runAndWait()
    engine.stop()

def speaknow2():
    txt2=text2.get(1.0,END)
    for voice in engine.getProperty('voices'):
        print(f"Voice: {voice.name}")
    engine.setProperty('voice', voice.id)  # for female voice  
    engine.say(txt2)
    engine.runAndWait()
    engine.stop()


def label_change():
    c1=combo1.get()
    c2=combo2.get()
    label1.configure(text=c1)
    label2.configure(text=c2)
    root.after(1000,label_change)

def translate_now():
    text_=text1.get(1.0,END)
    t1=Translator()
    trans_text=t1.translate(text_,src=combo1.get(),dest=combo2.get())
    trans_text=trans_text.text

    text2.delete(1.0,END)
    text2.insert(END,trans_text)

obj=LabelFrame(root,text="Translator with Text to speech",font=5,bd=2)
obj.pack(fill="both",expand="yes",padx=10,pady=10)

#image
mid_image = PhotoImage(file="C:/Users/ahnaf\Documents/Pycharm Projects/Translator with Speech/trans2.png")
image_label=Label(obj,image=mid_image,width=150)
image_label.place(x=460,y=50)



language = googletrans.LANGUAGES
languageV= list(language.values())
lang1=language.keys()



# first Text Box
combo1=ttk.Combobox(obj ,values=languageV ,font="Roboto 14",state="r")
combo1.place(x=110,y=20)
combo1.set("English")

label1=Label(obj,text="English",font="segoe 15",bg="white",width=18,bd=2 ,relief=GROOVE)
label1.place(x=130,y=50)

# first text box frame
f1=Frame(obj,bg="Black",bd=2)
f1.place(x=10,y=118,width=440,height=210)

text1=Text(f1,font="Roboto 20",bg="white",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)


scrolibar1=Scrollbar(f1)
scrolibar1.pack(side="right",fill="y")

scrolibar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrolibar1.set)

btn1=Button(obj,text="speak",font=20,bg="black",fg="white",command=speaknow1)
btn1.place(x=350,y=350)  



# 2nd Text Box
combo2=ttk.Combobox(obj,values=languageV,font="Roboto 14",state="r")
combo2.place(x=730,y=20)
combo2.set("select your language")

label2=Label(obj,text="English",font="segoe 15",bg="white",width=18,bd=2,relief=GROOVE)
label2.place(x=750,y=50)

# 2nd text box frame
f2=Frame(obj,bg="Black",bd=2)
f2.place(x=620,y=118,width=440,height=210)

text2=Text(f2,font="Roboto 20",bg="white",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)


scrolibar2=Scrollbar(f2)
scrolibar2.pack(side="right",fill="y")

scrolibar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrolibar2.set)

btn2=Button(obj,text="speak",font=20,bg="black",fg="white",command=speaknow2)
btn2.place(x=950,y=350) 


#translate_button
translate=Button(obj,text="Translate",font=("Roboto",15),
                activebackground="lightblue",cursor="hand2",bd=1,width=10,height=2,
                bg="lightgreen",fg="white",command= translate_now)
translate.place(x=480,y=250)                

label_change()

root.mainloop()