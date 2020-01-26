import pygame
from Defs import *
from Classes import *
from Locations.Map import Map
from Locations.Town import Town
from Locations.MenuBar import MenuBar
from Locations.Book import Book
from Locations.Blank import Blank
from Locations.znShablon import znShablon

pygame.init()

if open('settings/quest.data', 'r').read() == "NONE": #----------------------------------------------------очень жесткий костыль - надо придумать как пофиксить
    f = open('settings/quest.data', 'w')
    f.write('mat')
    f.close()

screen = pygame.display.set_mode((300, 550))
pygame.mouse.set_visible(True)
pygame.display.set_caption('D_P')

locations = {'map': Map(),
             'town': Town()}
menu_bar = MenuBar()
book = Book()
blank = Blank()
zn = znShablon()
player = Player(50, 50, load_image('default.png'), 6, 6, 6, get_invent('player_info.data'), )

running = True

while running:
    loca = open('settings/location.data').read()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            menu_bar.update(event.pos)
            if int(open('settings/blank_enabled.data', 'r').read()):
                blank.update(event.pos)
            elif int(open('settings/book_enabled.data', 'r').read()):
                book.update(event.pos)
            elif int(open('settings/zn_enabled.data', 'r').read()):
                zn.update(event.pos)
            else:
                locations[loca].update(event.pos)

    locations[loca].draw()
    screen.blit(locations[loca].include['screen'], (0, 0))
    menu_bar.draw()
    screen.blit(menu_bar.include['screen'], (0, 0))
    book.draw()
    if int(open('settings/book_enabled.data', 'r').read()):
        screen.blit(book.include['screen'], (0, 100))
    blank.draw()
    if int(open('settings/blank_enabled.data', 'r').read()):
        screen.blit(blank.include['screen'], (0, 0))
    zn.draw()
    if int(open('settings/zn_enabled.data', 'r').read()):
        screen.blit(zn.include['screen'], (0, 0))
    pygame.display.flip()

print('Работа завершена...')
terminate()
