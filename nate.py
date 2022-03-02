from time import sleep
import machine
import random
import PixelKit as kit
import math

TICKS = 0
MAX = 8

# def random_colors(max):
#     for y in range(0, 8):
#         for x in range(0, 16):
#             kit.set_pixel(x, y, [int(random.random() * max),int(random.random() * max),int(random.random() * max)])
#     kit.render()

def clear():
    for y in range(0, 8):
        for x in range(0, 16):
            kit.set_pixel(x, y, [0,0,0])
    kit.render()

def random_colors(max):
    y = math.floor(random.random()*8);
    x = math.floor(random.random()*16);
    kit.set_pixel(x, y, [int(random.random() * max),int(random.random() * max),int(random.random() * max)])
    y = math.floor(random.random()*8);
    x = math.floor(random.random()*16);
    kit.set_pixel(x, y, [0,0,0])
    kit.render()

def dim1(component, amount):
    return max(0, component - amount)

def dim(color, amount):
    return [dim1(component, amount) for component in color]

def color_ramp(tick):
    for x in range(0, 16):
        for y in range(0, 8):
            xa = abs(8 - x)
            ya = abs(4 - y)
            a = abs(32 - (1.1 * tick + x) % 64)
            b = abs(32 - (1.2 * tick + x) % 64)
            c = abs(32 - (1.3 * tick + x) % 64)
            r = math.floor(a)
            g = math.floor(b)
            b = math.floor(c)
            kit.set_pixel(x, y, dim([r, g, b], 16))
    kit.render()


def brightness_up():
    global MAX
    MAX = min(128, MAX * 2)

def brightness_down():
    global MAX
    MAX = max(4, MAX / 2)

def redraw():
    color_ramp(TICKS)

def on_dial(value):
    global MAX
    MAX = (kit.dial.read() / 16) - 10
    random_colors(MAX)

kit.on_button_a = clear
kit.on_joystick_up = brightness_up
kit.on_joystick_down = brightness_down


def nate():
    global TICKS
    clear()
    while True:
        kit.check_controls()
        redraw()
        TICKS = TICKS + 1

