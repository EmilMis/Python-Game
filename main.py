import keyboard
import start_screen
import os
import random
import time
import pynput
from pynput.keyboard import Listener
import sys
import playsound
import pygame
import simpleaudio as sa

# Input an existing wav file name
wavFile = "kill.wav"
w_object = sa.WaveObject.from_wave_file(wavFile)

wavFile2 = "png.wav"
w_object2 = sa.WaveObject.from_wave_file(wavFile2)

hit = "hit.wav"
hit = sa.WaveObject.from_wave_file(hit)

tele = "t.wav"
tele = sa.WaveObject.from_wave_file(tele)

gun = "gun.wav"
gun = sa.WaveObject.from_wave_file(gun)

bomb = "boom.wav"
bomb = sa.WaveObject.from_wave_file(bomb)

tick = "tick.wav"
tick = sa.WaveObject.from_wave_file(tick)

bl = "bl.wav"
bl = sa.WaveObject.from_wave_file(bl)
# Print error message if the file does not exist

pygame.mixer.init()
pygame.mixer.music.load("y.wav")
pygame.mixer.music.play(-1)

dfing = False
count = 0
bomb_count = 8
last_moves = ["d"]
poss = []
mss = []

bombposs = []
bombmss = []

color = "bl"
prop = 5
cols = []

bombdelay = 0

def clear():
    # check and make call for specific operating system
    os.system("cls")

maze = [
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "o", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
     "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
     "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
     "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
     "-", "-", "-", "-", "-", "-"]
]

weap = "gun"
fire_poss = []
prop = 1
props = []


def push_bullets():
    for i in range(len(poss)):
        try:
            (x, y) = poss[i]
        except:
            break
        last_move = last_moves[len(last_moves) - 1]
        if x > 0 and x < len(maze) - 1 and y > 0 and y < len(maze[x]) - 1:
            try:
                if mss[i] == "w":
                    if maze[x - 1][y] == "+":
                        maze[x - 1][y] = " "
                        maze[x][y] = " "
                        poss.remove(poss[i])
                        mss.remove(mss[i])
                        try:
                            w_object.play()
                        except:
                            time.sleep(0)

                    else:
                        maze[x][y] = " "
                        maze[x - 1][y] = "|"
                        poss[i] = (x - 1, y)

                elif mss[i] == "a":
                    if maze[x][y - 1] == "+":
                        maze[x][y] = " "
                        maze[x][y - 1] = " "
                        poss.remove(poss[i])
                        mss.remove(mss[i])
                        try:
                            w_object.play()
                        except:
                            time.sleep(0)

                    else:
                        maze[x][y] = " "
                        maze[x][y - 1] = "="
                        poss[i] = (x, y - 1)

                elif mss[i] == "s":
                    if maze[x + 1][y] == "+":
                        maze[x][y] = " "
                        maze[x + 1][y] = " "
                        poss.remove(poss[i])
                        mss.remove(mss[i])
                        try:
                            w_object.play()
                        except:
                            time.sleep(0)

                    else:
                        maze[x][y] = " "
                        maze[x + 1][y] = "|"
                        poss[i] = (x + 1, y)

                elif mss[i] == "d":
                    if maze[x][y + 1] == "+":
                        maze[x][y] = " "
                        maze[x][y + 1] = " "
                        poss.remove(poss[i])
                        mss.remove(mss[i])
                        try:
                            w_object.play()
                        except:
                            time.sleep(0)

                    else:
                        maze[x][y] = " "
                        maze[x][y + 1] = "="
                        poss[i] = (x, y + 1)
            except:
                wall()
        else:
            continue
        wall()

def explosion(x, y):
    if len(get_pos("e")) > 0:
        remove_smoke()
    maze[x][y] = " "
    do_destroy = []
    for i in range(len(get_pos("+"))):
        (xp, yp) = get_pos("+")[i]
        if xp < x + 10 and xp > x - 10 and yp < y + 20 and yp > y - 20:
            do_destroy.append((xp, yp))
    for p in range(1):
        for i in range(5):
            for n in range(8):
                if x - i > 1:
                    maze[x - i][y] = "e"
                if x + i < len(maze) - 2:
                    maze[x + i][y] = "e"
                if y - n > 0:
                    maze[x][y - n] = "e"
                if y + n < len(maze[x]) - 2:
                    maze[x][y + n] = "e"
                if x + i < len(maze) - 2 and y + n < len(maze[x + i]) - 2:
                    maze[x + i][y + n] = "e"
                if x - i > 1 and y + n < len(maze[x - i]) - 2:
                    maze[x - i][y + n] = "e"
                if x + i < len(maze) - 2 and y - n > 1:
                    maze[x + i][y - n] = "e"
                if x - i > 1 and y - n > 1:
                    maze[x - i][y - n] = "e"
    for i in range(len(do_destroy)):
        (d, f) = do_destroy[i]
        maze[d][f] = " "

    wall()

