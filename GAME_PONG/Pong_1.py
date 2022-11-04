import pygame 
pygame.init() 
import time

#Variables Extra
tiempo = 100
tiempo1= 70
contador = 2


#Colores
verde = (34,139,34)
rojo = (250,128,114)
amarillo = (255,255,0)
black = (0, 0, 0)
white = (255, 255, 255)
screen_size = (800, 600)
player_width = 15
player_height = 90

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

#Coordenadas y velocidad del jugador 1
player1_x_coor = 50
player1_y_coor = 300 -45
player1_y_speed = 0

#Coordenadas y velocidad del jugador 2
player2_x_coor = 750 - player_width
player2_y_coor = 300 - 45
player2_y_speed = 0

# Coordenadas de la pelota
pelota_x = 400
pelota_y = 300
pelota_speed_x = 4
pelota_speed_y = 4

#Obstaculo
obstaculo_x = 395
obstaculo_y = 10
obstaculo_velocidad_y = 1

#Obstaculo_2
obstaculo2_x = 395
obstaculo2_y = 520
obstaculo2_velocidad_y = 1


#Puntos
MarcadorA = 0
MarcadorB = 0

game_over = False


while not game_over:
    mifuente=pygame.font.Font(None,100)
    mitexto=mifuente.render(str(MarcadorA),25,(white))
    mifuente=pygame.font.Font(None,100)
    mitexto2=mifuente.render(str(MarcadorB),25,(white))
    mifuente=pygame.font.Font(None,100)
    mitexto3=mifuente.render(str(tiempo),25,(white))
    tiempo2=pygame.time.get_ticks()/1000
    tiempo -= 1
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            #Jugador 1
            if event.key == pygame.K_w:
                player1_y_speed = -7
            if event.key == pygame.K_s:
                player1_y_speed = 7
            #Jugador 2
            if event.key == pygame.K_UP:
                player2_y_speed = -7
            if event.key == pygame.K_DOWN:
                player2_y_speed = 7

        if event.type == pygame.KEYUP:
            #Jugador 1
            if event.key == pygame.K_w:
                player1_y_speed = 0
            if event.key == pygame.K_s:
                player1_y_speed = 0
            #Jugador 2
            if event.key == pygame.K_UP:
                player2_y_speed = 0
            if event.key == pygame.K_DOWN:
                player2_y_speed = 0

    if pelota_y > 590 or pelota_y < 10:
        pelota_speed_y *= -1
    
    #Limite de Obstaculo 1
    if obstaculo_y > 229 or obstaculo_y < 10:
       obstaculo_velocidad_y *= -1
    
    #Limite de Obstaculo 2
    if obstaculo2_y > 520 or obstaculo2_y < 301:
      obstaculo2_velocidad_y *= -1

    if tiempo > 800:
        break

    
        
    #Revisa si la pelota sale del lado derecho
    if pelota_x > 800:
        pelota_x = 400
        pelota_y = 300
        MarcadorA +=1
        '''
        if MarcadorA == contador:
            break 
        print("Ganaste, jugador A")
        '''
        #Si sale de la pantalla, invierte direccion
        pelota_speed_x *= -1
        pelota_speed_y *= -1

    #Revisa si la pelota sale del lado izquierdo
    if pelota_x < 0:
        pelota_x = 400
        pelota_y= 300
        MarcadorB+=1
        #Si sale de la pantalla, invierte direccion
        pelota_speed_x *= -1
        pelota_speed_y *= -1
        


    # Modifica las coordenadas para dar movimiento
    player1_y_coor += player1_y_speed
    player2_y_coor += player2_y_speed
    #Movimiento pelota
    pelota_x += pelota_speed_x
    pelota_y += pelota_speed_y

    #Movimiento Obstaculos
    obstaculo_y += obstaculo_velocidad_y
    obstaculo2_y -= obstaculo2_velocidad_y


    screen.fill(verde)
    #Zona de dibujo
    jugador1 = pygame.draw.rect(screen, rojo, (player1_x_coor, player1_y_coor, player_width, player_height))
    jugador2 = pygame.draw.rect(screen, amarillo, (player2_x_coor, player2_y_coor, player_width, player_height))
    circulo = pygame.draw.ellipse(screen, white,(300,200,200,200),5)
    linea = pygame.draw.rect(screen,white,(400,0,5,600))
    #CANCHA
    #linea1cancha=pygame.draw.rect(screen,white,(0,150,150,5))
    #linea2cancha=pygame.draw.rect(screen,white,(0,450,150,5))
    #BORDES
    borde1h=pygame.draw.rect(screen,black,(0,0,800,10))
    borde2h=pygame.draw.rect(screen,black,(1,590,800,10))
    borde3=pygame.draw.rect(screen,black,(0,0,10,600))
    borde4=pygame.draw.rect(screen,black,(790,5,10,800))

    obstaculo = pygame.draw.rect(screen, rojo,(obstaculo_x,obstaculo_y,15,70))
    obstaculo2 = pygame.draw.rect(screen, amarillo,(obstaculo2_x,obstaculo2_y,15,70))
    pelota = pygame.draw.circle(screen, white, (pelota_x, pelota_y), 10)
    
    

    #COLISION DE PELOTA Y JUGADORES
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2) or pelota.colliderect(obstaculo) or pelota.colliderect(obstaculo2):
        pelota_speed_x *= -1
    
    #COLISION DE OBSTACULOS Y PELOTA
    if obstaculo.colliderect(obstaculo2) or obstaculo2.colliderect(obstaculo):
        obstaculo_velocidad_y *= -1
        obstaculo2_velocidad_y *= -1
    

    #print(pelota_x, pelota_y)
    #print(MarcadorA, MarcadorB)
    screen.blit(mitexto,(200,10))
    screen.blit(mitexto2,(600,10))
    #screen.blit(mitexto3,(350,10))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
