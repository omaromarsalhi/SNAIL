y = True
while y:
    date = input('give the time ')
    if (len(date) == 5) and (date[2] == ':'):
        tab = [date[0], date[1], date[3], date[4]]
        for i in tab:
            if int(i) in range(0, 24):
                y = False
    else:
        y = True
import time

t = time.localtime()
tim=int(date[0]+date[1])-int(time.strftime("%H", t))
minn=int(date[3]+date[4])-int(time.strftime("%M", t))
time.sleep((tim*3600+minn*60)-30)
while True:
    cotrol = True
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    if str(date) == str(current_time):
        cotrol = True

        import pygame

        pygame.init()
        screen = pygame.display.set_mode((1530, 800))
        pygame.display.set_caption("salhi omar")
        icon = pygame.image.load('car.png')
        pygame.display.set_icon(icon)
        lo = pygame.image.load('Untitled.png')
        px = 200
        py = 100


        def text():
            screen.blit(lo, (px, py))


        while cotrol:
            screen.fill((200, 40, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    cotrol = False

            text()
            pygame.display.update()
    if cotrol == False:
        break
