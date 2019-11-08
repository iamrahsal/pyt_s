from pynput.mouse import Controller
import time

mouse = Controller()
while True:
    a = list(mouse.position)
    mouse.position = (a[0]+1, a[1]+1)
    time.sleep(10)