def push_bombs():
    global bomb_count
    for i in range(len(bombposs)):
        try:
            (x, y) = bombposs[i]
        except:
            break
        last_move = last_moves[len(last_moves) - 1]
        if x > 0 and x < len(maze) - 1 and y > 0 and y < len(maze[x]) - 1:
            try:
                if bombmss[i] == "w":
                    if maze[x - 1][y] == "+":
                        explosion(x, y)
                        maze[x - 1][y] = " "
                        maze[x][y] = " "
                        bombposs.remove(bombposs[i])
                        bombmss.remove(bombmss[i])
                        try:
                            bomb.play()
                        except:
                            time.sleep(0)

                    else:
                        maze[x][y] = " "
                        maze[x - 1][y] = "."
                        bombposs[i] = (x - 1, y)

                elif bombmss[i] == "a":
                    if maze[x][y - 1] == "+":
                        explosion(x, y)
                        maze[x][y] = " "
                        maze[x][y - 1] = " "
                        bombposs.remove(bombposs[i])
                        bombmss.remove(bombmss[i])
                        try:
                            bomb.play()
                        except:
                            time.sleep(0)

                    else:
                        maze[x][y] = " "
                        maze[x][y - 1] = "."
                        bombposs[i] = (x, y - 1)

                elif bombmss[i] == "s":
                    if maze[x + 1][y] == "+":
                        explosion(x, y)
                        maze[x][y] = " "
                        maze[x + 1][y] = " "
                        bombposs.remove(bombposs[i])
                        bombmss.remove(bombmss[i])
                        try:
                            bomb.play()
                        except:
                            time.sleep(0)

                    else:
                        maze[x][y] = " "
                        maze[x + 1][y] = "."
                        bombposs[i] = (x + 1, y)

                elif bombmss[i] == "d":
                    if maze[x][y + 1] == "+":
                        explosion(x, y)
                        maze[x][y] = " "
                        maze[x][y + 1] = " "
                        bombposs.remove(bombposs[i])
                        bombmss.remove(bombmss[i])
                        try:
                            bomb.play()
                        except:
                            time.sleep(0)

                    else:
                        maze[x][y] = " "
                        maze[x][y + 1] = "."
                        bombposs[i] = (x, y + 1)
            except:
                wall()
        else:
            continue
        if bomb_count == 8:
            tick.play()
            bomb_count = 0
        else:
            bomb_count += 1
        wall()

def wall():
    global bombdelay
    for i in range(len(maze)):
        for n in range(len(maze[i])):
            if maze[i][n] != "-" and ((i == 0 or i == len(maze) - 1) or (n == 0 or n == len(maze[i]) - 1)):
                if maze[i][n] == "=" or maze[i][n] == "|":
                    index = poss.index((i, n))
                    mss.remove(mss[index])
                    poss.remove((i, n))
                    maze[i][n] = "-"
                    try:
                        hit.play()
                    except:
                        continue
                elif maze[i][n] == ".":
                    explosion(i, n)
                    index = bombposs.index((i, n))
                    bombmss.remove(bombmss[index])
                    bombposs.remove((i, n))
                    maze[i][n] = "-"
                    bomb.play()
                else:
                    maze[i][n] = "-"

def shoot():
    (x, y) = get_pos("o")[0]
    if last_move == "w":
        if x > 2:
            maze[x - 1][y] = "|"
            list = (x - 1, y)
            poss.append(list)
            mss.append("w")

    if last_move == "a":
        if y > 2:
            maze[x][y - 1] = "="
            list = (x, y - 1)
            poss.append(list)
            mss.append("a")

    if last_move == "s":
        if x < len(maze) - 3:
            maze[x + 1][y] = "|"
            list = (x + 1, y)
            poss.append(list)
            mss.append("s")

    if last_move == "d":
        if y < len(maze[x]) - 3:
            maze[x][y + 1] = "="
            list = (x, y + 1)
            poss.append(list)
            mss.append("d")
    try:
        w_object2.play()
    except:
        time.sleep(0)

