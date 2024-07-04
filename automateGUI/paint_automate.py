import subprocess,time
import pyautogui._pyautogui_win as pygwin
import pyautogui as pyg



pyg.hotkey('alt','tab')

time.sleep(1)
pyg.press(keys='enter')


time.sleep(1)
height,width = pyg.size()

position_center = pyg.center((0,0 ,width,height))

center_position = (960,540)


pyg.moveTo(center_position)



distance = 300
change = 20
while distance>0:
    pyg.drag(distance,0,duration=0.2)
    distance = distance-change
    pyg.drag(0,distance,duration=0.2)
    pyg.drag(-distance,0,duration=0.2)
    distance = distance-change
    pyg.drag(0,-distance,duration=0.2)