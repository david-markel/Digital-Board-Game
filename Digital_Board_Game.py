import pygame  # pygame basics
pygame.init()
pygame.mixer.init()
pygame.font.init()

# names of music
Green = 'Green.mp3'
Blue = 'Blue.mp3'
Red = 'Red.mp3'
Yellow = 'Yellow.mp3'
Menu = 'Menu.mp3'

# volume
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.load(Menu)
pygame.mixer.music.play(-1, 0.0)

# volume rectangles
v0 = pygame.Rect(15, 492, 8, 8)
v1 = pygame.Rect(37, 484, 8, 16)
v2 = pygame.Rect(59, 476, 8, 24)
v3 = pygame.Rect(81, 468, 8, 32)
v4 = pygame.Rect(103, 460, 8, 40)


pygame.display.set_caption("Fire Bros")


# variables
win = pygame.display.set_mode((1024, 768))  # dimension of game
game_run = False  # main game  loops
menu_run = True

# images
red = (237, 28, 36)  # these correspond to desired colors
blue = (63, 72, 204)
green = (34, 177, 76)
yellow = (255, 242, 0)

swordR = pygame.image.load('swordR.png')  # swords in menu
swordB = pygame.image.load('swordB.png')
swordG = pygame.image.load('swordG.png')
swordY = pygame.image.load('swordY.png')

redBG = pygame.image.load('Chess Red.png')  # backgrounds
blueBG = pygame.image.load('Chess Blue.png')
greenBG = pygame.image.load('Chess Green.png')
yellowBG = pygame.image.load('Chess Yellow.png')

selector = pygame.image.load('selector.png')  # selection on side
obstacle1 = pygame.image.load('obstacle1.png')  # black box
selected_tile = pygame.image.load('selected_tile.png')  # black square

bg = redBG  # start on redBG

mbg = pygame.image.load('Menu.png')

clock = pygame.time.Clock()  # pygame clock

counter = None  # keeps track of the counter for which turn it is, if it's red's turn then it equals red_turn's counter, counts how many units are on that team

clearing = False  # menu clearing units and tiles

selected_pos = None  # the position that's selected for choosing unitsd

select_rect = pygame.Rect(0, 192, 128, 64)  # button for selecting
selecting = False  # is user selecting
attacking_rect = pygame.Rect(0, 256, 128, 64)  # button for attacking
attacking = False  # is user attacking

plain1vertL = pygame.Rect(0, 0, 64, 191)  # 1 range
plain1horL = pygame.Rect(0, 0, 191, 64)

plain2vertL = pygame.Rect(0, 0, 64, 319)  # 2 range
plain2horL = pygame.Rect(0, 0, 319, 64)
plain2square = pygame.Rect(0, 0, 192, 192)

plain3vertL = pygame.Rect(0, 0, 64, 447)  # 3 range
plain3horL = pygame.Rect(0, 0, 447, 64)
plain3vertR = pygame.Rect(0, 0, 192, 320)
plain3horR = pygame.Rect(0, 0, 320, 192)

plain4vertL = pygame.Rect(0, 0, 64, 575)  # 4 range
plain4horL = pygame.Rect(0, 0, 575, 64)
plain4square = pygame.Rect(0, 0, 319, 319)
plain4vertR = pygame.Rect(0, 0, 191, 447)
plain4horR = pygame.Rect(0, 0, 447, 191)

plain5vertL = pygame.Rect(0, 0, 64, 703)  # 5 range
plain5horL = pygame.Rect(0, 0, 703, 64)
plain5squareVERT = pygame.Rect(0, 0, 319, 447)
plain5squareHOR = pygame.Rect(0, 0, 447, 319)
plain5vertR = pygame.Rect(0, 0, 191, 511)
plain5horR = pygame.Rect(0, 0, 511, 191)

deathbox = pygame.Rect(1025, 0, 0, 0)  # box off screen for when dead

selected_unit = None  # which unit is selected

turn = 0  # current turn?
tBoxX = tBoxX = 896  # turn box coordinates
tBoxY = 576
turn_box = pygame.Rect(tBoxX, tBoxY, 64, 64)

gray_team = pygame.Rect(0, 0, 1024, 51)
stats = pygame.image.load('gray_team.png')


arrowR = pygame.image.load('Arrow Red.png')  # names of arrows
arrowB = pygame.image.load('Arrow Blue.png')
arrowG = pygame.image.load('Arrow Green.png')
arrowY = pygame.image.load('Arrow Yellow.png')

back = False  # flag used to determine when to find a new back_unit
back_cords = None  # current back value
back_tile = None
back_unit = None
back_counter = False
back_horse = None
back_horse_tile = None
back_horse_cords = None
got_horse = False

black = (0, 0, 0)  # color

font = pygame.font.SysFont('Blackadder ITC', 26)  # stats
font1 = pygame.font.SysFont('Castellar', 25)  # stats
font2 = pygame.font.SysFont('Algerian', 30)  # selecting buttons
font3 = pygame.font.SysFont('Algerian', 25)  # smaller font 2
font4 = pygame.font.SysFont('Blackadder ITC', 19)  # stats


name_text = font.render(None, True, black)  # placeholder to initialize
name_rect = pygame.Rect(0, 320, 128, 48)  # location of rectangles

health_text = font.render(None, True, black)
health_rect = pygame.Rect(1, 369, 63, 39)

attack_text = font.render(None, True, black)
attack_rect = pygame.Rect(65, 369, 63, 39)

move_text = font.render(None, True, black)
move_rect = pygame.Rect(1, 409, 63, 39)

range_text = font.render(None, True, black)
range_rect = pygame.Rect(65, 409, 63, 39)

chat1 = font.render(None, True, black)
chat2 = font.render(None, True, black)
chat3 = font.render(None, True, black)

chat1_rect = pygame.Rect(0, 449, 128, 44)
chat2_rect = pygame.Rect(0, 493, 128, 44)
chat3_rect = pygame.Rect(0, 537, 128, 44)

select_text = font2.render('Select', True, black)
attacking_text = font2.render('Attack', True, black)

# sprite animation timer
walkCount = 0

# used when determining if pegasus is using remainder movements
# the_pegasus is the pegasus that needs to use its movement
pegasus_active = False
the_pegasus = None

# start button
start = pygame.Rect(0, 384, 128, 64)

# menu buttons
Msel = False
clearing = False
MselectBox = pygame.Rect(0, 192, 128, 64)
clearBox = pygame.Rect(0, 256, 128, 64)

# how many players, player text
player = 4
player_text = font3.render(str(player) + ' Player', True, black)
player_rect = pygame.Rect(0, 320, 128, 64)

# text for buttons
mselect_text = font3.render('Select', True, black)

clear_text = font2.render('Clear', True, black)

start_text = font2.render('Start', True, black)

# various images used for castles depending on the number of players
red_starter4 = pygame.image.load('red_starter4.png')
blue_starter34 = pygame.image.load('blue_starter34.png')
green_starter4 = pygame.image.load('green_starter4.png')
yellow_starter = pygame.image.load('yellow_starter.png')

red_starter3 = pygame.image.load('red_starter3.png')
green_starter3 = pygame.image.load('green_starter3.png')

red_starter2 = pygame.image.load('red_starter2.png')
blue_starter2 = pygame.image.load('blue_starter2.png')

# which unit just got danced
danced_unit = None

# true if two behind units occupy the same tile
onTOP = False

# base colors used for palette swap
light_base = (200, 191, 231)
dark_base = (163, 73, 164)

# main color bases
light_red = (237, 28, 36)
dark_red = (136, 0, 21)

light_blue = (48, 75, 205)
dark_blue = (22, 35, 97)

light_green = (21, 113, 49)
dark_green = (10, 52, 22)

light_yellow = (255, 242, 83)
dark_yellow = (89, 83, 0)

# castles are located
red_spot4 = pygame.Rect(256, 128, 128, 128)
red_spot3 = pygame.Rect(256, 256, 128, 128)
red_spot2 = pygame.Rect(384, 128, 128, 128)

blue_spot4 = pygame.Rect(640, 128, 128, 128)

