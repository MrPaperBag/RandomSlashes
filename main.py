from os import environ
#environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import random
import pyperclip

pygame.init()

over = False
bg = (0,0,0)

FPS = 30
w, h = 500, 500
Dis = pygame.display.set_mode((w, h))
w, h = pygame.display.get_surface().get_size()
MainCam = pygame.Surface((w, h))
GUI = pygame.Surface((w, h))
CamPos = (0,0)
pygame.display.set_caption("GameName")
clock = pygame.time.Clock()

Data = ""

def Slash(Dis, pos, Len):
	global Data
	pygame.draw.line(Dis, (0,255,0), (pos[0] + Len, pos[1]), (pos[0], pos[1] + Len) )
	Data += "/"

def BSlash(Dis, pos, Len):
	global Data
	pygame.draw.line(Dis, (0,255,0), (pos[0], pos[1]), (pos[0] + Len, pos[1] + Len) )
	Data += "\\"

def UpdatePattern(Len):
	global Data
	MainCam.fill(bg)
	over = False
	for i in range(0, w+1, Len):
		for j in range(0, h+1, Len):
			random.choice([Slash, BSlash])(MainCam, (i,j), Len)
		Data += "\n"
	Dis.blit(MainCam, CamPos)
	#Dis.blit(GUI, CamPos)
	pygame.display.update()	

def RunGame():
	global Data
	over = False
	Len = 30
	for i in range(0, w+1, Len):
		for j in range(0, h+1, Len):
			random.choice([Slash, BSlash])(MainCam, (i,j), Len)
		Data += "\n"
	print(Data)
	pyperclip.copy(Data)
	Dis.blit(MainCam, CamPos)
	pygame.display.update()
	while not over:

		#MainCam.fill(bg)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				over = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r:
					Data = ""
					UpdatePattern(Len)
					print(Data)
					pyperclip.copy(Data)
				if event.key == pygame.K_s:
					name = input("Enter name of image: ") + ".jpeg"
					pygame.image.save(Dis, name)
					pyperclip.copy(Data)
		keys = pygame.key.get_pressed()







		clock.tick(30)

def CreateImg(n):
	global Data
	over = False
	Len = 30
	for i in range(0, w+1, Len):
		for j in range(0, h+1, Len):
			random.choice([Slash, BSlash])(MainCam, (i,j), Len)
		Data += "\n"
	print(Data)
	name = str(n) + ".jpeg"
	pygame.image.save(MainCam, name)


RunGame()
#CreateImg(2)