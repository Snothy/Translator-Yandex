#Translator with GUI
#######No forgetterino : According to the Terms of Use for the Yandex.Translate service, the text Powered by Yandex.Translate must be shown above or below the translation result, with a clickable link to the page http://translate.yandex.com/.
#Yandex translator docs: https://tech.yandex.com/translate/doc/dg/concepts/About-docpage/
import json, requests

text = input("Transalte: ")
language = input("To what language?: ").capitalize()
#text = "Много съм красив. Но за жалост съм и гладен."
#language = "english"

yandex_key = "API KEY HERE"
url = "https://translate.yandex.net/api/v1.5/tr.json/"
#### Supported languages dictionary ####
lang_url = url+"getLangs?ui=en&key="+yandex_key
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
texturl = text.replace(" ", "+")
#### Detect input language ####
detect_url = url+"detect?hint=en,bg,pt,es&key=" + yandex_key+"&text="+texturl
langfrom = requests.get(detect_url).json()["lang"]

#print(detect_url)

#### Translation ####
result_url = url + "translate?text="+texturl+"&key="+yandex_key+"&lang="+langfrom+"-"+langto
result_dict = requests.get(result_url).json()
#print(result_url)
try:
    result = result_dict["text"][0]
except:
    result = result_dict["message"]
print(result)