green_spot4 = pygame.Rect(640, 512, 128, 128)
green_spot3 = pygame.Rect(512, 512, 128, 128)

# rotating with button
player_list = [4, 2, 3]
# used for scrolling through players
player_count = 0

red_team = []

blue_team = []

green_team = []

yellow_team = []

counter_list = []  # stores each color's counter

tiles_list = []

grays = []

castles_list = []

units_list = []

turn_list = [0, 1, 2, 3]

positions_list = []

# classes


class Counter:

    def __init__(self, team, value):
        self.team = team
        self.value = value

        counter_list.append(self)


red_counter = Counter(0, 0)
blue_counter = Counter(1, 0)
green_counter = Counter(2, 0)
yellow_counter = Counter(3, 0)


class Position:
    def __init__(self, cords, team,  active, player):
        self.rect = pygame.Rect(cords, (64, 64))
        self.cords = cords
        self.team = team
        self.player = player
        self.active = active
        positions_list.append(self)


r1_4 = Position((256, 128), 0, True, 4)
r2_4 = Position((320, 128), 0, True, 4)
r3_4 = Position((384, 128), 0, True, 4)
r4_4 = Position((256, 192), 0, True, 4)
r5_4 = Position((320, 192), 0, True, 4)
r6_4 = Position((384, 192), 0, True, 4)
r7_4 = Position((256, 256), 0, True, 4)
r8_4 = Position((320, 256), 0, True, 4)

b1_4 = Position((576, 128), 1, True, 4)
b2_4 = Position((640, 128), 1, True, 4)
b3_4 = Position((704, 128), 1, True, 4)
b4_4 = Position((576, 192), 1, True, 4)
b5_4 = Position((640, 192), 1, True, 4)
b6_4 = Position((704, 192), 1, True, 4)
b7_4 = Position((640, 256), 1, True, 4)
b8_4 = Position((704, 256), 1, True, 4)

g1_4 = Position((640, 448), 2, True, 4)
g2_4 = Position((704, 448), 2, True, 4)
g3_4 = Position((576, 512), 2, True, 4)
g4_4 = Position((640, 512), 2, True, 4)
g5_4 = Position((704, 512), 2, True, 4)
g6_4 = Position((576, 576), 2, True, 4)
g7_4 = Position((640, 576), 2, True, 4)
g8_4 = Position((704, 576), 2, True, 4)

y1_4 = Position((256, 448), 3, True, 4)
y2_4 = Position((320, 448), 3, True, 4)
y3_4 = Position((256, 512), 3, True, 4)
y4_4 = Position((320, 512), 3, True, 4)
y5_4 = Position((384, 512), 3, True, 4)
y6_4 = Position((256, 576), 3, True, 4)
y7_4 = Position((320, 576), 3, True, 4)
y8_4 = Position((384, 576), 3, True, 4)


r1_3 = Position((256, 192), 0, False, 3)
r2_3 = Position((320, 192), 0, False, 3)
r3_3 = Position((256, 256), 0, False, 3)
r4_3 = Position((320, 256), 0, False, 3)
r5_3 = Position((384, 256), 0, False, 3)
r6_3 = Position((256, 320), 0, False, 3)
r7_3 = Position((320, 320), 0, False, 3)
r8_3 = Position((384, 320), 0, False, 3)
r9_3 = Position((256, 384), 0, False, 3)
r10_3 = Position((320, 384), 0, False, 3)

g1_3 = Position((512, 448), 2, False, 3)
g2_3 = Position((576, 448), 2, False, 3)
g3_3 = Position((448, 512), 2, False, 3)
g4_3 = Position((512, 512), 2, False, 3)
g5_3 = Position((576, 512), 2, False, 3)
g6_3 = Position((640, 512), 2, False, 3)
g7_3 = Position((448, 576), 2, False, 3)
g8_3 = Position((512, 576), 2, False, 3)
g9_3 = Position((576, 576), 2, False, 3)
g10_3 = Position((640, 576), 2, False, 3)


r1_2 = Position((320, 128), 0, False, 2)
r2_2 = Position((384, 128), 0, False, 2)
r3_2 = Position((448, 128), 0, False, 2)
r4_2 = Position((512, 128), 0, False, 2)
r5_2 = Position((320, 192), 0, False, 2)
r6_2 = Position((384, 192), 0, False, 2)
r7_2 = Position((448, 192), 0, False, 2)
r8_2 = Position((512, 192), 0, False, 2)
r9_2 = Position((384, 256), 0, False, 2)
r10_2 = Position((448, 256), 0, False, 2)

b1_2 = Position((512, 448), 1, False, 2)
b2_2 = Position((576, 448), 1, False, 2)
b3_2 = Position((448, 512), 1, False, 2)
b4_2 = Position((512, 512), 1, False, 2)
b5_2 = Position((576, 512), 1, False, 2)
b6_2 = Position((640, 512), 1, False, 2)
b7_2 = Position((448, 576), 1, False, 2)
b8_2 = Position((512, 576), 1, False, 2)
b9_2 = Position((576, 576), 1, False, 2)
b10_2 = Position((640, 576), 1, False, 2)


class Castle:
    def __init__(self, name, team, health, x, y, width, height, isDead, sprite):
        self.team = team
        self.health = health
        self.x = x
        self.y = y
        self.name = name
        self.rect = pygame.Rect(x, y, width, height)
        self.isDead = isDead
        self.sprite = pygame.image.load(sprite)
        castles_list.append(self)

    def showCastle(self):
        if self.isDead == False:
            win.blit(self.sprite, (self.x, self.y))
        elif self.isDead == True:
            win.blit(self.sprite, (1025, 0))

    def DEAD(self):
        if self.health <= 0:
            self.isDead = True

        if self.isDead == True:
            self.rect.clamp_ip(deathbox)


red_castle = Castle('Red Castle', 0, 20, 256, 128, 128, 128, False, 'Castle Red.png')
blue_castle = Castle('Blue Castle', 1, 20, 640, 128, 128, 128, False, 'Castle Blue.png')
green_castle = Castle('Green Castle', 2, 20, 640, 512, 128, 128, False, 'Castle Green.png')
yellow_castle = Castle('Yellow Castle', 3, 20, 256, 512, 128, 128, False, 'Castle Yellow.png')