def shoot_blaster():
    try:
        (x, y) = get_pos("o")[0]
    except:
        return False
    for i in range(len(maze)):
        if x + i + 1 < len(maze) - 1:
            if maze[x + 1 + i][y] == ".":
                index = bombposs.index((x + i + 1, y))
                bombmss.remove(bombmss[index])
                bombposs.remove((x + 1 + i, y))
            elif maze[x + i + 1][y] == "=" or maze[x + i + 1][y] == "|":
                index = poss.index((x + i + 1, y))
                mss.remove(mss[index])
                poss.remove((x + i + 1, y))

            maze[x + i + 1][y] = "3"
        if x - i - 1 > 0:
            if maze[x - 1 - i][y] == ".":
                index = bombposs.index((x - i - 1, y))
                bombmss.remove(bombmss[index])
                bombposs.remove((x - 1 - i, y))
            elif maze[x - i - 1][y] == "=" or maze[x - i - 1][y] == "|":
                index = poss.index((x - i - 1, y))
                mss.remove(mss[index])
                poss.remove((x - i - 1, y))
            maze[x - i - 1][y] = "3"

    for i in range(len(maze[x])):
        if y + i + 1 < len(maze[x]) - 1:
            if maze[x][y + i + 1] == ".":
                index = bombposs.index((x, y + 1 + i))
                bombmss.remove(bombmss[index])
                bombposs.remove((x, y + i + 1))
            elif maze[x][y + i + 1] == "=" or maze[x][y + i + 1] == "|":
                index = poss.index((x, y + i + 1))
                mss.remove(mss[index])
                poss.remove((x, y + i + 1))
            maze[x][y + i + 1] = "1"
        if y - i - 1 > 0:
            if maze[x][y - i - 1] == ".":
                index = bombposs.index((x, y - i - 1))
                bombmss.remove(bombmss[index])
                bombposs.remove((x, y - i - 1))
            elif maze[x][y - i - 1] == "=" or maze[x][y - i - 1] == "|":
                index = poss.index((x, y - i - 1))
                mss.remove(mss[index])
                poss.remove((x, y - i - 1))
            maze[x][y - i - 1] = "1"
    if x + 1 < len(maze) - 1 and y + 1 < len(maze[x]) - 1:
        maze[x  + 1][y + 1] = "3"
    if x + 1 < len(maze) - 1 and y - 1 > 0:
        maze[x  + 1][y - 1] = "3"
    if x - 1 > 1 - 0 and y + 1 < len(maze[x]) - 1:
        maze[x  - 1][y + 1] = "3"
    if x - 1 > 0 and y - 1 > 0:
        maze[x  - 1][y - 1] = "3"
    bl.play()

def update_bl():
    for i in range(len(maze)):
        for n in range(len(maze[i])):
            if maze[i][n] == "1" or maze[i][n] == "3":
                maze[i][n] = "2"
    wall()
def shoot_bomb():
    global color
    (x, y) = get_pos("o")[0]
    if last_move == "w":
        if x > 2:
            maze[x - 1][y] = "."
            list = (x - 1, y)
            bombposs.append(list)
            bombmss.append("w")

    if last_move == "a":
        if y > 2:
            maze[x][y - 1] = "."
            list = (x, y - 1)
            bombposs.append(list)
            bombmss.append("a")

    if last_move == "s":
        if x < len(maze) - 3:
            maze[x + 1][y] = "."
            list = (x + 1, y)
            bombposs.append(list)
            bombmss.append("s")

    if last_move == "d":
        if y < len(maze[x]) - 3:
            maze[x][y + 1] = "."
            list = (x, y + 1)
            bombposs.append(list)
            bombmss.append("d")
    try:
        w_object2.play()
    except:
        time.sleep(0)

    if color == "bl":
        cols.append(color)
        color = "re"

    elif color == "re":
        cols.append(color)
        color = "bl"



