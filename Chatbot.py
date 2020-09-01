#simple text chatbot- Sunshine
import pyttsx3 as p
import os
from time import sleep
from selenium import webdriver
print("Launching Sunshine")
p.speak("hey Namrata...")
p.speak("Tell me your requirement:")


i="input"
while True:
  print("Write Bye or bye to exit")
  i= input("Enter:")
  i=i.lower()
  if "browser" in i and not "chrome" in i and not "firfox" in i:
    p.speak("Namrata there are 2 options chrome and firefox. Choose one please")
    j=input("Enter:")
    j=j.lower()
    if "chrome"  in j or "chrome browser" in j:
      p.speak("opening chrome")
      print(os.system("chrome"))
    elif "firefox browser" in j or "firefox" in j:
      p.speak("opening firefox...")
      print(os.system("firefox"))
  elif "youtube" in i:
    p.speak("what u wanna search for??")
    print("What u wanna search for:")
    q=input()
    q=q.lower()
    p.speak("Okay! opening {} in YouTube".format(q))
    try:
      b = webdriver.Chrome()
    except:
      b = webbrowser.open()
    if "prakash" in q or "agarwal" in q:
      b.get('https://www.youtube.com/channel/UCzR0TCNb-c19_zNnsZKKiKA')
    elif "ml" in q or "machine learning" in q:
      b.get('https://www.youtube.com/watch?v=iVOxMcumR4A')
    else:
      b.get('https://www.youtube.com/results?search_query={}'.format(q))
    
  elif "text editor" in i and not "notepad" in i and not "sublime" in i:
    p.speak("Namrata there are 2 options notepad and sublime. Choose one please")   
    j=input("Enter:")
    j.lower()
    if "notepad"  in j or "notepad text editor" in j:
      p.speak("Okay! opening notepad")
      print(os.system("notepad"))
    elif "sublime text editor" in j or "sublime" in j:
      p.speak("Okay! opening sublime text editor...")
      print(os.system("sublime_text"))
  elif "chrome"  in i or "chrome browser" in i:
      p.speak("opening chrome")
      print(os.system("chrome"))
  elif "firefox browser" in i or "firefox" in i:
      p.speak("opening firefox...")
      print(os.system("firefox"))
  elif "notepad" in i or "notepad text editor" in i and "sublime" not in i:
    p.speak("opening notepad")
    print(os.system("notepad"))
  elif "sublime" in i or "sublime text editor" in i and "notepad" not in i:
    p.speak("opening sublime text editor")
    print(os.system("sublime_text"))
  elif "windows media player" in i or "media player" in i:
    p.speak("opening windows media player")
    print(os.system("wmplayer"))
  elif "Bye" in i or "bye" in i :
    p.speak("See you again Namrata!! \n BYE BYE")
    exit()
  else:
    p.speak("Sorry we do not support this ...")