class Unit:
    #self, name, team, sprite, health, max_health, attack, cords, isDead, rng, move, heal, moved, hasAttacked, code, stopMinus
    def __init__(self, code, team):
        self.code = code
        self.team = team

        if self.team == 0:
            self.letter = 'R'
        elif self.team == 1:
            self.letter = 'B'
        elif self.team == 2:
            self.letter = 'G'
        elif self.team == 3:
            self.letter = 'Y'

        if self.code == 0:
            self.health = 8
            self.attack = 3
            self.move = 2
            self.rng = 2
            self.heal = 0
            self.mounted = False
            self.flyer = False
            self.behind = False
            self.name = 'Soldier'

        elif self.code == 1:
            self.health = 10
            self.attack = 3
            self.move = 1
            self.rng = 1
            self.heal = 0
            self.mounted = False
            self.flyer = False
            self.behind = False
            self.name = 'Knight'

        elif self.code == 2:
            self.health = 7
            self.attack = 3
            self.move = 4
            self.rng = 1
            self.heal = 0
            self.mounted = True
            self.flyer = False
            self.behind = False
            self.name = 'Horseman'

        elif self.code == 3:
            self.health = 10
            self.attack = 2
            self.move = 2
            self.rng = 1
            self.heal = 0
            self.mounted = False
            self.flyer = False
            self.behind = False
            self.name = 'King'

        elif self.code == 4:
            self.health = 8
            self.attack = 2
            self.move = 2
            self.rng = 3
            self.heal = 0
            self.mounted = False
            self.flyer = False
            self.behind = False
            self.name = 'Archer'

        elif self.code == 5:
            self.health = 6
            self.attack = 2
            self.move = 1
            self.rng = 4
            self.heal = 0
            self.mounted = False
            self.flyer = False
            self.behind = False
            self.name = 'Sniper'

        elif self.code == 6:
            self.health = 6
            self.attack = 2
            self.move = 4
            self.rng = 3
            self.heal = 0
            self.mounted = True
            self.flyer = False
            self.behind = False
            self.name = 'Nomad'

        elif self.code == 7:
            self.health = 7
            self.attack = 4
            self.move = 3
            self.rng = 1
            self.heal = 0
            self.mounted = False
            self.flyer = False
            self.behind = False
            self.name = 'Duelist'

        elif self.code == 8:
            self.health = 6
            self.attack = 5
            self.move = 3
            self.rng = 1
            self.heal = 0
            self.mounted = False
            self.flyer = False
            self.behind = False
            self.name = 'Fighter'

        elif self.code == 9:
            self.health = 8
            self.attack = 0
            self.move = 3
            self.rng = 1
            self.heal = 3
            self.mounted = False
            self.flyer = False
            self.behind = False
            self.name = 'Healer'

        elif self.code == 10:
            self.health = 6
            self.attack = 3
            self.move = 2
            self.rng = 2
            self.heal = 1
            self.mounted = False
            self.flyer = False
            self.behind = False
            self.name = 'Wizard'

        elif self.code == 11:
            self.health = 6
            self.attack = 2
            self.move = 2
            self.rng = 2
            self.heal = 2
            self.mounted = False
            self.flyer = False
            self.behind = False
            self.name = 'Sorcerer'

        elif self.code == 12:
            self.health = 6
            self.attack = 3
            self.move = 5
            self.rng = 1
            self.heal = 0
            self.mounted = True
            self.flyer = True
            self.behind = False
            self.name = 'Draco'

        elif self.code == 13:
            self.health = 6
            self.attack = 2
            self.move = 6
            self.rng = 1
            self.heal = 0
            self.mounted = True
            self.flyer = True
            self.behind = False
            self.name = 'Pegasus'

        elif self.code == 14:
            self.health = 8
            self.attack = 2
            self.move = 2
            self.rng = 1
            self.heal = 0
            self.attacked_unit = None
            self.stop = False
            self.mounted = False
            self.flyer = False
            self.behind = False
            self.name = 'Villager'

        elif self.code == 15:
            self.health = 8
            self.attack = 0
            self.move = 3
            self.rng = 1
            self.heal = 0
            self.mounted = False
            self.flyer = False
            self.behind = True
            self.name = 'Guard'

        elif self.code == 16:
            self.health = 4
            self.attack = 0
            self.move = 3
            self.rng = 0
            self.heal = 0
            self.mounted = False
            self.flyer = False
            self.behind = True
            self.name = 'Spirit'

        elif self.code == 17:
            self.health = 4
            self.attack = 0
            self.move = 4
            self.rng = 0
            self.heal = 0
            self.mounted = True
            self.flyer = False
            self.behind = True
            self.name = 'Horse'

        elif self.code == 18:
            self.health = 6
            self.attack = 0
            self.move = 3
            self.rng = 1
            self.heal = 0
            self.mounted = False
            self.flyer = False
            self.behind = False
            self.name = 'Dancer'

        elif self.code == 19:
            self.health = 8
            self.attack = 0
            self.move = 3
            self.rng = 0
            self.heal = 0
            self.mounted = True
            self.flyer = True
            self.behind = False
            self.name = 'Spy'

        self.cords = (1025, 0)
        self.max_health = self.health
        self.rect = pygame.Rect(self.cords, (64, 64))
        self.isDead = False
        self.moved = 0

        self.mHOR = pygame.Rect.copy(plain1horL)
        self.mVERT = pygame.Rect.copy(plain1vertL)
        self.stopMinus = True

        self.horse_move = self.move + 2
        self.HORSE = None
        self.spirited = False

        self.action = False
        self.idle = pygame.image.load(self.name + '.png')
        self.first = pygame.image.load(self.name + ' 1.png')
        self.second = pygame.image.load(self.name + ' 2.png')
        if self.team == 1 or self.team == 2:
            self.idle = pygame.transform.flip(self.idle, True, False)
            self.first = pygame.transform.flip(self.first, True, False)
            self.second = pygame.transform.flip(self.second, True, False)

        self.sprite = [self.idle, self.first, self.second, self.first]

        units_list.append(self)
        if self.team == 0:
            red_team.append(self)

        elif self.team == 1:
            blue_team.append(self)

        elif self.team == 2:
            green_team.append(self)

        elif self.team == 3:
            yellow_team.append(self)

    def showUnit(self):
        if self.isDead == False:
            win.blit(self.idle, (self.cords))

        elif self.isDead == True:
            win.blit(self.idle, (1025, 0))

    def makeRANGE(self):
        if self.rng == 1:
            self.rVERT = pygame.Rect.copy(plain1vertL)
            self.rVERT.clamp_ip(self.rect)
            self.rHOR = pygame.Rect.copy(plain1horL)
            self.rHOR.clamp_ip(self.rect)

        elif self.rng == 2:
            self.rVERT = pygame.Rect.copy(plain2vertL)
            self.rVERT.clamp_ip(self.rect)
            self.rHOR = pygame.Rect.copy(plain2horL)
            self.rHOR.clamp_ip(self.rect)
            self.rSQUARE = pygame.Rect.copy(plain2square)
            self.rSQUARE.clamp_ip(self.rect)

        elif self.rng == 3:
            self.rVERT = pygame.Rect.copy(plain3vertL)
            self.rVERT.clamp_ip(self.rect)
            self.rHOR = pygame.Rect.copy(plain3horL)
            self.rHOR.clamp_ip(self.rect)
            self.rVERTr = pygame.Rect.copy(plain3vertR)
            self.rVERTr.clamp_ip(self.rect)
            self.rHORr = pygame.Rect.copy(plain3horR)
            self.rHORr.clamp_ip(self.rect)

        elif self.rng == 4:
            self.rVERT = pygame.Rect.copy(plain4vertL)
            self.rVERT.clamp_ip(self.rect)
            self.rHOR = pygame.Rect.copy(plain4horL)
            self.rHOR.clamp_ip(self.rect)
            self.rVERTr = pygame.Rect.copy(plain4vertR)
            self.rVERTr.clamp_ip(self.rect)
            self.rHORr = pygame.Rect.copy(plain4horR)
            self.rHORr.clamp_ip(self.rect)
            self.rSQUARE = pygame.Rect.copy(plain4square)
            self.rSQUARE.clamp_ip(self.rect)

    def DEAD(self):
        if self.health <= 0:
            self.isDead = True

        if self.isDead == True:
            self.rect.clamp_ip(deathbox)

    def inRange(self, otherRect):
        if self.rng == 1:
            if self.rVERT.colliderect(otherRect) or self.rHOR.colliderect(otherRect):
                return True
            else:
                return False
        elif self.rng == 2:
            if self.rVERT.colliderect(otherRect) or self.rHOR.colliderect(otherRect) or self.rSQUARE.colliderect(otherRect):
                return True
            else:
                return False
        elif self.rng == 3:
            if self.rVERT.colliderect(otherRect) or self.rHOR.colliderect(otherRect) or self.rVERTr.colliderect(otherRect) or self.rHORr.colliderect(otherRect):
                return True
            else:
                return False
        elif self.rng == 4:
            if self.rVERT.colliderect(otherRect) or self.rHOR.colliderect(otherRect) or self.rSQUARE.colliderect(otherRect) or self.rVERTr.colliderect(otherRect) or self.rHORr.colliderect(otherRect):
                return True
            else:
                return False

    def sameTeam(self, otherUnit):
        if self.team == otherUnit.team:
            return True
        else:
            return False

    def ALLfuncs(self):
        Unit.DEAD(self)
        self.mVERT.clamp_ip(self.rect)
        Unit.makeRANGE(self)
        self.mHOR.clamp_ip(self.rect)


guardR = Unit(15, 0)
spiritR = Unit(16, 0)
horseR = Unit(17, 0)

