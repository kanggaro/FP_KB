import pygame, sys, random
from likalikuJalur import *
from button import Button
from pygame.locals import *

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
s_width, s_height = SCREEN.get_size()

BG = pygame.image.load("assets/Background.png")

clock = pygame.time.Clock()
FPS = 60

background_group = pygame.sprite.Group()
sprite_group = pygame.sprite.Group()

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("8-BIT WONDER.TTF", size)

class Background(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()

		self.image = pygame.Surface([x,y])
		self.image.fill('white')
		self.image.set_colorkey('black')
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.y += 1
		self.rect.x += 1 
		if self.rect.y > s_height:
			self.rect.y = random.randrange(-10, 0)
			self.rect.x = random.randrange(-400, s_width)

class Game:
	def __init__(self):
		self.run_game()

	def create_background(self):
		for i in range(50):
			x = random.randint(1,6)
			background_image = Background(x,x)
			background_image.rect.x = random.randrange(0, s_width)
			background_image.rect.y = random.randrange(0, s_height)
			background_group.add(background_image)
			sprite_group.add(background_image)

	def run_update(self):
		sprite_group.draw(SCREEN)
		sprite_group.update()

	def run_game(self):
		self.create_background()
		while True:
			SCREEN.fill('black')
            # self.play()
            # self.options()
            # self.main_menu
			self.run_update()
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

			pygame.display.update()
			clock.tick(FPS)


def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
def credits():
    while True:
        CREDITS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        CREDITS_TEXT = get_font(75).render("CREDITS", True, "Black")
        CREDITS_RECT = CREDITS_TEXT.get_rect(center=(640, 130))
        SCREEN.blit(CREDITS_TEXT, CREDITS_RECT)
        CREDITS_TEXT = get_font(38).render("Muhammad Fuad 5025201000", True, "Black")
        CREDITS_RECT = CREDITS_TEXT.get_rect(center=(640, 290))
        SCREEN.blit(CREDITS_TEXT, CREDITS_RECT)
        CREDITS_TEXT1 = get_font(38).render("Afanfian Awamiry 5025201000", True, "Black")
        CREDITS_RECT1 = CREDITS_TEXT1.get_rect(center=(640, 390))
        SCREEN.blit(CREDITS_TEXT1, CREDITS_RECT1)
        CREDITS_TEXT2 = get_font(38).render("Muhammad Qushoyyi 5025201028", True, "Black")
        CREDITS_RECT2 = CREDITS_TEXT2.get_rect(center=(640, 490))
        SCREEN.blit(CREDITS_TEXT2, CREDITS_RECT2)

        CREDITS_BACK = Button(image=None, pos=(1110, 640), 
                            text_input="BACK", font=get_font(25), base_color="Black", hovering_color="Green")

        CREDITS_BACK.changeColor(CREDITS_MOUSE_POS)
        CREDITS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CREDITS_BACK.checkForInput(CREDITS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        # game = Game()
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
        CREDITS_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 400), 
                            text_input="CREDITS", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(45), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, CREDITS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    exec(open('likalikuJalur.py').read())
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    credits()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

   

main_menu()