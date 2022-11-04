from pelota import Pelota

nueva_pelota = Pelota()
nueva_pelota.height = 100
nueva_pelota.speed_x = 5
nueva_pelota.speed_y = 5
nueva_pelota.ancho_pelota(100)
nueva_pelota.coor_pelota_x(400)
nueva_pelota.coor_pelota_y(300)

from jugador import Jugador

nuevo_jugador = Jugador()
nuevo_jugador.height = 90
nuevo_jugador.width = 15
nuevo_jugador.player1_x_coor

class Juego():
    import pygame 
    pygame.init() 
    import time

    #Variables Extra
    tiempo = 100
    tiempo1= 70
    contador = 2


    #Colores
    black = (0, 0, 0)
    white = (255, 255, 255)
    screen_size = (800, 600)

    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()

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

        if tiempo > 800:
            break

        screen.fill(black)
        #Zona de dibujo
        jugador1 = pygame.draw.rect(screen, white, (player1_x_coor, player1_y_coor, player_width, player_height))
        jugador2 = pygame.draw.rect(screen, white, (player2_x_coor, player2_y_coor, player_width, player_height))
        pelota = pygame.draw.circle(screen, white, (pelota_x, pelota_y), 10)

        screen.blit(mitexto,(200,10))
        screen.blit(mitexto2,(600,10))
        screen.blit(mitexto3,(350,10))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()