soldierR = Unit(0, 0)
knightR = Unit(1, 0)
horsemanR = Unit(2, 0)
kingR = Unit(3, 0)
archerR = Unit(4, 0)
sniperR = Unit(5, 0)
nomadR = Unit(6, 0)
duelistR = Unit(7, 0)
fighterR = Unit(8, 0)
healerR = Unit(9, 0)
wizardR = Unit(10, 0)
sorcererR = Unit(11, 0)
dracoR = Unit(12, 0)
pegasusR = Unit(13, 0)
villagerR = Unit(14, 0)
dancerR = Unit(18, 0)
spyR = Unit(19, 0)


guardB = Unit(15, 1)
spiritB = Unit(16, 1)
horseB = Unit(17, 1)

soldierB = Unit(0, 1)
knightB = Unit(1, 1)
horsemanB = Unit(2, 1)
kingB = Unit(3, 1)
archerB = Unit(4, 1)
sniperB = Unit(5, 1)
nomadB = Unit(6, 1)
duelistB = Unit(7, 1)
fighterB = Unit(8, 1)
healerB = Unit(9, 1)
wizardB = Unit(10, 1)
sorcererB = Unit(11, 1)
dracoB = Unit(12, 1)
pegasusB = Unit(13, 1)
villagerB = Unit(14, 1)
dancerB = Unit(18, 1)
spyG = Unit(19, 1)


guardG = Unit(15, 2)
spiritG = Unit(16, 2)
horseG = Unit(17, 2)

soldierG = Unit(0, 2)
knightG = Unit(1, 2)
horsemanG = Unit(2, 2)
kingG = Unit(3, 2)
archerG = Unit(4, 2)
sniperG = Unit(5, 2)
nomadG = Unit(6, 2)
duelistG = Unit(7, 2)
fighterG = Unit(8, 2)
healerG = Unit(9, 2)
wizardG = Unit(10, 2)
sorcererG = Unit(11, 2)
dracoG = Unit(12, 2)
pegasusG = Unit(13, 2)
villagerG = Unit(14, 2)
dancerG = Unit(18, 2)
spyG = Unit(19, 2)

guardY = Unit(15, 3)
spiritY = Unit(16, 3)
horseY = Unit(17, 3)

soldierY = Unit(0, 3)
knightY = Unit(1, 3)
horsemanY = Unit(2, 3)
kingY = Unit(3, 3)
archerY = Unit(4, 3)
sniperY = Unit(5, 3)
nomadY = Unit(6, 3)
duelistY = Unit(7, 3)
fighterY = Unit(8, 3)
healerY = Unit(9, 3)
wizardY = Unit(10, 3)
sorcererY = Unit(11, 3)
dracoY = Unit(12, 3)
pegasusY = Unit(13, 3)
villagerY = Unit(14, 3)
dancerY = Unit(18, 3)
spyY = Unit(19, 3)


pxarray = None

for unit in units_list:
    for i in unit.sprite:

        pxarray = pygame.PixelArray(i)
        if unit.team == 0:

            pxarray.replace(light_base, light_red)
            pxarray.replace(dark_base, dark_red)

        elif unit.team == 1:

            pxarray.replace(light_base, light_blue)
            pxarray.replace(dark_base, dark_blue)

        elif unit.team == 2:

            pxarray.replace(light_base, light_green)
            pxarray.replace(dark_base, dark_green)

        elif unit.team == 3:
            pxarray.replace(light_base, light_yellow)
            pxarray.replace(dark_base, dark_yellow)

        pygame.PixelArray.close(pxarray)


warriorR = pygame.image.load('warrior.png')
warriorB = pygame.image.load('warrior.png')
warriorG = pygame.image.load('warrior.png')
warriorY = pygame.image.load('warrior.png')

pxarray = pygame.PixelArray(warriorR)
pxarray.replace(light_base, light_red)
pxarray.replace(dark_base, dark_red)
pygame.PixelArray.close(pxarray)

pxarray = pygame.PixelArray(warriorB)
pxarray.replace(light_base, light_blue)
pxarray.replace(dark_base, dark_blue)
pygame.PixelArray.close(pxarray)

pxarray = pygame.PixelArray(warriorG)
pxarray.replace(light_base, light_green)
pxarray.replace(dark_base, dark_green)
pygame.PixelArray.close(pxarray)

pxarray = pygame.PixelArray(warriorY)
pxarray.replace(light_base, light_yellow)
pxarray.replace(dark_base, dark_yellow)
pygame.PixelArray.close(pxarray)


spirit_list = [spiritR, spiritB, spiritG, spiritY]
pegasus_list = [pegasusR, pegasusB, pegasusG, pegasusY]


class Tile:

    def __init__(self, name, tx, ty):
        self.name = name
        self.rect = pygame.Rect(tx, ty, 64, 64)
        self.tx = tx
        self.ty = ty
        self.occupy = 0
        self.starter = False
        tiles_list.append(self)


a1 = Tile('a1', 256, 576)
a2 = Tile('a2', 256, 512)
a3 = Tile('a3', 256, 448)
a4 = Tile('a4', 256, 384)
a5 = Tile('a5', 256, 320)
a6 = Tile('a6', 256, 256)
a7 = Tile('a7', 256, 192)
a8 = Tile('a8', 256, 128)

b1 = Tile('b1', 320, 576)
b2 = Tile('b2', 320, 512)
b3 = Tile('b3', 320, 448)
b4 = Tile('b4', 320, 384)
b5 = Tile('b5', 320, 320)
b6 = Tile('b6', 320, 256)
b7 = Tile('b7', 320, 192)
b8 = Tile('b8', 320, 128)

c1 = Tile('c1', 384, 576)
c2 = Tile('c2', 384, 512)
c3 = Tile('c3', 384, 448)
c4 = Tile('c4', 384, 384)
c5 = Tile('c5', 384, 320)
c6 = Tile('c6', 384, 256)
c7 = Tile('c7', 384, 192)
c8 = Tile('c8', 384, 128)

d1 = Tile('d1', 448, 576)
d2 = Tile('d2', 448, 512)
d3 = Tile('d3', 448, 448)
d4 = Tile('d4', 448, 384)
d5 = Tile('d5', 448, 320)
d6 = Tile('d6', 448, 256)
d7 = Tile('d7', 448, 192)
d8 = Tile('d8', 448, 128)

e1 = Tile('e1', 512, 576)
e2 = Tile('e2', 512, 512)
e3 = Tile('e3', 512, 448)
e4 = Tile('e4', 512, 384)
e5 = Tile('e5', 512, 320)
e6 = Tile('e6', 512, 256)
e7 = Tile('e7', 512, 192)
e8 = Tile('e8', 512, 128)

f1 = Tile('f1', 576, 576)
f2 = Tile('f2', 576, 512)
f3 = Tile('f3', 576, 448)
f4 = Tile('f4', 576, 384)
f5 = Tile('f5', 576, 320)
f6 = Tile('f6', 576, 256)
f7 = Tile('f7', 576, 192)
f8 = Tile('f8', 576, 128)

g1 = Tile('g1', 640, 576)
g2 = Tile('g2', 640, 512)
g3 = Tile('g3', 640, 448)
g4 = Tile('g4', 640, 384)
g5 = Tile('g5', 640, 320)
g6 = Tile('g6', 640, 256)
g7 = Tile('g7', 640, 192)
g8 = Tile('g8', 640, 128)

h1 = Tile('h1', 704, 576)
h2 = Tile('h2', 704, 512)
h3 = Tile('h3', 704, 448)
h4 = Tile('h4', 704, 384)
h5 = Tile('h5', 704, 320)
h6 = Tile('h6', 704, 256)
h7 = Tile('h7', 704, 192)
h8 = Tile('h8', 704, 128)


class Gray:
    def __init__(self, num):
        self.num = num
        self.rect = pygame.Rect(num*50+23, 0, 50, 50)
        grays.append(self)


soldier = Gray(0)
knight = Gray(1)
horseman = Gray(2)
king = Gray(3)
archer = Gray(4)
sniper = Gray(5)
nomad = Gray(6)
duelist = Gray(7)
fighter = Gray(8)
healer = Gray(9)
wizard = Gray(10)
sorcerer = Gray(11)
draco = Gray(12)
pegasus = Gray(13)
villager = Gray(14)
guard = Gray(15)
spirit = Gray(16)
horse = Gray(17)
dancer = Gray(18)
spy = Gray(19)


