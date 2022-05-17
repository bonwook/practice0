from tabnanny import check
from pynput import keyboard
import win32api

MyHotkey = [
    {"function1" : {keyboard.Key.ctrl_l, keyboard.Key.alt_l,keyboard.KeyCode(char = "n")}}
]

curr = set()

def function1():
    print("함수1 호출")
    win32api.WinExec("calc.exe") #계산기 띄움

def on_press(key):
    print('{} pressed'.format(key))
    for data in MyHotkey:
        FUNCTION = list(data.keys())[0]
        KEYS = list(data.values())[0]

        if key in KEYS:
            curr.add(key)

            if all(k in curr for k in KEYS): #모두 있으면 만족하고
                    function = eval(FUNCTION)
                    function()



def on_release(key):
    print('{} released'.format(key))

    if key in curr:
        curr.remove(key)
    if key == keyboard.Key.esc: #esc 키가 입력되면 종료
        return False
        
 # 리스너 등록방법1
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
