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


COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(vk=162)}  # control + alt
]

def execute():
    folder = os.path.dirname(os.path.abspath(__file__))
    phil = folder + "\\show.py"
    os.popen("python " + phil)
    sys.exit()

def get_vk(key):
    return key.vk if hasattr(key, 'vk') else key.value.vk

def is_combination_pressed(combination):
    return all([get_vk(key) in pressed_vks for key in combination])

def on_press(key):
    vk = get_vk(key)  
    pressed_vks.add(vk)  

    for combination in COMBINATIONS:  
        if is_combination_pressed(combination):  
            execute()  
            break 

def on_release(key):
    vk = get_vk(key)  
    pressed_vks.remove(vk) 

pressed_vks = set()

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()



