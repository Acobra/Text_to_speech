from gtts import gTTS
from bs4 import BeautifulSoup
import requests
import os
print("Press 1 to enter whom u want to search:")
print("Press 2 to know About")
print("Press 3 to Exit")
lan='en'
choice=int(input())
if choice==1:
    word=input('enter name of the thing you want:')
    try:
        word.replace(" ", "_").capitalize()
        word+='_'
        print(word)
        word2=input("enter surname if exits")
        word2.capitalize()
        new_word = word + word2
        url=f'https://en.wikipedia.org/wiki/{new_word}'
        info=requests.get(url).text
        soup=BeautifulSoup(info,'html.parser')
        #print(soup.text)
        p = soup.find('div',class_='mw-parser-output').find_all('p')[1].text
        p.replace("\n","end=''")
        print(p)
        out=gTTS(text=p,lang=lan,slow=False)
        out.save("new.mp3")
        os.system("new.mp3")
    except :
        text="retype using spaces between words else it wont work and also refer relevant words only"
        text.replace(" ","")
        out=gTTS(text=text,lang=lan,slow=False)
        out.save("new.mp3")
        os.system("new.mp3")

elif choice==2:
    print(f'This script is a little text to voice info script that gives you some basic info')
    text=' this is made by aayush Singh organization name azeus'
    text.replace(" ","")
    lan='en'
    out=gTTS(text=text,lang=lan,slow=False)
    out.save("new.mp3")
    os.system("new.mp3")
elif choice==3:
    os._exit(1)
else:
    text=" kindly choose a valid operation"
    text.replace(" ", "")
    lan='en'
    out = gTTS(text=text, lang=lan, slow=False)
    out.save("new.mp3")
    os.system("new.mp3")
#Kapil_Sharma_(comedian)