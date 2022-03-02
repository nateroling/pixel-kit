import PixelKit as kit
import random
import math

t = 40
b = 5


dial = 128 - round(kit.dial.read() / 32)
white = [dial, dial, dial]
pixels = [[white for i in range(0, 8)] for j in range(0, 16)]

def fadeC(val, amt):
    return min(128, max(0, val + amt))

def fade(color, amt):
    return [fadeC(v, amt) for v in color]

dir = -1

def sum1(input):
    return sum(map(sum, input))

class Iterator2D:

    def __init__(self, aMax, bMax):
        self.a = aMax-1
        self.b = bMax-1
        self.aMax = aMax
        self.bMax = bMax

    def __iter__(self):
        return self

    def __next__(self):
        if (self.b == self.bMax-1):
            self.b = 0
            if (self.a == self.aMax-1):
                self.a = 0
            else:
                self.a = self.a+1
        else:
            self.b = self.b + 1

        return [self.a, self.b]


indexes = Iterator2D(8, 16)

step = 100

x = 0
while True:
    x = x + 1

    dial = 128 - round(kit.dial.read() / 32)
    #ind = next(indexes)
    #pixels[ind[1]][ind[0]] = [dial,dial,dial]
    #if (x % 5 == 0):

    #idx = abs((x % 30) - 15)
    #pixels.pop(idx)
    #pixels.insert(idx, [[dial, dial, dial]]*8)

#    if (step == 0):
#        if (dir == 1):
#            step = 200
#            dir = -1
#        else:
#            step = 100
#            dir = 1
#    step = step - 1

    scale = 100
    bright = 50
    breath = abs((x - scale) % (scale * 2) - scale) / scale
    #breath = round(50 * math.sin(math.pi*breath))
    breath = round(bright * breath)

    for i in range(0, 16):
        for j in range(0, 8):
            v = pixels[i][j][0]
            if (random.random() < 1/4):
                pixels[i][j] = fade(pixels[i][j], dir)
            if (random.random() < 1/500):
                pixels[i][j] = [dial, dial, dial]
            #pixels[i][j] = fade(pixels[i][j], dir)

            #pixels[i][j] = [breath, breath, breath]



    # draw
    for i in range(0, 16):
        for j in range(0, 8):
            kit.set_pixel(i, j, pixels[i][j])
    kit.render()


