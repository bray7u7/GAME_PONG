class Jugador():
    
    def __init__(self):
     self.width = 0
     self.height = 0
    
    def jugador_ancho():
     player_width = 15
    def jugador_altura():
     player_height = 90
     
 #Coordenadas y velocidad del jugador 1
    player1_x_coor = 50
    player1_y_coor = 300 - 45
    player1_y_speed = 0

    #Coordenadas y velocidad del jugador 2
    player2_x_coor = 750 - jugador_ancho
    player2_y_coor = 300 - 45
    player2_y_speed = 0

    # Modifica las coordenadas para dar movimiento
    player1_y_coor += player1_y_speed
    player2_y_coor += player2_y_speed

    
    