import pygame
from pygame import mixer
pygame.init()
mixer.init()
woman=False
s_ou_n= 0
size=((800, 600))
ima=pygame.image.load("medo.png")
image=pygame.transform.scale(ima, (800, 600))
sim= pygame.image.load('sim.png')
cam=pygame.image.load("campo.png")
não=pygame.image.load('não.png')
campop=pygame.transform.scale(cam, (800, 600))
mouse= pygame.image.load('mouse.png')

size= (800, 600)

mixer.music.set_volume(300)



screen = pygame.display.set_mode((size))
fim = False

while not fim:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
      key = pygame.key.get_pressed()
      if key[pygame.K_ESCAPE]:
         pygame.quit()
      elif key[pygame.K_SPACE]:
         pygame.mouse.set_pos(0, 400)
      m = pygame.mouse.get_pos()
      mp = pygame.mouse.get_pressed()
               #x                y               y
      if 0 <= m[0] <= 160 and  m[1] <= 480 and m[1] >= 400 :
         if mp[0]:
            s_ou_n=1
              #x               y                 y
      elif  m[0] >= 400 and  m[1] >= 400  and  m[1] < 480 :
         if mp[0]:
            s_ou_n=2

      screen.fill((0, 0, 0))
      screen.blit(sim, (10, 400))
      screen.blit(não, (400,400))
      screen.blit(mouse, (m))
      m =pygame.mouse.get_pos()
      

      
      if s_ou_n == 1:
         mixer.music.load("woman.mp3")
         woman = 1

      if s_ou_n == 2:
         
         mixer.music.load("campo.mp3")

      
      
      
      
      
      
      if s_ou_n == 1:
         screen.blit(image, (0, 0))
         mixer.music.play()
      elif s_ou_n == 2:
         screen.blit(campop, (0, 0))
         mixer.music.play()
      print(m)
      pygame.display.flip()
