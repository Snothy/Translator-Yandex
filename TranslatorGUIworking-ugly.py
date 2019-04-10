import requests, json
from tkinter import *

#Constants
apikey = "API KEY HERE"
url = "https://translate.yandex.net/api/v1.5/tr.json/"
root = Tk()
label = Label(root, text = "I'm a translator <3")
label.pack()
frame1=Frame(root)
frame1.pack(side=LEFT)
label2 = Label(frame1, text="Insert text here.:")
label2.pack(side = LEFT)
var = StringVar()
var2 = StringVar()
e = Entry(frame1, textvariable = var)
e.pack(side = LEFT)
#e.focus_set()
frame3 = Frame(root)
frame3.pack()
label5 = Label(frame3, text="language")
label5.pack(side=LEFT)
e2 = Entry(frame3, textvariable = var2)
e2.pack(side=LEFT)
#e2.focus_set()
#text = "I'm extremely hungry"
frame2 = Frame(root)
frame2.pack(side=BOTTOM)


def resulttext():
    global text 
    global language
    text = e.get()
    language = e2.get()
    print(text, language)



Button(frame2, text = "Set", command=resulttext).pack(side=RIGHT)


label3 = Label(frame2, text="Result: ")
label3.pack(side=LEFT)
label4 = Label(frame2, text ="")
label4.pack(side=RIGHT)
def getresult(text, language):
    print(text, language)
    #text = "I'm extremely hungry"
    #language = "bulgarian"
    text=text.replace(" ", "+")
    #Language form language dictionary
    lang_url = url+"getLangs?ui=en&key="+apikey
    lang_dict = requests.get(lang_url).json()["langs"]
    for key in lang_dict:
        if lang_dict[key] == language.capitalize() or language.lower() == key: #The dictionary has the values with a capital letter
            langto = key
        else:
            continue

    try:
        langto
    except:
        print("Incorrect language.")
    #Detecting input language
    detect_url = url+"detect?hint=en,bg,pt,es&key="+apikey+"&text="+text
    langfrom = requests.get(detect_url).json()["lang"]
    #Generating result
    result_url = url+"translate?text="+text+"&key="+apikey+"&lang="+langfrom+"-"+langto
    result_dict = requests.get(result_url).json()
    try:
        result = result_dict["text"][0]
    except:
        result = result_dict["message"]
    label4.config(text = result)
#def getresult():
 #   result.config(label4, txt = result)



Button(frame3, text="Go!", command=lambda:getresult(text, language)).pack()

root.mainloop()