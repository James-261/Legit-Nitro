import time
import sys
import psutil
from os import listdir
from os.path import isfile, join
import os
import pyperclip
from pynput import keyboard
import tkinter as tk
import logging
import tkinter.ttk as ttk
from guizero import *
import pygetwindow as gw
from pynput.keyboard import Key, Controller

def quita():    
    sys.exit()

def copy1(beep):
    pyperclip.copy("https://raw.githubusercontent.com/James-261/nitrotest/main/soos/" + beep)
    vent()
    quita()

def vent():
    discard.activate()
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

amogus = []
keyboard = Controller()
root = App(title="Nitro", layout="grid", height=520, width=520)
discard = gw.getWindowsWithTitle('Discord')[0]

folder = os.path.dirname(os.path.abspath(__file__))
amogus = os.listdir(folder + "\\pack1\\soos")
sus = len(amogus)
red = 0
blue = 0 
yellow = 0

for imposter in amogus:
    imeg = os.path.join(folder, ("pack1\\soos\\" + imposter))
    b1 = PushButton(root, image=imeg, command=lambda imposter=imposter: copy1(imposter), grid=[blue,yellow])
    red += 1
    if blue != 5:
        blue += 1
    else:
        yellow += 1
        blue = 0

root.display()