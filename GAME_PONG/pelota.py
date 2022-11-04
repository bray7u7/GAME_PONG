class Pelota():

    def __init__(self):
        self.width = 50
        self.height = 50
        self.speed_x = 0
        self.speed_y = 0
        self.coor_pelota_x = 0
        self.coor_pelota_y = 0


    def ancho_pelota(self, ancho):
        self.width = ancho









    def altura_pelota():
     player_height = 90
    # Coordenadas de la pelota
    def coor_pelota_x():
     pelota_x = 400
    def coor_pelota_y():
     pelota_y = 300
    def vel_pelota_x():
     pelota_speed_x = 5
    def vel_pelota_y():
     pelota_speed_y = 5

    if coor_pelota_y > 590 or coor_pelota_y < 10:
            vel_pelota_y *= -1
    
    #Revisa si la pelota sale del lado derecho
    if coor_pelota_x > 800:
        coor_pelota_x = 400
        coor_pelota_y = 300
        MarcadorA +=1
    
        #Si sale de la pantalla, invierte direccion
        vel_pelota_x *= -1
        vel_pelota_y *= -1
    
    #Revisa si la pelota sale del lado izquierdo
    if coor_pelota_x < 0:
        coor_pelota_x = 400
        coor_pelota_y = 300
        MarcadorB+=1
        #Si sale de la pantalla, invierte direccion
        vel_pelota_x *= -1
        vel_pelota_y *= -1

    #Movimiento pelota
    coor_pelota_x += vel_pelota_x
    coor_pelota_y += vel_pelota_y

    