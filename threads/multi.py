import threading,time

print('Start of program')

def takeNap():
    time.sleep(5)
    print('Wake Up')
    
threadObj = threading.Thread(target=print,args=['Cats','Dogs','Frogs'],kwargs={'sep':' & '})
threadObj.start()

print('End of program')