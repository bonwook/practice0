from pynput import keyboard

def on_press(key):
    print('Key {} pressed'.format(key))

def on_release(key):
    print('Key {} released'.format(key))
    if key == keyboard.Key.esc: #esc 키가 입력되면 종료
        return False
        
 # 리스너 등록방법1
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