def move_bois():
    list = get_pos("+")
    las = get_pos("2")
    for i in range(len(list)):
        x = list[i][0]
        y = list[i][1]
        if True:
            while True:
                move = get_pos_to_move_bois(x, y)
                if move == 1:
                    if x > 1:
                        if maze[x - 1][y] == "|" or maze[x - 1][y] == "=":
                            maze[x - 1][y] = " "
                            maze[x][y] = " "
                            index = poss.index((x - 1, y))
                            poss.remove((x - 1, y))
                            mss.remove(mss[index])
                            w_object.play()
                        elif maze[x - 1][y] == ".":
                            explosion(x, y)
                            maze[x - 1][y] = " "
                            maze[x][y] = " "
                            index = bombposs.index((x - 1, y))
                            bombposs.remove((x - 1, y))
                            bombmss.remove(bombmss[index])
                            bomb.play()
                        elif maze[x - 1][y] == "2":
                            maze[x - 1][y] = "2"
                            maze[x][y] = " "
                        elif maze[x - 1][y] == "1":
                            maze[x - 1][y] = "1"
                            maze[x][y] = " "
                        elif maze[x - 1][y] == "3":
                            maze[x - 1][y] = "3"
                            maze[x][y] = " "
                        else:
                            maze[x][y] = " "
                            maze[x - 1][y] = "+"

                    else:
                        move = random.randint(1, 8)
                if move == 2:
                    if (x > 1) and (y < (len(maze[x]) - 2)):
                        if maze[x - 1][y + 1] == "|" or maze[x - 1][y + 1] == "=":
                            maze[x - 1][y + 1] = " "
                            maze[x][y] = " "
                            index = poss.index((x - 1, y + 1))
                            poss.remove((x - 1, y + 1))
                            mss.remove(mss[index])
                            w_object.play()
                        elif maze[x - 1][y + 1] == ".":
                            explosion(x, y)
                            maze[x - 1][y + 1] = " "
                            maze[x][y] = " "
                            index = bombposs.index((x - 1, y + 1))
                            bombposs.remove((x - 1, y + 1))
                            bombmss.remove(bombmss[index])
                            bomb.play()
                        elif maze[x - 1][y + 1] == "2":
                            maze[x - 1][y + 1] = "2"
                            maze[x][y] = " "
                        elif maze[x - 1][y + 1] == "1":
                            maze[x - 1][y + 1] = "1"
                            maze[x][y] = " "
                        elif maze[x - 1][y + 1] == "3":
                            maze[x - 1][y + 1] = "3"
                            maze[x][y] = " "
                        else:
                            maze[x][y] = " "
                            maze[x - 1][y + 1] = "+"
                        break
                    else:
                        move = random.randint(1, 8)
                if move == 3:
                    if y < (len(maze[x]) - 2):
                        if maze[x][y + 1] == "|" or maze[x][y + 1] == "=":
                            maze[x][y + 1] = " "
                            maze[x][y] = " "
                            index = poss.index((x, y + 1))
                            poss.remove((x, y + 1))
                            mss.remove(mss[index])
                            w_object.play()
                        elif maze[x][y + 1] == ".":
                            explosion(x, y)
                            maze[x][y + 1] = " "
                            maze[x][y] = " "
                            index = bombposs.index((x, y + 1))
                            bombposs.remove((x, y + 1))
                            bombmss.remove(bombmss[index])
                            bomb.play()
                        elif maze[x][y + 1] == "2":
                            maze[x][y + 1] = "2"
                            maze[x][y] = " "
                        elif maze[x][y + 1] == "1":
                            maze[x][y + 1] = "1"
                            maze[x][y] = " "
                        elif maze[x][y + 1] == "3":
                            maze[x][y + 1] = "3"
                            maze[x][y] = " "
                        else:
                            maze[x][y] = " "
                            maze[x][y + 1] = "+"
                        break
                    else:
                        move = random.randint(1, 8)
                if move == 4:
                    if x < len(maze) - 2 and y < (len(maze[x]) - 2):
                        if maze[x + 1][y + 1] == "|" or maze[x + 1][y + 1] == "=":
                            maze[x + 1][y + 1] = " "
                            maze[x][y] = " "
                            index = poss.index((x + 1, y + 1))
                            poss.remove((x + 1, y + 1))
                            mss.remove(mss[index])
                            w_object.play()
                        elif maze[x + 1][y + 1] == ".":
                            explosion(x, y)
                            maze[x + 1][y + 1] = " "
                            maze[x][y] = " "
                            index = bombposs.index((x + 1, y + 1))
                            bombposs.remove((x + 1, y + 1))
                            bombmss.remove(bombmss[index])
                            bomb.play()
                        elif maze[x + 1][y + 1] == "2":
                            maze[x + 1][y + 1] = "2"
                            maze[x][y] = " "
                        elif maze[x + 1][y + 1] == "1":
                            maze[x + 1][y + 1] = "1"
                            maze[x][y] = " "
                        elif maze[x + 1][y + 1] == "3":
                            maze[x + 1][y + 1] = "3"
                            maze[x][y] = " "
                        else:
                            maze[x][y] = " "
                            maze[x + 1][y + 1] = "+"
                        break
                    else:
                        move = random.randint(1, 8)
                if move == 5:
                    if x < (len(maze) - 2):
                        if maze[x + 1][y] == "|" or maze[x + 1][y] == "=":
                            maze[x + 1][y] = " "
                            index = poss.index((x + 1, y))
                            poss.remove((x + 1, y))
                            mss.remove(mss[index])
                            w_object.play()
                        elif maze[x + 1][y] == ".":
                            explosion(x, y)
                            maze[x + 1][y] = " "
                            maze[x][y] = " "
                            index = bombposs.index((x + 1, y))
                            bombposs.remove((x + 1, y))
                            bombmss.remove(bombmss[index])
                            bomb.play()
                        elif maze[x + 1][y] == "2":
                            maze[x + 1][y] = "2"
                            maze[x][y] = " "
                        elif maze[x + 1][y] == "1":
                            maze[x + 1][y] = "1"
                            maze[x][y] = " "
                        elif maze[x + 1][y] == "3":
                            maze[x + 1][y] = "3"
                            maze[x][y] = " "
                        else:
                            maze[x][y] = " "
                            maze[x + 1][y] = "+"
                        break
                    else:
                        move = random.randint(1, 8)
                if move == 6:
                    if x < (len(maze) - 2) and y > 1:
                        if maze[x + 1][y - 1] == "|" or maze[x + 1][y - 1] == "=":
                            maze[x + 1][y - 1] = " "
                            maze[x][y] = " "
                            index = poss.index((x + 1, y - 1))
                            poss.remove((x + 1, y - 1))
                            mss.remove(mss[index])
                            w_object.play()
                        elif maze[x + 1][y - 1] == ".":
                            explosion(x, y)
                            maze[x + 1][y - 1] = " "
                            maze[x][y] = " "
                            index = bombposs.index((x + 1, y - 1))
                            bombposs.remove((x + 1, y - 1))
                            bombmss.remove(bombmss[index])
                            bomb.play()
                        elif maze[x + 1][y - 1] == "2":
                            maze[x + 1][y - 1] = "2"
                            maze[x][y] = " "
                        elif maze[x + 1][y - 1] == "1":
                            maze[x + 1][y - 1] = "1"
                            maze[x][y] = " "
                        elif maze[x + 1][y - 1] == "3":
                            maze[x + 1][y - 1] = "3"
                            maze[x][y] = " "
                        else:
                            maze[x][y] = " "
                            maze[x + 1][y - 1] = "+"
                        break
                    else:
                        move = random.randint(1, 8)
                if move == 7:
                    if y > 1:
                        if maze[x][y - 1] == "|" or maze[x][y - 1] == "=":
                            maze[x][y - 1] = " "
                            maze[x][y] = " "
                            index = poss.index((x, y - 1))
                            poss.remove((x, y - 1))
                            mss.remove(mss[index])
                            w_object.play()
                        elif maze[x][y - 1] == ".":
                            explosion(x, y)
                            maze[x][y - 1] = " "
                            maze[x][y] = " "
                            index = bombposs.index((x, y - 1))
                            bombposs.remove((x, y - 1))
                            bombmss.remove(bombmss[index])
                            bomb.play()
                        elif maze[x][y - 1] == "2":
                            maze[x][y - 1] = "2"
                            maze[x][y] = " "
                        elif maze[x][y - 1] == "1":
                            maze[x][y - 1] = "1"
                            maze[x][y] = " "
                        elif maze[x][y - 1] == "3":
                            maze[x][y - 1] = "3"
                            maze[x][y] = " "
                        else:
                            maze[x][y] = " "
                            maze[x][y - 1] = "+"
                        break
                    else:
                        move = random.randint(1, 8)
                if move == 8:
                    if x > 1 and y > 1:
                        if maze[x - 1][y - 1] == "|" or maze[x - 1][y - 1] == "=":
                            maze[x - 1][y - 1] = " "
                            maze[x][y] = " "
                            index = poss.index((x - 1, y - 1))
                            poss.remove((x - 1, y - 1))
                            mss.remove(mss[index])
                            w_object.play()
                        elif maze[x - 1][y - 1] == ".":
                            explosion(x, y)
                            maze[x - 1][y - 1] = " "
                            maze[x][y] = " "
                            index = bombposs.index((x - 1, y - 1))
                            bombposs.remove((x - 1, y - 1))
                            bombmss.remove(bombmss[index])
                            bomb.play()
                        elif maze[x - 1][y - 1] == "2":
                            maze[x - 1][y - 1] = "2"
                            maze[x][y] = " "
                        elif maze[x - 1][y - 1] == "1":
                            maze[x - 1][y - 1] = "1"
                            maze[x][y] = " "
                        elif maze[x - 1][y - 1] == "3":
                            maze[x - 1][y - 1] = "3"
                            maze[x][y] = " "
                        else:
                            maze[x][y] = " "
                            maze[x - 1][y - 1] = "+"
                        break
                    else:
                        move = random.randint(1, 8)
