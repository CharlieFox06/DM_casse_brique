import pyxel
#https://kitao.github.io/pyxel/wasm/launcher/?run=CharlieFox06.DM_casse_brique.main162

# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(128, 128, title="Charlie Casse Brique")

# position initiale du vaisseau et de la balle
# (origine des positions : coin haut gauche)
vaisseau_x = 48
vaisseau_y = 100
vaisseau_x_2 = vaisseau_x + 32
balle_x = 84
balle_y = 94
dx = 1
dy = -1
bord_haut = 0
bord_gauche = 0
bord_droite = 128
score = 0
r = 4
vies = 3
b_y = 40 - (r+1)
b_1_x = 22 - (r+1)
b_2_x = 39 - (r+1)
b_3_x = 56 - (r+1)
b_4_x = 73 - (r+1)
b_5_x = 90 - (r+1)
brique_1 = True
brique_2 = True
brique_3 = True
brique_4 = True
brique_5 = True

def vaisseau_deplacement(x, y):
    """déplacement avec les touches de directions"""
    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 80):
            x += 2
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 15):
            x -= 2
    return x, y

def balle_deplacement(x, y, dx, dy, brique_1, brique_2, brique_3, brique_4, brique_5, b_y, b_1_x, b_2_x, b_3_x, b_4_x, b_5_x):
    x += dx
    y += dy
    if x <= bord_gauche + r:
        dx = -dx
    if x >= bord_droite - (r+1):
        dx = -dx
    if y <= bord_haut + r:
        dy = -dy   
    if brique_1 == True:
        if x == b_1_x and b_y <= y <= b_y + 4:
            dx = -dx
        elif x == b_1_x + 16 + (r+5) and b_y <= y <= b_y + 4:
            dx = -dx
        elif y == b_y and b_1_x <= x <= (b_1_x + 16):
            dy = -dy
        elif y == b_y + 4 + (r+5) and b_1_x <= x <= (b_1_x + 16):
            dy = -dy
    if brique_2 == True:
        if x == b_2_x and b_y <= y <= b_y + 4:
            dx = -dx
        elif x == b_2_x + 16 + (r+5) and b_y <= y <= b_y + 4:
            dx = -dx
        elif y == b_y and b_2_x <= x <= (b_2_x + 16):
            dy = -dy
        elif y == b_y + 4 + (r+5) and b_2_x <= x <= (b_2_x + 16):
            dy = -dy
    if brique_3 == True:
        if x == b_3_x and b_y <= y <= b_y + 4:
            dx = -dx
        elif x == b_3_x + 16 + (r+5) and b_y <= y <= b_y + 4:
            dx = -dx
        elif y == b_y and b_3_x <= x <= (b_3_x + 16):
            dy = -dy
        elif y == b_y + 4 + (r+5) and b_3_x <= x <= (b_3_x + 16):
            dy = -dy
    if brique_4 == True:
        if x == b_4_x and b_y <= y <= b_y + 4:
            dx = -dx
        elif x == b_4_x + 16 + (r+5) and b_y <= y <= b_y + 4:
            dx = -dx
        elif y == b_y and b_4_x <= x <= (b_4_x + 16):
            dy = -dy
        elif y == b_y + 4 + (r+5) and b_4_x <= x <= (b_4_x + 16):
            dy = -dy
    if brique_5 == True:
        if x == b_5_x and b_y <= y <= b_y + 4:
            dx = -dx
        elif x == b_5_x + 16 + (r+5) and b_y + 5 <= y <= b_y + 4 + 5:
            dx = -dx
        elif y == b_y and b_5_x <= x <= (b_5_x + 16):
            dy = -dy
        elif y == b_y + 4 + (r+5) and b_5_x <= x <= (b_5_x + 16):
            dy = -dy    
    return x, y, dx, dy, brique_1, brique_2, brique_3, brique_4, brique_5, b_y, b_1_x, b_2_x, b_3_x, b_4_x, b_5_x

