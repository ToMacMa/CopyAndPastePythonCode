import tkinter as tk
import requests



i = 0
while 13 > i:
    print("")
    i = i + 1

def downloadFile(link, saveName):
    url = str(link)
    r = requests.get(url, allow_redirects=True)
    open(str(saveName), 'wb').write(r.content)
def downloads():
    downloadFile('https://raw.githubusercontent.com/ToMacMa/CopyAndPastePythonCode/main/requiredData.json', 'requiredData.json')
    with open("main.py", "w") as file:
        file.write("")
    downloadFile('https://raw.githubusercontent.com/ToMacMa/CopyAndPastePythonCode/main/main.py', 'main.py')
if 0 == 1:
    downloads()


import main

main.StartWindow("500x300", "Main window")
