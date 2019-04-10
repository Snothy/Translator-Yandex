import requests, json
from tkinter import *
from tkinter import ttk #To make things look prettier

#Constants
apikey = "API KEY HERE"
url = "https://translate.yandex.net/api/v1.5/tr.json/"
root = Tk()

def resulttext(): #Set variables to global in order to pass them into the other function 
    global text 
    global language
    text = e1.get()
    language = e2.get()

def getresult(text, language):
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
        label4.config(text="Enter a correct language.")
        return
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

frame1=Frame(root)
frame1.pack()
frame2=Frame(root)
frame2.pack()
frame3=Frame(root)
frame3.pack()
frame4=Frame(root)
frame4.pack()

label1 = ttk.Label(frame1, text = "I'm a translator <3")
label1.pack(side=TOP)
label2 = Label(frame1, text = "Text: ")
label2.pack(side=LEFT)
label3 = Label(frame2, text= "Language: ")
label3.pack(side=LEFT)
label4 = Label(frame4, text = "Result")
label4.pack(side=LEFT)
label5 = Label(frame4, text= "")
label5.pack(side=RIGHT)

e1 = Entry(frame1)
e1.pack(side=LEFT)
e2 = Entry(frame2)
e2.pack(side=LEFT)

button1 = ttk.Button(frame3, text="Set", command = resulttext)
button1.pack(side=LEFT)
button2 = ttk.Button(frame3, text="Go", command = lambda:getresult(text,language)) #lambda to stop the function from getting empty inputs on startup
button2.pack(side=LEFT)

root.mainloop()