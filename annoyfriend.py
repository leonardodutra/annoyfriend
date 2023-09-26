import random
import pyautogui as pg
import time
variable=('hero','man','aaa')
time.sleep(8)
for i in range(500):
    a=random.choice(variable)
    pg.write("you are a "+a)
    pg.press('enter')
