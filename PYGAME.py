import  pygame
pygame.init()
screen= pygame.display.set_mode((1530,800))
pygame.display.set_caption("salhi omar")
icon=pygame.image.load('car.png')
pygame.display.set_icon(icon)
lo=pygame.image.load('Untitled.png')
px=200
py=100
def text():
    screen.blit(lo,(px,py))
cotrol=True
while cotrol:
    screen.fill((200, 40, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cotrol=False

    text()
    pygame.display.update()