def bounce_off_vaisseau(x, y, dx, dy, vaisseau_x, vaisseau_y):
    """ rebondi sur le haut du vaisseau """
    if (vaisseau_y + 15 - (r + 1))>= y >= (vaisseau_y - (r + 1)) and vaisseau_x <= x <= (vaisseau_x + 32):
        dy = -dy
    """ rebondi sur le triangle gauche du vaisseau et sur le triangle droit du vaisseau """
    if 106 <= y <= 121:
        if y >= (-x + 106 + vaisseau_x - (r+1)) and (vaisseau_x - 15 - (r+1)) <= x <= (vaisseau_x - (r+1)):
            dx = -dx
            dy = -dy
        elif y >= (x + 106 - vaisseau_x_2 + 2*(r+1)) and vaisseau_x_2 + 15 <= x <= vaisseau_x_2:
            dx = -dx
            dy = -dy
    return x, y, dx, dy, vaisseau_x, vaisseau_y

    #if  215 <= y <= (238):
    #   if (vaisseau_x -20) <= x < (vaisseau_x) or (vaisseau_x + 32) < x <= (vaisseau_x + 55):
    #        ball_y = ball_y + 5
    #        xball_speed = -xball_speed*1.015
    #        yball_speed = -yball_speed*1.015
    #    elif vaisseau_x <= x <= (vaisseau_x +32):
    #        ball_y = ball_y + 5
    #        xball_speed = xball_speed*1.015
    #        yball_speed = -yball_speed*1.015

def score_timer(score):
    if balle_y < 128:
        score += 1
    return score

def vies_counter(vies, x, y, dx, dy):
    if y >= 128:
        vies -= 1
        x = 64
        y = 94
        dx = 1
        dy = -1
    return vies, x, y, dx, dy

# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y, balle_x, balle_y, dx, dy, score, vies, brique_1, brique_2, brique_3, brique_4, brique_5, b_y, b_1_x, b_2_x, b_3_x, b_4_x, b_5_x
    # mise à jour de la position du vaisseau
    vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)
    
    # mise a jour de la position de la balle
    balle_x, balle_y, dx, dy, vaisseau_x, vaisseau_y = bounce_off_vaisseau(balle_x, balle_y, dx, dy, vaisseau_x, vaisseau_y)
    balle_x, balle_y, dx, dy, brique_1, brique_2, brique_3, brique_4, brique_5, b_y, b_1_x, b_2_x, b_3_x, b_4_x, b_5_x = balle_deplacement(balle_x, balle_y, dx, dy, brique_1, brique_2, brique_3, brique_4, brique_5, b_y, b_1_x, b_2_x, b_3_x, b_4_x, b_5_x)
    
    # mise a jour du score (30 par seconde)
    score = score_timer(score)
    vies, balle_x, balle_y, dx, dy = vies_counter(vies, balle_x, balle_y, dx, dy)
# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""
    
    global vaisseau_x, vaisseau_y, balle_x, balle_y, dx, dy, score, vies, brique_1, brique_2, brique_3, brique_4, brique_5, b_y, b_1_x, b_2_x, b_3_x, b_4_x, b_5_x
    
    if vies <= 0:
        pyxel.text(45,64, 'GAME OVER', 7)
    elif score >= 10001:
        pyxel.text(45,64, 'VICTOIRE!', 7)
    else: 
        # vide la fenetre
        pyxel.cls(0)

        # vaisseau (rectangles) (x, y, taille_x, taille_y, couleur)
        # vaisseau (triangles) (x1, y1, x2, y2, x3, y3, couleur)
        pyxel.rect(vaisseau_x, vaisseau_y, 32, 16, 12)
        pyxel.tri(vaisseau_x, vaisseau_y, vaisseau_x, vaisseau_y+15, vaisseau_x-15, vaisseau_y+15, 12)
        pyxel.tri(vaisseau_x+32, vaisseau_y, vaisseau_x+32, vaisseau_y+15, vaisseau_x+47, vaisseau_y+15, 12)
        pyxel.rect(vaisseau_x-15, vaisseau_y+15, 63, 4, 12)

        # balle (cercle) (x, y, rayon, couleur)
        pyxel.circ(balle_x, balle_y, 4, 10)

        # score (rectangle) (x, y, "texte", couleur)
        pyxel.text(2, 2, f"score: {score}/10000", 7)

        # vies (rectangle) (x, y, "texte", couleur)
        pyxel.text(2, 8, f"vies: {vies}", 7)

        # briques (rectangle) (x, y, taille_x, taille_y, couleur)
        pyxel.rect(22, 40, 16, 4, 4) 
        pyxel.rect(39, 40, 16, 4, 4)   
        pyxel.rect(56, 40, 16, 4, 4) 
        pyxel.rect(73, 40, 16, 4, 4) 
        pyxel.rect(90, 40, 16, 4, 4) 
    
pyxel.run(update, draw)
