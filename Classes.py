import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, image, *groups, **args):
        super().__init__(groups)
        self.image = pygame.transform.scale(image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.w = w
        self.h = h
        self.func = self.nothing
        self.enabled = True

    def connect(self, func):
        self.func = func

    def disconnect(self):
        self.func = self.nothing

    def nothing(self, *args):
        pass

    def update(self, pos, *args):
        if pos[0] in range(self.rect.x, self.rect.x + self.w) and pos[1] in range(self.rect.y, self.rect.y + self.h)\
                and self.enabled:
            self.func(*args)

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y


class Fon(pygame.sprite.Sprite):
    def __init__(self, w, h, image, *groups, **args):
        super().__init__(groups)
        self.image = pygame.transform.scale(image, (w, h))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.y = 0
        if 'x' in args:
            self.rect.x = args['x']
        if 'y' in args:
            self.rect.x = args['y']


class Label:
    def __init__(self, x, y, text, *groups, **args):
        super().__init__()
        self.color = (0, 0, 0, 255)
        if 'color' in args:
            self.color = args['color']
        self.size = 20
        if 'size' in args:
            self.size = args['size']
        self.fat = 1
        if 'fat' in args:
            self.fat = args['fat']
        self.sth = 1
        if 'sth' in args:
            self.sth = args['sth']
        self.text = text
        self.x = x
        self.y = y

    def draw(self, screen):
        font = pygame.font.Font(None, self.size)
        text = self.text.split('\n')
        y = 0
        for string in self.text.split('\n'):
            text = font.render(string, self.fat, self.color)
            screen.blit(text, (self.x, self.y + (self.sth + self.size) * y))
            y += 1

    def set_text(self, text):
        self.text = text

    def set_size(self, size):
        self.size = size

    def set_color(self, color):
        self.color = color

    def set_fat(self, fat):
        self.fat = fat

    def set_sth(self, sth):
        self.sth = sth

    def move(self, x, y):
        self.x = x
        self.y = y


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y,  w, h, image, hp, atk, df, *groups):
        super().__init__(groups)
        self.image = pygame.transform.scale(image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.max_hp = hp
        self.hp = hp
        self.atk = atk
        self.df = df

    def attack(self, target):
        target.hit(self.atk)

    def hit(self, dmg):
        self.hp -= max((dmg - self.df), 1)
        if self.hp < 0:
            self.hp = 0

    def update(self):
        if self.hp == 0:
            self.kill()
            f = open('settings/battle.data', 'w')
            f.write('1')
            f.close()


class Player(pygame.sprite.Sprite):
    def __init__(self, w, h, image, hp, atk, df, invent, *groups):
        super().__init__(groups)
        self.image = pygame.transform.scale(image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = -1000
        self.rect.y = -1000
        self.max_hp = hp
        self.hp = hp
        self.atk = atk
        self.invent = invent
        self.df = df

    def attack(self, target):
        target.hit(self.atk)

    def hit(self, dmg):
        self.hp -= max((dmg - self.df), 1)
        if self.hp < 0:
            self.hp = 0

    def update(self):
        if self.hp == 0:
            self.kill()
            f = open('settings/battle.data', 'w')
            f.write('-1')
            f.close()

    def add_item(self, item):
        self.invent.append(item)

    def del_item(self, item):
        if item in self.invent:
            del self.invent[self.invent.index(item)]

    def get_item(self, n):
        return self.invent[n]

    def move(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, id, *groups):
        super().__init__(groups)
        self.image = pygame.transform.scale(image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.w = w
        self.h = h
        f = list(open('items/' + str(id) + '.data'))
        self.desk = f[-1]
        self.name = f[0]
        self.atk = int(f[1].split(':')[1][:-1])
        self.df = int(f[1].split(':')[2][:-1])
        self.hp = int(f[1].split(':')[3][:-1])

    def use(self, player):
        player.atk += self.atk
        player.df += self.df
        player.hp += self.hp
        player.del_item(self)
        self.kill()
