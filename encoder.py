import pygame, os, pyautogui, PIL, json

from colors import Colors

pygame.init()

size = [840, 1188]
screen = pygame.display.set_mode(size)

files = os.listdir('InputEncoder')

count = [
        ['N10', 0],
        ['04', 0],
        ['M3', 0],
        ['C2', 0],
        ['B34', 0],
        ['N01', 0],
        ['N21', 0],
        ['N19', 0],
        ['017', 0],
        ['C14', 0],
        ['040', 0],
        ['M20', 0],
        ['C18', 0],
        ['048', 0],
        ['M49', 0],
        ['C50', 0],
        ['N11', 0],
        ['022', 0],
        ['M16', 0],
        ['C15', 0],
        ['042', 0],
        ['M24', 0],
        ['C32', 0],
        ['044', 0],
        ['M43', 0],
        ['C41', 0],
        ['N09', 0],
        ['030', 0],
        ['M29', 0],
        ['C28', 0],
        ['R26', 0],
        ['N05', 0],
        ['012', 0],
        ['M8', 0],
        ['C6', 0],
        ['N07', 0],
        ['E60', 0],
        ['E80', 0],
        ['E100', 0],
        ['L46', 0],
        ['NoN', 0]
        ]

colors = Colors()
calibration = colors.load()

for f in files:
    name = f[5:8]

    image = pygame.image.load('InputEncoder/' + f)
    im = PIL.Image.open('InputEncoder/' + f)
    colorList = []
    
    for y in range(image.get_height()):
        l = []
        for x in range(image.get_width()): 
            l.append(im.getpixel((x, y)))
        colorList.append(l)

    codeList = []
    
    yc = 0
    for color in colorList:
        xc = 0
        l = []
        for color in colorList[yc]:
            found = False
            for c in calibration:
                minRGB = c[1]
                maxRGB = c[2]
                if color[0] >= minRGB[0] and color[0] <= maxRGB[0] and color[1] >= minRGB[1] and color[1] <= maxRGB[1] and color[2] >= minRGB[2] and color[2] <= maxRGB[2]:
                    l.append(c[0])
                    for code in count:
                        if c[0] == code[0]:
                            code[1] += 1
                    found = True
            if found == False:
                l.append(' - ')
                count[len(count) - 1][1] += 1
            xc += 1
        codeList.append(l)
        yc += 1

    fSize = 12
    nameFont = pygame.font.SysFont('arial', 26)
    font = pygame.font.SysFont('arial', fSize)

    surfaceList = []
    surfaceMatrix = []

    ycount = 0
    for code in codeList:
        xcount = 0
        l = []
        for code in codeList[ycount]:
            l.append(font.render(code, True, (0, 0, 0)))
            xcount += 1
        surfaceList.append(l)
        ycount += 1

    title = nameFont.render(name, True, (0, 0, 0))

    squareSize = 40

    gridSize = [17, 24]

    xOffset = 28
    yOffset = 60
    spacing = 7

    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    yCount = 0
    for surf in surfaceList:
        xCount = 0
        for surf in surfaceList[yCount]:
            xcenter = 0 #squareSize//2 - ((fSize//2) * 3)
            ycenter = 0 #fSize//2
            screen.blit(surf, (((squareSize + spacing) * xCount) + xOffset ,((squareSize + spacing) * yCount) + yOffset))
            xCount += 1
        yCount += 1

    screen.blit(title, (size[0]/2, 15))

    f = open('OutputEncoder/TextFormat/Hoja' + name + '.txt','w')
    for line in codeList:
        f.write(str(line) + '\n')
    f.close()

    pygame.display.update()
    pygame.image.save(screen, 'OutputEncoder/Hoja ' + name + '.png')


f = open('Cantidades.txt', 'w')
for code in count:
    f.write(str(code) + '\n')
f.close()

print('Cantidades de venecitas:')
print(count)