def on_press(key):
    global weap
    global dfing
    if dfing == False:
        if key == key.up:
            move("w")
        elif key == key.down:
            move("s")
        elif key == key.right:
            move("d")
        elif key == key.left:
            move("a")
        elif key == key.enter:
            if weap == "gun":
                shoot()
            elif weap == "bomb":
                shoot_bomb()
            elif weap == "bl":
                shoot_blaster()
        elif key == key.space:
            if weap == "gun":
                weap = "bomb"
                bomb.play()
            elif weap == "bomb":
                weap = "bl"
                bl.play()
            elif weap == "bl":
                weap = "gun"
                gun.play()
        else:
            move(key)


def get_pos_to_move_bois(boisx, boisy):
    while True:
        try:
            try:
                (xo, yo) = get_pos("o")[0]
            except:
                clear()
                respawn()
                print_maze()
            if boisx > xo and boisy == yo:
                return 1
            elif boisx > xo and boisy < yo:
                return 2
            elif boisx == xo and boisy < yo:
                return 3
            elif boisx < xo and boisy < yo:
                return 4
            elif boisx < xo and boisy == yo:
                return 5
            elif boisx < xo and boisy > yo:
                return 6
            elif boisx == xo and boisy > yo:
                return 7
            else:
                return 8
            break
        except:
            continue