class Phase:

    def __init__(self):
        self.action_counter = 0
        self.turn_count = 0
        self.new_turn = False
        self.pegasus_active = False

    def resetPHASE(self):
        self.action_counter = 0
        self.turn_count += 1
        self.new_turn = False
        self.pegasus_active = False


phase = Phase()

# functions


def Mode(rect):

    if onTOP != True:
        if rect.collidepoint(pos) and pressed1:

            return True


def subMOVE(unit, tile):

    unit.rect.clamp_ip(tile.rect)
    unit.cords = (tile.tx, tile.ty)
    unit.moved += 1


def MOVE(unit, tile, phase):

    if unit.action == False or unit.code == 13:
        if unit.HORSE == None or unit.behind == True:
            if unit.moved < unit.move:
                if tile.occupy == 4:
                    subMOVE(unit, tile)

                elif tile.occupy == unit.team:

                    if unit.code != 13:
                        subMOVE(unit, tile)

                    elif unit.code == 13:
                        if tile.occupy == 4:
                            subMOVE(unit, tile)

                        elif tile.occupy == unit.team:
                            if unit.moved != unit.move - 1:
                                subMOVE(unit, tile)

                            else:
                                for castle in castles_list:
                                    if tile.rect.colliderect(castle.rect) and tile.guy == None or tile.guy != None and tile.guy.behind == True:
                                        subMOVE(unit, tile)

                elif tile.occupy == 5:
                    if unit.flyer == True:
                        if tile.guy == None or tile.guy.team == unit.team:
                            if unit.code != 13:
                                subMOVE(unit, tile)

                            elif unit.code == 13:
                                if tile.guy == None:
                                    subMOVE(unit, tile)

                                elif tile.guy != None:
                                    if unit.moved != unit.move - 1:
                                        subMOVE(unit, tile)

                                else:
                                    print('occupied, dude')

                        else:
                            print('occupied, dude')

        elif unit.HORSE != None and unit.behind == False:
            if unit.moved < unit.horse_move:
                if tile.occupy == 4 or tile.occupy == unit.team:
                    subMOVE(unit, tile)

                    unit.HORSE.rect.clamp_ip(tile.rect)
                    unit.HORSE.cords = (tile.tx, tile.ty)


def isTURN():
    if selected_unit != None:
        if selected_unit.team == turn:
            return True


def resetTURN():
    for unit in units_list:
        unit.moved = 0
        unit.action = False


