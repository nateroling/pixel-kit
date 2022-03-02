import PixelKit as kit
import random

kit.clear()

while True:
    sleep(1)
    color = [random.randrange(5, 20), random.randrange(5, 20), random.randrange(5, 20)]
    if (random.randint(0, 10) < 10):
        color = [0, 0, 0]
    kit.set_pixel(random.randrange(16), random.randrange(8), color)
    kit.render()
