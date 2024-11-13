import os, PIL, cv2

import numpy as np

from colors import Colors

files = os.listdir('OutputEncoder/TextFormat')

colors = Colors()
calibration = colors.load()

for f in files:
    name = f

    data = []
    with open('OutputEncoder/TextFormat/' + name) as fname:
        lines = fname.readlines()
        for line in lines:
            data.append(line.strip('\n'))

    array = []
    for line in data:
        array.append(eval(line))

    img = np.zeros((len(array), len(array[0]), 3), np.uint8)
    colorList = []

    for line in array:
        l = []
        for code in line:
            find = False
            for color in colors.colors:
                if code == color[0]:
                    l.append(color[1])
                    find = True
            if find == False:
                l.append((252, 186, 3))
        colorList.append(l)

    print(colorList)

    yCount = 0
    for l in colorList:
        xCount = 0
        for color in l:
            img[yCount, xCount] = color
            xCount += 1
        yCount += 1

    cv2.imwrite('OutputDecoder/' + name + '.png', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