def redrawGameWindow():
    global walkCount

    if arrow == 0:
        bg.blit(arrowR, (tBoxX, tBoxY))
    elif arrow == 1:
        bg.blit(arrowB, (tBoxX, tBoxY))
    elif arrow == 2:
        bg.blit(arrowG, (tBoxX, tBoxY))
    elif arrow == 3:
        bg.blit(arrowY, (tBoxX, tBoxY))

    win.blit(bg, (0, 0))

    for tile in tiles_list:
        if tile.occupy == 5:
            win.blit(obstacle1, (tile.tx, tile.ty))

    for castle in castles_list:
        Castle.showCastle(castle)

    if back_tile != None:
        if isTURN():
            if selected_unit.action == False:
                if back_unit == selected_unit:
                    win.blit(selected_tile, back_cords)

    if walkCount + 1 >= 20:
        walkCount = 0

    for unit in units_list:
        if unit.isDead == False:
            if turn == unit.team and unit.isDead == False and unit.action == False and unit.sprite != None:
                win.blit(unit.sprite[walkCount//5], unit.cords)

            else:
                win.blit(unit.idle, unit.cords)

    walkCount += 1

    if selecting == True:
        win.blit(selector, (0, 191))

    if attacking == True:
        win.blit(selector, (0, 255))

    if gray_team.collidepoint(pos):
        win.blit(stats, (0, 0))

    win.blit(select_text, (select_rect.width//2 - select_text.get_width() //
             2, select_rect.height//2 - select_text.get_height()//2 + 192))

    win.blit(attacking_text, (attacking_rect.width//2 - attacking_text.get_width() //
             2, attacking_rect.height//2 - attacking_text.get_height()//2 + 256))

    win.blit(name_text, (name_rect.width//2 - name_text.get_width() //
             2, name_rect.height//2 - name_text.get_height()//2 + 320))

    win.blit(health_text, (health_rect.width//2 - health_text.get_width() //
             2 + 1, health_rect.height//2 - health_text.get_height()//2 + 369))

    win.blit(attack_text, (attack_rect.width//2 - attack_text.get_width() //
             2 + 65, attack_rect.height//2 - attack_text.get_height()//2 + 369))

    win.blit(move_text, (move_rect.width//2 - move_text.get_width()//2 +
             1, move_rect.height//2 - move_text.get_height()//2 + 409))

    win.blit(range_text, (range_rect.width//2 - range_text.get_width()//2 +
             65, range_rect.height//2 - range_text.get_height()//2 + 409))

    win.blit(chat1, (chat1_rect.width//2 - chat1.get_width()//2,
             chat1_rect.height//2 - chat1.get_height()//2 + 449))
    win.blit(chat2, (chat2_rect.width//2 - chat2.get_width()//2,
             chat2_rect.height//2 - chat2.get_height()//2 + 493))
    win.blit(chat3, (chat3_rect.width//2 - chat3.get_width()//2,
             chat3_rect.height//2 - chat3.get_height()//2 + 537))

    pygame.display.update()


def startTILES(s_list):

    for tile in tiles_list:
        if tile in s_list:
            tile.starter = True
        else:
            tile.starter = False


def menuRedraw(arrow):
    global walkCount

    win.blit(mbg, (0, 0))

    win.blit(arrow, (tBoxX, tBoxY))

    player_text = font3.render(str(player) + ' Player', True, black)

    win.blit(player_text, (player_rect.width//2 - player_text.get_width() //
             2, player_rect.height//2 - player_text.get_height()//2 + 320))

    win.blit(select_text, (select_rect.width//2 - select_text.get_width() //
             2, select_rect.height//2 - select_text.get_height()//2 + 192))

    win.blit(clear_text, (clearBox.width//2 - clear_text.get_width() //
             2, clearBox.height//2 - clear_text.get_height()//2 + 256))

    win.blit(start_text, (start.width//2 - start_text.get_width() //
             2, start.height//2 - start_text.get_height()//2 + 384))

    if Msel == True:
        win.blit(selector, (0, 191))
    if clearing == True:
        win.blit(selector, (0, 255))

    if player == 4:
        win.blit(red_starter4, (256, 128))
        win.blit(blue_starter34, (576, 128))
        win.blit(green_starter4, (576, 448))
        win.blit(yellow_starter, (256, 448))

        if turn == 0:
            win.blit(sword, (192, 128))
        elif turn == 1:
            win.blit(sword, (768, 128))
        elif turn == 2:
            win.blit(sword, (768, 576))
        elif turn == 3:
            win.blit(sword, (192, 576))

    elif player == 3:
        win.blit(red_starter3, (256, 192))
        win.blit(blue_starter34, (576, 128))
        win.blit(green_starter3, (448, 448))

        if turn == 0:
            win.blit(sword, (192, 256))
        elif turn == 1:
            win.blit(sword, (768, 128))
        elif turn == 2:
            win.blit(sword, (768, 576))

    elif player == 2:
        win.blit(red_starter2, (320, 128))
        win.blit(blue_starter2, (448, 448))

        if turn == 0:
            win.blit(sword, (192, 128))
        elif turn == 1:
            win.blit(sword, (768, 576))

    if walkCount + 1 >= 16:
        walkCount = 0

    for unit in units_list:
        if turn == unit.team:
            if unit.isDead == False and unit.action == False and unit.sprite != None:
                win.blit(unit.sprite[walkCount//4], unit.cords)

            else:
                win.blit(unit.idle, unit.cords)

    walkCount += 1

    if selected_pos != None:
        win.blit(selected_tile, selected_pos.cords)

    for tile in tiles_list:
        if tile.occupy == 5:
            win.blit(obstacle1, (tile.tx, tile.ty))

    pygame.display.update()


def resetUNITS():

    for unit in units_list:
        unit.cords = (1025, 0)
        unit.rect.clamp_ip(deathbox)
        red_counter.value = 0
        blue_counter.value = 0
        green_counter.value = 0
        yellow_counter.value = 0


while menu_run == True:
    clock.tick(30)
    keys = pygame.key.get_pressed()
    pos = pygame.mouse.get_pos()

    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()

    for position in positions_list:
        if player == 4:

            green_castle.isDead = False
            yellow_castle.isDead = False

            red_castle.x = 256
            red_castle.y = 128
            red_castle.rect.clamp_ip(red_spot4)

            blue_castle.x = 640
            blue_castle.y = 128
            blue_castle.rect.clamp_ip(blue_spot4)

            green_castle.x = 640
            green_castle.y = 512
            green_castle.rect.clamp_ip(green_spot4)

            startTILES([a8, b8, c8, f8, g8, h8, a7, b7, c7, f7, g7, h7, a6, b6, g6, h6,
                       a3, b3, g3, h3, a2, b2, c2, f2, g2, h2, a1, b1, c1, f1, g1, h1])

            if position.player == 4:
                position.active = True
            else:
                position.active = False

        elif player == 3:

            green_castle.isDead = False
            yellow_castle.isDead = True

            red_castle.x = 256
            red_castle.y = 256
            red_castle.rect.clamp_ip(red_spot3)

            blue_castle.x = 640
            blue_castle.y = 128
            blue_castle.rect.clamp_ip(blue_spot4)

            green_castle.x = 512
            green_castle.y = 512
            green_castle.rect.clamp_ip(green_spot3)

            startTILES([f8, g8, h8, a7, b7, f7, g7, h7, a6, b6, c6, g6, h6, a5,
                       b5, c5, a4, b4, e3, f3, d2, e2, f2, g2, d1, e1, f1, g1])

            if position.player == 3 or position.team == 1 and position.player == 4:
                position.active = True
            else:
                position.active = False

        elif player == 2:

            green_castle.isDead = True
            yellow_castle.isDead = True

            red_castle.x = 384
            red_castle.y = 128
            red_castle.rect.clamp_ip(red_spot2)

            blue_castle.x = 512
            blue_castle.y = 512
            blue_castle.rect.clamp_ip(green_spot3)

            startTILES([b8, c8, d8, e8, b7, c7, d7, e7, c6, d6,
                       e3, f3, d2, e2, f2, g2, d1, e1, f1, g1])

            if position.player == 2:
                position.active = True
            else:
                position.active = False

    if MselectBox.collidepoint(pos) and pressed1:
        Msel = True
        clearing = False
    if clearBox.collidepoint(pos) and pressed1:
        clearing = True
        Msel = False

    for position in positions_list:
        if position.rect.collidepoint(pos) and pressed1:
            if position.active == True:
                if turn == position.team:
                    selected_pos = position

    if turn == 0:
        counter = red_counter.value
    elif turn == 1:
        counter = blue_counter.value
    elif turn == 2:
        counter = green_counter.value
    elif turn == 3:
        counter = yellow_counter.value

    if Msel == True:
        for tile in tiles_list:
            if tile.starter == False:
                if tile.rect.collidepoint(pos) and pressed1:
                    tile.occupy = 5
        if selected_pos != None:
            for unit in units_list:
                for gray in grays:
                    if unit.team == selected_pos.team:
                        if gray.rect.collidepoint(pos) and pressed1:
                            if gray.num == unit.code:
                                if counter < 6:
                                    if unit.cords == (1025, 0):
                                        if turn == 0:
                                            red_counter.value += 1
                                        elif turn == 1:
                                            blue_counter.value += 1
                                        elif turn == 2:
                                            green_counter.value += 1
                                        elif turn == 3:
                                            yellow_counter.value += 1
                                    unit.cords = selected_pos.cords
                                    unit.rect.clamp_ip(selected_pos.rect)
                                    for ham in units_list:
                                        if ham != unit:
                                            if ham.rect.colliderect(selected_pos):
                                                ham.cords = (1025, 0)
                                                ham.rect.clamp_ip(deathbox)
                                                if turn == 0:
                                                    red_counter.value -= 1
                                                elif turn == 1:
                                                    blue_counter.value -= 1
                                                elif turn == 2:
                                                    green_counter.value -= 1
                                                elif turn == 3:
                                                    yellow_counter.value -= 1
                                elif counter >= 6:
                                    print('You have six! Clear to make room')

    if clearing == True:
        for tile in tiles_list:
            if tile.starter == False:
                if tile.rect.collidepoint(pos) and pressed1:
                    tile.occupy = 0
        for unit in units_list:
            if unit.team == turn:
                if unit.rect.collidepoint(pos) and pressed1:
                    unit.cords = (1025, 0)
                    unit.rect.clamp_ip(deathbox)
                    if turn == 0:
                        red_counter.value -= 1
                    elif turn == 1:
                        blue_counter.value -= 1
                    elif turn == 2:
                        green_counter.value -= 1
                    elif turn == 3:
                        yellow_counter.value -= 1

    if start.collidepoint(pos) and pressed1:
        menu_run = False
        game_run = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu_run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if player_rect.collidepoint(pos):
                    for tile in tiles_list:
                        player = player_list[player_count]
                        if player_count == 2:
                            player_count = 0
                        else:
                            player_count += 1
                        resetUNITS()
                        selected_pos = None
                        tile.occupy = 0

                if player == 4:
                    if turn == 0 and turn_box.collidepoint(pos):
                        turn = 1
                        selected_pos = None
                    elif turn == 1 and turn_box.collidepoint(pos):
                        turn = 2
                        selected_pos = None
                    elif turn == 2 and turn_box.collidepoint(pos):
                        turn = 3
                        selected_pos = None
                    elif turn == 3 and turn_box.collidepoint(pos):
                        turn = 0
                        selected_pos = None

                elif player == 3:
                    if turn == 0 and turn_box.collidepoint(pos):
                        turn = 1
                        selected_pos = None
                    elif turn == 1 and turn_box.collidepoint(pos):
                        turn = 2
                        selected_pos = None
                    elif turn == 2 and turn_box.collidepoint(pos):
                        turn = 0
                        selected_pos = None

                elif player == 2:
                    if turn == 0 and turn_box.collidepoint(pos):
                        turn = 1
                        selected_pos = None
                    elif turn == 1 and turn_box.collidepoint(pos):
                        turn = 0
                        selected_pos = None

    if turn == 0:
        sword = swordR
    elif turn == 1:
        sword = swordB
    elif turn == 2:
        sword = swordG
    elif turn == 3:
        sword = swordY

    if player == 4:
        if turn == 0:
            arrow = arrowB
        elif turn == 1:
            arrow = arrowG
        elif turn == 2:
            arrow = arrowY
        elif turn == 3:
            arrow = arrowR

    elif player == 3:
        if turn == 0:
            arrow = arrowB
        if turn == 1:
            arrow = arrowG
        if turn == 2:
            arrow = arrowR

    elif player == 2:
        if turn == 0:
            arrow = arrowB
        if turn == 1:
            arrow = arrowR
        if turn == 2 or turn == 3:
            turn = 0
            arrow = arrowB

    if v0.collidepoint(pos) and pressed1:
        pygame.mixer.music.set_volume(0.00)
    if v1.collidepoint(pos) and pressed1:
        pygame.mixer.music.set_volume(0.10)
    if v2.collidepoint(pos) and pressed1:
        pygame.mixer.music.set_volume(0.30)
    if v3.collidepoint(pos) and pressed1:
        pygame.mixer.music.set_volume(0.65)
    if v4.collidepoint(pos) and pressed1:
        pygame.mixer.music.set_volume(1.0)

    menuRedraw(arrow)

while game_run:

    pos = pygame.mouse.get_pos()

    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()

    keys = pygame.key.get_pressed()

    clock.tick(30)

    if phase.turn_count >= len(turn_list):
        phase.turn_count = 0

    turn = turn_list[phase.turn_count]

    if phase.turn_count + 1 < len(turn_list):
        arrow = turn_list[phase.turn_count + 1]

    elif phase.turn_count + 1 >= len(turn_list):
        arrow = turn_list[0]

    for counter in counter_list:
        if counter.value == 0:
            for i in turn_list:
                if i == counter.team:
                    turn_list.remove(i)

    if phase.new_turn == False:
        if turn == 0:
            pygame.mixer.music.load(Red)
        elif turn == 1:
            pygame.mixer.music.load(Blue)
        elif turn == 2:
            pygame.mixer.music.load(Green)
        elif turn == 3:
            pygame.mixer.music.load(Yellow)

        pygame.mixer.music.play(-1, 0.0)

        phase.new_turn = True

    if selected_unit != None:
        name_text = font.render(
            str(selected_unit.name + selected_unit.letter + '.'), True, (0, 0, 0), True)

        health_text = font1.render("H: " + str(selected_unit.health), True, (0, 0, 0), True)

        attack_text = font1.render("A: " + str(selected_unit.attack), True, (0, 0, 0), True)

        move_text = font1.render("M: " + str(selected_unit.move), True, (0, 0, 0), True)

        range_text = font1.render("R: " + str(selected_unit.rng), True, (0, 0, 0), True)

    if keys[pygame.K_1]:
        selecting = True
        attacking = False
    elif keys[pygame.K_2]:
        attacking = True
        selecting = False

    # all back stuff
    if selected_unit != None:
        if back == False:
            back_cords = selected_unit.cords

            back = True
            back_unit = selected_unit
            back_counter = phase.action_counter

            back_horse = selected_unit.HORSE

            for tile in tiles_list:
                if tile.rect.colliderect(selected_unit.rect):
                    back_tile = tile

                if back_horse != None:
                    if tile.rect.colliderect(back_horse.rect):
                        back_horse_tile = tile
                        back_horse_cords = selected_unit.cords

    if back_unit != selected_unit:
        back = False

        if back_unit.moved != 0:
            if back_unit.action == False or back_unit is the_pegasus:
                phase.action_counter += 1

                back_unit.action = True

        for pegasus in pegasus_list:
            if pegasus is selected_unit:
                if phase.action_counter == 2 and pegasus.action == False:
                    phase.pegasus_active = True
                    the_pegasus = pegasus

    # determines whether to end turn or not based on pegasus

    if phase.pegasus_active == False:
        if phase.action_counter == 3:
            if onTOP != True:
                resetTURN()
                phase.resetPHASE()

    elif phase.pegasus_active == True:
        if the_pegasus.moved >= the_pegasus.move and the_pegasus.action == True or phase.action_counter >= 4:
            if onTOP != True:
                resetTURN()
                phase.resetPHASE()

    if keys[pygame.K_q]:
        if back_unit != None:
            if back_unit.team == turn:
                if back_unit.action == False:
                    print('q')
                    back_unit.rect.clamp_ip(back_tile)
                    back_unit.cords = back_cords
                    back_unit.moved = 0
                    phase.action_counter = back_counter

                    if back_horse != None and back_unit.behind == False:
                        back_horse.rect.clamp_ip(back_horse_tile)
                        back_horse.cords = back_horse_cords

    # when the selected unit picks up the horse, that's when it marks the cords and tile
    if selected_unit != None:
        if back_horse == None and selected_unit.HORSE != None:
            back_horse = selected_unit.HORSE
            back_horse_cords = selected_unit.cords
            for tile in tiles_list:
                if selected_unit.rect.colliderect(tile.rect):
                    back_horse_tile = tile

    for unit in units_list:
        for ham in units_list:
            if ham.code == 17:
                if onTOP == False:
                    if unit.rect.colliderect(ham.rect) and unit.mounted == False:
                        unit.HORSE = ham

                        break
                    else:
                        unit.HORSE = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
        elif event.type == pygame.KEYDOWN:

            if selected_unit != None:
                if isTURN():
                    if phase.action_counter < 3 or selected_unit == danced_unit or phase.pegasus_active == True and selected_unit == the_pegasus:
                        for tile in tiles_list:
                            if event.key == pygame.K_s:
                                if selected_unit.cords[0] == tile.tx and selected_unit.cords[1] + 64 == tile.ty:
                                    MOVE(selected_unit, tile, phase)
                                    break

                            elif event.key == pygame.K_w:
                                if selected_unit.cords[0] == tile.tx and selected_unit.cords[1] - 64 == tile.ty:
                                    MOVE(selected_unit, tile, phase)
                                    break

                            elif event.key == pygame.K_a:
                                if selected_unit.cords[0] - 64 == tile.tx and selected_unit.cords[1] == tile.ty:
                                    MOVE(selected_unit, tile, phase)
                                    break

                            elif event.key == pygame.K_d:
                                if selected_unit.cords[0] + 64 == tile.tx and selected_unit.cords[1] == tile.ty:
                                    MOVE(selected_unit, tile, phase)
                                    break
                    else:
                        print('not key')

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if onTOP != True:
                    if turn_box.collidepoint(pos):
                        resetTURN()
                        phase.resetPHASE()

                    if attacking == True and selected_unit != None:
                        if selected_unit.code == 19 and isTURN() and selected_unit.action == False:
                            for tile in tiles_list:
                                if tile.rect.colliderect(selected_unit.rect) and tile.rect.collidepoint(pos):
                                    if tile.occupy == selected_unit.team:
                                        tile.occupy = 5
                                        phase.action_counter += 1
                                        selected_unit.action = True

                                        print(tile.occupy)
                                    elif tile.occupy == 5:
                                        tile.occupy = 4
                                        phase.action_counter += 1
                                        selected_unit.action = True

                                        print(tile.occupy)
                        for unit in units_list:
                            if unit == selected_unit:
                                continue
                            elif not Unit.sameTeam(selected_unit, unit) and isTURN() and selected_unit.action == False:
                                if unit.behind == True:
                                    continue
                                elif unit.rect.collidepoint(pos) and selected_unit.inRange(unit.rect):

                                    if not selected_unit.spirited:
                                        unit.health -= selected_unit.attack

                                    elif selected_unit.spirited:
                                        unit.health -= selected_unit.attack + 2

                                    print(unit.health)

                                    phase.action_counter += 1

                                    selected_unit.action = True

                                    if selected_unit.code == 14:
                                        selected_unit.attacked_unit = unit

                                    # chat log
                                    chat3 = chat2

                                    chat2 = chat1

                                    if not selected_unit.spirited:
                                        chat1 = font4.render(
                                            str(unit.name) + str(unit.letter) + '. -' + str(selected_unit.attack), True, black)

                                    elif selected_unit.spirited:
                                        chat1 = font4.render(
                                            str(unit.name) + str(unit.letter) + '. -' + str(selected_unit.attack + 2), True, black)

                            elif Unit.sameTeam(selected_unit, unit) and isTURN() and selected_unit.action == False:
                                if unit.rect.collidepoint(pos) and selected_unit.inRange(unit.rect):
                                    if selected_unit.code == 18:
                                        if unit.behind == False:
                                            unit.action = False
                                            unit.moved = 0
                                            selected_unit.action = True
                                            danced_unit = unit

                                            # chat log
                                            chat3 = chat2

                                            chat2 = chat1

                                            chat1 = font4.render(
                                                str(unit.name) + str(unit.letter) + '. Da', True, black)

                                    if selected_unit.heal > 0:
                                        if unit.behind == False:
                                            if unit.health + selected_unit.heal <= unit.max_health:
                                                unit.health += selected_unit.heal
                                                print(unit.health)
                                                phase.action_counter += 1
                                                selected_unit.action = True

                                                chat3 = chat2

                                                chat2 = chat1

                                                chat1 = font4.render(
                                                    str(unit.name) + str(unit.letter) + '. +' + str(selected_unit.heal), True, black)

                                            elif unit.health + selected_unit.heal > unit.max_health:
                                                unit.health = unit.max_health
                                                print(unit.health)
                                                phase.action_counter += 1
                                                selected_unit.action = True

                                                chat3 = chat2

                                                chat2 = chat1

                                                chat1 = font4.render(
                                                    str(unit.name) + str(unit.letter) + '. +' + str(unit.max_health - unit.health), True, black)

                    elif selecting == True:
                        pass

            elif event.button == 3:
                if selecting == True:
                    for castle in castles_list:
                        if castle.rect.collidepoint(pos) and keys[pygame.K_LSHIFT]:
                            name_text = font.render(castle.name, True, black, True)

                            health_text = font1.render(
                                "H: " + str(castle.health), True, (0, 0, 0), True)

                            attack_text = font1.render("A: 0", True, black, True)

                            move_text = font1.render("M: 0", True, black, True)

                            range_text = font1.render("R: 0", True, black, True)

                            selected_unit = None

                for unit in units_list:
                    if unit.behind == True:
                        if selecting == True and unit.rect.collidepoint(pos) and onTOP == False:
                            selected_unit = unit

                    if attacking == True:
                        if not Unit.sameTeam(selected_unit, unit) and isTURN() and selected_unit.action == False:
                            if unit.behind == True:
                                if unit.rect.collidepoint(pos) and selected_unit.inRange(unit.rect):

                                    if not selected_unit.spirited:
                                        unit.health -= selected_unit.attack

                                    elif selected_unit.spirited:
                                        unit.health -= selected_unit.attack + 2

                                    print(unit.health)

                                    # chat log
                                    chat3 = chat2

                                    chat2 = chat1

                                    if not selected_unit.spirited:
                                        chat1 = font4.render(
                                            str(unit.name) + str(unit.letter) + '. -' + str(selected_unit.attack), True, black)

                                    elif selected_unit.spirited:
                                        chat1 = font4.render(
                                            str(unit.name) + str(unit.letter) + '. -' + str(selected_unit.attack + 2), True, black)

                                    phase.action_counter += 1
                                    selected_unit.action = True
                                    if selected_unit.code == 14:
                                        selected_unit.attacked_unit = unit

                        elif Unit.sameTeam(selected_unit, unit) and isTURN() and selected_unit.action == False:
                            if unit.rect.collidepoint(pos) and selected_unit.inRange(unit.rect):
                                if selected_unit.code == 18:
                                    if unit.behind == True:
                                        unit.action = False
                                        unit.moved = 0
                                        selected_unit.action = True
                                        danced_unit = unit

                                elif selected_unit.heal > 0:
                                    if unit.behind == True:
                                        if unit.health + selected_unit.heal <= unit.max_health:
                                            unit.health += selected_unit.heal

                                            print(unit.health)
                                            phase.action_counter += 1
                                            selected_unit.action = True

                                            chat3 = chat2

                                            chat2 = chat1

                                            chat1 = font4.render(
                                                str(unit.name) + str(unit.letter) + '. +' + str(selected_unit.heal), True, black)

                                        elif unit.health + selected_unit.heal > unit.max_health:
                                            unit.health = unit.max_health
                                            print(unit.health)
                                            phase.action_counter += 1
                                            selected_unit.action = True

                                            chat3 = chat2

                                            chat2 = chat1

                                            chat1 = font4.render(
                                                str(unit.name) + str(unit.letter) + '. +' + str(unit.max_health - unit.health), True, black)

                        for castle in castles_list:
                            if selected_unit != None:
                                if selected_unit.team != castle.team:
                                    if isTURN():
                                        if castle.rect.collidepoint(pos) and keys[pygame.K_LSHIFT]:
                                            if selected_unit.action == False:
                                                if selected_unit.inRange(castle):
                                                    selected_unit.action = True
                                                    phase.action_counter += 1

                                                    if not selected_unit.spirited:
                                                        castle.health -= selected_unit.attack

                                                    elif selected_unit.spirited:
                                                        castle.health -= selected_unit.attack + 2

                                                    # chat log
                                                    chat3 = chat2

                                                    chat2 = chat1

                                                    if not selected_unit.spirited:
                                                        chat1 = font4.render(
                                                            str(castle.name) + '. -' + str(selected_unit.attack), True, black)

                                                    elif selected_unit.spirited:
                                                        chat1 = font4.render(
                                                            str(castle.name) + '. -' + str(selected_unit.attack + 2), True, black)

                                                    print(castle.health)

    for unit in units_list:
        if unit.code == 14:
            if unit.stop == False:
                if unit.attacked_unit != None:
                    if unit.attacked_unit.health <= 0:
                        unit.attack = 4
                        unit.max_health = 9
                        unit.health += 1
                        unit.move = 3
                        unit.idle = pygame.image.load('warrior.png')
                        unit.first = pygame.image.load('warrior 1.png')
                        unit.second = pygame.image.load('warrior 2.png')
                        if unit.team == 1 or unit.team == 2:
                            unit.idle = pygame.transform.flip(unit.idle, True, False)
                            unit.first = pygame.transform.flip(unit.first, True, False)
                            unit.second = pygame.transform.flip(unit.second, True, False)

                        unit.sprite = (unit.idle, unit.first, unit.second, unit.first)

                        for i in unit.sprite:

                            pxarray = pygame.PixelArray(i)

                            if unit.team == 0:

                                pxarray.replace(light_base, light_red)
                                pxarray.replace(dark_base, dark_red)

                            elif unit.team == 1:

                                pxarray.replace(light_base, light_blue)
                                pxarray.replace(dark_base, dark_blue)

                            elif unit.team == 2:

                                pxarray.replace(light_base, light_green)
                                pxarray.replace(dark_base, dark_green)

                            elif unit.team == 3:
                                pxarray.replace(light_base, light_yellow)
                                pxarray.replace(dark_base, dark_yellow)

                            pygame.PixelArray.close(pxarray)

                        unit.stop = True

    for unit in units_list:
        Unit.ALLfuncs(unit)
    for castle in castles_list:
        Castle.DEAD(castle)

    for castle in castles_list:
        if castle.isDead == True:
            for unit in units_list:
                if castle.team == unit.team:
                    unit.isDead = True
            for counter in counter_list:
                if counter.team == castle.team:
                    counter.value = 0

    for tile in tiles_list:
        for unit in units_list:

            if tile.rect.colliderect(unit.rect):
                tile.occupy = unit.team
                break

            elif tile.occupy == 5:
                break

            else:
                tile.occupy = 4

        for castle in castles_list:
            if castle.rect.colliderect(tile.rect):
                tile.occupy = castle.team

    for counter in counter_list:
        if counter.value == 0:
            for castle in castles_list:
                if castle.team == counter.team:
                    castle.isDead = True

    if turn == 0:
        bg = redBG

    elif turn == 1:
        bg = blueBG

    elif turn == 2:
        bg = greenBG

    elif turn == 3:
        bg = yellowBG

    for unit in units_list:
        if unit.stopMinus == False:
            if unit.isDead == True:
                for counter in counter_list:
                    if counter.team == unit.team:
                        counter.value -= 1
                        unit.stopMinus = True

    for unit in units_list:
        for tile in tiles_list:
            if unit.rect.colliderect(tile.rect):
                unit.stopMinus = False
                break

        if selected_unit != None:

            if selected_unit.rect.colliderect(unit.rect):
                if selected_unit != unit:
                    if selected_unit.HORSE == None or unit is selected_unit.HORSE:
                        if selected_unit.behind != unit.behind:
                            continue

                    onTOP = True
                    print('Press "q" to separate units')
                    break

            else:
                onTOP = False

    for tile in tiles_list:
        if tile.occupy == 5 or tile.occupy == turn:
            for unit in units_list:
                if tile.rect.colliderect(unit.rect):
                    tile.guy = unit
                    break
                else:
                    tile.guy = None

    if Mode(select_rect):
        selecting = True
        attacking = False

    elif Mode(attacking_rect):
        selecting = False
        attacking = True

    for unit in units_list:
        if selecting == True and unit.rect.collidepoint(pos) and pressed1 and onTOP == False:
            if unit.behind == True:
                continue
            selected_unit = unit

    for unit in units_list:
        for spirit in spirit_list:
            if spirit.team == unit.team:
                if unit.rect.colliderect(spirit.rect):
                    unit.spirited = True

                else:
                    unit.spirited = False
            else:
                continue

    redrawGameWindow()

pygame.quit()


