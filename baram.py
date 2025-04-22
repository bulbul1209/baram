# # #8qarQ

import keyboard
import mouse
import time

def one():
    time.sleep(0.02)
    keyboard.press_and_release('esc')  # '1' 입력
    time.sleep(0.02)    
    keyboard.press_and_release('6')  # 'right' 입력

def repeat_left():
    time.sleep(0.03)
    keyboard.press_and_release('esc')   
    time.sleep(0.03)
    keyboard.press_and_release('6')  # '1' 입력
    time.sleep(0.05)        
    keyboard.press_and_release('left')  # 'right' 입력
    time.sleep(0.05) 
    keyboard.press_and_release('enter')  # 'enter' 입력

    

def repeat_right():
    time.sleep(0.03)
    keyboard.press_and_release('esc')       
    time.sleep(0.03)
    keyboard.press_and_release('6')  # '1' 입력
    time.sleep(0.05)        
    keyboard.press_and_release('right')  # 'right' 입력      
    time.sleep(0.05) 
    keyboard.press_and_release('enter')  # 'enter' 입력


        
def repeat_3():
    time.sleep(0.02)
    keyboard.press_and_release('3')
    time.sleep(0.1)   
    keyboard.press_and_release('3')    
    time.sleep(0.1)
    keyboard.press_and_release('3')   
    time.sleep(0.1)
    keyboard.press_and_release('3')
    time.sleep(0.1)    
    keyboard.press_and_release('3')

def on_click():    
    time.sleep(0.02)  # 클릭 후 약간의 딜레이
    keyboard.press_and_release('enter')

            

if __name__ == "__main__":
    print("F1 키를 누르면 1-left-enter 반복 실행, F3 키를 누르면 3이 5번 입력됩니다.")
    print("마우스 왼쪽 클릭 시 자동으로 Enter 키 입력됩니다. 종료하려면 Ctrl+C를 누르세요.")

    #마우스 오른쪽 클릭 감지 후 enter 입력
    mouse.on_click(on_click)

    while True:
        event = keyboard.read_event()  # 키 입력 감지
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'f1':
                repeat_left()
            elif event.name == 'f2':              
                repeat_right()                
            elif event.name == 'f3':
                repeat_3()
            elif event.name == 'f4':
                keyboard.press_and_release('esc')                                
                time.sleep(0.05)
                keyboard.press_and_release('3')
                time.sleep(0.05)
                keyboard.press_and_release('home')
                time.sleep(0.05)
                keyboard.press_and_release('enter')
                time.sleep(0.05)
                keyboard.press_and_release('3')
                time.sleep(0.05)
                keyboard.press_and_release('enter')
                time.sleep(0.05)
                keyboard.press_and_release('tab')
                time.sleep(0.1)
                keyboard.press_and_release('tab')
            elif event.name == 'f5':
                keyboard.press_and_release('esc')                
                time.sleep(0.05)
                keyboard.press_and_release('8')
                time.sleep(0.05)              
                keyboard.press_and_release('home')             
                time.sleep(0.05)                
                keyboard.press_and_release('enter')
                time.sleep(0.05)
                
            elif event.name == '`':
                one()                 

            # elif event.name == 'caps lock':
            #     time.sleep(0.02)
            #     keyboard.press_and_release('esc')
            #     time.sleep(0.02)                
            #     keyboard.press_and_release('6')            


            elif event.name == 'delete':
                time.sleep(0.02)                
                keyboard.press_and_release(',')

            elif event.name == 'caps lock':
                time.sleep(0.02)                
                keyboard.press_and_release(',')






