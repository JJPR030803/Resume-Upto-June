import pyautogui as pygui


wh = pygui.size()

for i in range(0):
    pygui.moveTo(100,100,duration=0.25)
    pygui.moveTo(200,100,duration=0.25)
    pygui.moveTo(200,200,duration=0.25)
    pygui.moveTo(100,200,duration=0.25)
    print(pygui.position())

for i in range(0):
    pygui.move(100,0,duration=0.25)
    pygui.move(0,100,duration=0.25)
    pygui.move(-100,0,duration=0.25)
    pygui.move(0,-100,duration=0.25)
    print(pygui.position())
    
pygui.click(170,40)
