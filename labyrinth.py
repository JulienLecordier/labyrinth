'''edm : créer un labyrinthe aléatoire qui se résout seul
Auteur : Julien Lecordier
date : Janvier 2019
'''

import pygame
import random
import time, sys

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

pygame.init()

largeur = 70
hauteur = 70
 
surface = pygame.display.set_mode((largeur*10,hauteur*10))
game_over = False
pygame.display.set_caption("Labyrinthe")
surface.fill(white)
pygame.display.update()

print('')
print('Génération du labyrinthe...')
print('')

#on créé une matrice aléatoire qui sert de base au labyrinthe :
M = [[random.randint(0,1) for i in range(hauteur)] for j in range(largeur)] 



for j in range (largeur): #traçage des bords
    M[int(j)][0] = 1
for j in range (largeur):
    M[int(j)][hauteur-1] = 1
for i in range (hauteur):
    M[0][int(i)] = 1
for i in range (hauteur):
    M[int(largeur-1)][int(i)] = 1


j = 1
i = hauteur -2
M[int(j)][int(i)] = 0
a = random.randint(0,1)
while j < largeur-1:#on trace au moins un chemin possible aléatoire pour le robot
    if a == 1:
        j = j + 1
    if a == 0 and i > 1 :
        i = i - 1
    if i < 1:
        i = 1
    if j<1:
        j=1
    if i>hauteur-2:
        i = hauteur-3
    M[int(j)][int(i)] = 0
    a = random.randint(0,1)
    

sens = 'droite'


x = 0 #x correspond à j, 0 à gauche 
y = int(hauteur-2) #y correspond à i, 0 en haut (y augmente vers le bas)

M[x][y] = 2
def déplacement(x,y,sens,M):
    if sens == 'droite':

        if M[x][y-1] == 1: #on regarde ce qu'il y a à sa gauche
            if M[x+1][y] == 0: #on regarde ce qu'il y a devant lui
                return(x+1,y,'droite')
            else:
                if M[x][y+1] == 0: #on regarde ce qu'il y a à sa droite
                    return(x,y+1,'bas')
                else:
                    return(x-1,y,'gauche') #demi-tour chef
        else:
            return(x,y-1,'haut')
        
    if sens == 'bas':
        if M[x+1][y] == 1: #on regarde ce qu'il y a à sa gauche
            if M[x][y+1] == 0: #on regarde ce qu'il y a devant lui
                return(x,y+1,'bas')
            else:
                if M[x-1][y] == 0: #on regarde ce qu'il y a à sa droite
                    return(x-1,y,'gauche')
                else:
                    return(x,y-1,'haut') #demi-tour chef
        else:
            return(x+1,y,'droite')

    if sens == 'haut':
        if M[x-1][y] == 1: #on regarde ce qu'il y a à sa gauche
            if M[x][y-1] == 0: #on regarde ce qu'il y a devant lui
                return(x,y-1,'haut')
            else:
                if M[x+1][y] == 0: #on regarde ce qu'il y a à sa droite
                    return(x+1,y,'droite')
                else:
                    return(x,y+1,'bas') #demi-tour chef
        else:
            return(x-1,y,'gauche')
        
    if sens == 'gauche':

        if M[x][y+1] == 1: #on regarde ce qu'il y a à sa gauche
            if M[x-1][y] == 0: #on regarde ce qu'il y a devant lui
                return(x-1,y,'gauche')
            else:
                if M[x][y-1] == 0: #on regarde ce qu'il y a à sa droite
                    return(x,y-1,'haut')
                else:
                    return(x+1,y,'droite') #demi-tour chef
        else:
            return(x,y+1,'bas')

        

print('Début de la résolution...')             

''' boucle principale
'''
while not game_over : 
    time.sleep(0.05)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #detection clic croix rouge fenetre
            game_over = True
            pygame.quit()
    
    for j in range (0,hauteur):     #affichage du labyrinthe
        for i in range (0,largeur):
            if M[i][j] == 1:
                pygame.draw.rect(surface, black,(i*10,j*10,10,10))
            if M[i][j] == 0:
                pygame.draw.rect(surface, white,(i*10,j*10,10,10))
            if M[i][j] == 2:
                pygame.draw.rect(surface, red,(i*10,j*10,10,10))
    pygame.display.update()
        
    M[x][y] = 0 #mise à jour du robot
    x,y,sens = déplacement(x,y,sens,M)
    M[x][y] = 2
    if x >= largeur-1 :
        game_over = True
    
print('')
print('Nous avons trouvé la sortie !')

#on attend que l'utilisateur ferme la fenêtre
game_over = False
while not game_over : 
    time.sleep(0.05)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #detection clic croix rouge fenetre
            game_over = True
            pygame.quit()
