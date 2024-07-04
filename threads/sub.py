import subprocess
paintProc = subprocess.Popen('C:\\Windows\\System32\\calc.exe')
text = subprocess.Popen(['C:\\Windows\\notepad.exe','C:\\Users\Al\\hello.txt'])
paintProc.wait()
print(paintProc.poll() == None)