def remove_smoke():
    global prop
    if prop > 600:
        prop = 0
        if True:
            for i in range(len(maze)):
                for n in range(len(maze[i])):
                    if maze[i][n] == "e":
                        maze[i][n] = " "
                    else:
                        continue

def randommize():
    for i in range(10):
        spawn_enemy()

def spawn_enemy():
    free_coords = []
    for i in range(len(maze)):
        for n in range(len(maze[i])):
            if maze[i][n] == " ":
                cup = (i, n)
                free_coords.append(cup)
    (x, y) = random.choice(free_coords)
    maze[x][y] = "+"

to_up = 0

def print_maze():
    global to_up
    global color
    global prop
    for i in range(len(maze)):
        for n in range(len(maze[i])):
            if maze[i][n] == "-":
                print("█", end="")
            elif maze[i][n] == "o":
                print('\033[92m', end="")
                print("█", end="")
                print('\33[37m', end="")
            elif maze[i][n] == "+":
                print('\33[91m', end="")
                print("█", end="")
                print('\33[37m', end="")
            elif maze[i][n] == " ":
                print('\33[90m', end="")
                print("█", end="")
                print('\33[37m', end="")
            elif maze[i][n] == "|":
                print('\33[100m', end="")
                print('\33[34m', end="")
                print('\033[1m', end="")
                print("|", end="")
                print('\033[0m', end="")
                print('\33[37m', end="")
                print('\33[40m', end="")
            elif maze[i][n] == "=":
                print('\33[100m', end="")
                print('\33[34m', end="")
                print('\033[1m', end="")
                print("-", end="")
                print('\033[0m', end="")
                print('\33[37m', end="")
                print('\33[40m', end="")
            elif maze[i][n] == ".":
                index = bombposs.index((i, n))
                cor = cols[index]
                if cor == "bl":
                    print('\33[100m', end="")
                    print('\33[34m', end="")
                    print('\33[30m', end="")
                    print("●", end="")
                    print('\33[0m', end="")
                    print('\33[37m', end="")
                    print('\33[40m', end="")
                elif cor == "re":
                    print('\33[100m', end="")
                    print('\33[34m', end="")
                    print('\33[31m', end="")
                    print("●", end="")
                    print('\033[0m', end="")
                    print('\33[37m', end="")
                    print('\33[40m', end="")
            elif maze[i][n] == "e":
                choice = random.randint(1, 700)
                global prop
                remove_smoke()
                if choice > prop:
                    print('\33[41m', end="")
                    print('\33[34m', end="")
                    br = random.randint(1, 3)
                    if br == 2:
                        print('\33[31m', end="")
                    elif br == 1:
                        print('\33[103m', end="")
                    elif br == 3:
                        print('\033[43m', end="")
                    print(" ", end="")
                    print('\033[0m', end="")
                    print('\33[37m', end="")
                    print('\33[40m', end="")
                    prop += 3
                else:
                    print('\33[100m', end="")
                    print(" ", end="")
                    print('\33[40m', end="")
            elif maze[i][n] == "1":
                print('\33[100m', end="")
                print('\33[34m', end="")
                print('\033[1m', end="")
                print("-", end="")
                print('\033[0m', end="")
                print('\33[37m', end="")
                print('\33[40m', end="")

                if to_up > 400:
                    update_bl()
                else:
                    to_up += 1
            elif maze[i][n] == "2":
                print('\33[100m', end="")
                print('\33[34m', end="")
                print('\033[1m', end="")
                print("█", end="")
                print('\033[0m', end="")
                print('\33[37m', end="")
                print('\33[40m', end="")
            elif maze[i][n] == "3":
                print('\33[100m', end="")
                print('\33[34m', end="")
                print('\033[1m', end="")
                print("|", end="")
                print('\033[0m', end="")
                print('\33[37m', end="")
                print('\33[40m', end="")
            else:
                print(maze[i][n], end="")
        print()

