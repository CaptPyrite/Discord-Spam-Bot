import requests
import time
import random
import keyboard

payload = {
    "content":random.uniform(-1,1)
}

header = {
    "authorization":"YOUR DISCORD AUTHORIZATION"
}

msg_count = 0

print("press Ctrl+Q to quit")
while keyboard.is_pressed("ctrl+q") != True:
    if msg_count >= 5:
        time.sleep(4.5)
        msg_count = 0
    else:
        r = requests.post("CHANEL ID",data=payload,headers=header)
        payload["content"] = random.uniform(-1,1)
    msg_count += 1
print("Stoped the program")
