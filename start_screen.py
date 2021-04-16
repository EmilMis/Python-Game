import os
from pynput.keyboard import Listener
from pynput import *
import simpleaudio as sa

run = "run.wav"
run2 = sa.WaveObject.from_wave_file(run)

to_stop = False
to_quit = False

pos = "left"

os.system("cls")

def print_options():
    global pos
    print(r"""
                                    ██    ███████    █████████     █         ███████    █████████   ██
                                  ██     █               █        █ █       █       █       █         ██
                                ██       █               █       █   █      ████████        █           ██
                              ██          ███████        █      █     █     ███             █             ██
                                ██               █       █     █████████    █  ██           █           ██
                                  ██             █       █    █         █   █    ██         █         ██
                                    ██    ███████        █   █           █  █      ██       █       ██""")
    print()
    if pos == "left":
        print("                                          ", end="")
        print('\33[102m', end="")
        print("           PLAY          ", end="")
        print('\33[40m', end="")
        print("           QUIT          ", end="")
    else:
        print("                                          ", end="")
        print("           PLAY          ", end="")
        print('\33[101m', end="")
        print("           QUIT          ", end="")
        print('\33[40m', end="")
    print("\n\n\n")




def on_press(key):
    global pos
    global to_stop
    global to_quit
    while True:
        try:
            if key == key.left:
                if pos == "left":
                    pos = "left"
                    #select2.play()
                else:
                    pos = "left"
            elif key == key.right:
                if pos == "right":
                    pos = "right"
                    #select2.play()
                else:
                    pos = "right"
            elif key == key.enter:
                if pos == "right":
                    to_stop = True
                    run2.play()
                else:
                    to_quit = True
            break
        except:
            continue
    os.system("cls")
    print_options()

print_options()
with keyboard.Listener(
            on_press=on_press) as listener:
    while True:
        if to_quit == True:
            break
        if to_stop == True:
            quit()