def update_cols():
    for i in range(len(cols)):
        if cols[i] == "re":
            cols[i] = "bl"
        else:
            cols[i] = "re"

def get_pos(element):
    overall = []
    for i in range(len(maze)):
        for n in range(len(maze[i])):
            nov = []
            if maze[i][n] == element:
                nov.append(i)
                nov.append(n)
                overall.append(nov)
    return overall

def bl_delete():
    global to_up
    for i in range(len(maze)):
        for n in range(len(maze[i])):
            if maze[i][n] == "2":
                maze[i][n] = " "
    to_up = 0

def move(dir):
    list = get_pos("o")
    enemy_list = get_pos("+")
    try:
        x = list[0][0]
        y = list[0][1]
    except:
        clear()
        print_maze()
        return False
    if dir == "w":
        if x == 1:
            maze[x][y] = "o"
        else:
            maze[x][y] = " "
            maze[x - 1][y] = "o"
    elif dir == "s":
        if x == len(maze) - 2:
            maze[x][y] = "o"
        else:
            maze[x][y] = " "
            maze[x + 1][y] = "o"
    elif dir == "a":
        if y == 1:
            maze[x][y] = "o"
        else:
            maze[x][y] = " "
            maze[x][y - 1] = "o"
    elif dir == "d":
        if y == len(maze[x]) - 2:
            maze[x][y] = "o"
        else:
            maze[x][y] = " "
            maze[x][y + 1] = "o"
    list_new = get_pos("o")[0]
    (xn, yn) = list_new
    if list_new in enemy_list:
        maze[xn][yn] = "+"
    last_moves.append(dir)

randommize()

def respawn():
    if len(get_pos("o")) == 0:
        maze[1][2] = " "
        maze[2][1] = " "
        maze[2][2] = " "
        maze[1][1] = "o"

nump_old = len(get_pos("+"))

numm = 0
while True:
    with Listener(
            on_press=on_press) as listener:
        if True:
            clear()
            print_maze()
            respawn()
            try:
                last_move = last_moves[len(last_moves) - 1]
            except:
                last_move = "d"
            push_bombs()
            push_bullets()
            move_bois()
            update_cols()
            if len(get_pos("2")) > 0:
                if numm > 10:
                    bl_delete()
                    numm = 0
                else:
                    numm += 1
            if len(get_pos("+")) == 0:
                spawn_enemy()
            if len(get_pos("1")) > 0 or len(get_pos("2")) > 0 or len(get_pos("3")) > 0:
                dfing = True
            else:
                dfing = False