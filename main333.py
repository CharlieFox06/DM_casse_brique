import pyxel
#https://kitao.github.io/pyxel/wasm/launcher/?run=CharlieFox06.DM_casse_brique.main331

# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(128, 128, title="Charlie Casse Brique")

# position initiale du vaisseau et de la balle
# (origine des positions : coin haut gauche)
vaisseau_x = 48
vaisseau_y = 100
vaisseau_x_2 = vaisseau_x + 32
balle_x = 64
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

def balle_deplacement(x, y, dx, dy, brique_1, brique_2, brique_3, brique_4, brique_5, b_y, b_1_x, b_2_x, b_3_x, b_4_x, b_5_x, score):
    """la balle se deplace de dx en x et de dy en y"""
    x += dx
    y += dy
    """rebondissements sur les bords du jeu"""
    if x <= bord_gauche + r:
        dx = -dx
    if x >= bord_droite - (r+1):
        dx = -dx
    if y <= bord_haut + r:
        dy = -dy   
    """rebondissements sur les briques si elles sont présentes"""
    if brique_1 == True:
        if x == b_1_x and b_y <= y <= b_y + 4 + (r+1):
            dx = -dx
            brique_1 = False
            score += 100
        elif x == b_1_x + 16 + (r+5) and b_y <= y <= b_y + 4 + (r+1):
            dx = -dx
            brique_1 = False
            score += 100
        elif y == b_y and b_1_x <= x <= (b_1_x + 16):
            dy = -dy
            brique_1 = False
            score += 100
        elif y == b_y + 4 + (r+5) and b_1_x <= x <= (b_1_x + 16):
            dy = -dy
            brique_1 = False
            score += 100
    if brique_2 == True:
        if x == b_2_x and b_y <= y <= b_y + 4 + (r+1):
            dx = -dx
            brique_2 = False
            score += 200
        elif x == b_2_x + 16 + (r+5) and b_y <= y <= b_y + 4 + (r+1):
            dx = -dx
            brique_2 = False
            score += 200
        elif y == b_y and b_2_x <= x <= (b_2_x + 16):
            dy = -dy
            brique_2 = False
            score += 200
        elif y == b_y + 4 + (r+5) and b_2_x <= x <= (b_2_x + 16):
            dy = -dy
            brique_2 = False
            score += 200
    if brique_3 == True:
        if x == b_3_x and b_y <= y <= b_y + 4 + (r+1):
            dx = -dx
            brique_3 = False
            score += 300
        elif x == b_3_x + 16 + (r+5) and b_y <= y <= b_y + 4 + (r+1):
            dx = -dx
            brique_3 = False
            score += 300
        elif y == b_y and b_3_x <= x <= (b_3_x + 16):
            dy = -dy
            brique_3 = False
            score += 300
        elif y == b_y + 4 + (r+5) and b_3_x <= x <= (b_3_x + 16):
            dy = -dy
            brique_3 = False
            score += 300
    if brique_4 == True:
        if x == b_4_x and b_y <= y <= b_y + 4 + (r+1):
            dx = -dx
            brique_4 = False
            score += 200
        elif x == b_4_x + 16 + (r+5) and b_y <= y <= b_y + 4 + (r+1):
            dx = -dx
            brique_4 = False
            score += 200
        elif y == b_y and b_4_x <= x <= (b_4_x + 16):
            dy = -dy
            brique_4 = False
            score += 200
        elif y == b_y + 4 + (r+5) and b_4_x <= x <= (b_4_x + 16):
            dy = -dy
            brique_4 = False
            score += 200
    if brique_5 == True:
        if x == b_5_x and b_y <= y <= b_y + 4 + (r+1):
            dx = -dx
            brique_5 = False
            score += 100
        elif x == b_5_x + 16 + (r+5) and b_y <= y <= b_y + 4 + (r+1):
            dx = -dx
            brique_5 = False
            score += 100
        elif y == b_y and b_5_x <= x <= (b_5_x + 16):
            dy = -dy
            brique_5 = False
            score += 100
        elif y == b_y + 4 + (r+5) and b_5_x <= x <= (b_5_x + 16):
            dy = -dy
            brique_5 = False
            score += 100
    return x, y, dx, dy, brique_1, brique_2, brique_3, brique_4, brique_5, b_y, b_1_x, b_2_x, b_3_x, b_4_x, b_5_x, score
    
def bounce_off_vaisseau(x, y, dx, dy, vaisseau_x, vaisseau_y):
    """ rebondi sur le haut du vaisseau """
    if (vaisseau_y + 15 - (r + 1))>= y >= (vaisseau_y - (r + 1)) and vaisseau_x <= x <= (vaisseau_x + 32):
        dy = -dy
    """ rebondi sur le triangle gauche du vaisseau et sur le triangle droit du vaisseau """
    if 106 <= y <= 121:
        if y >= (-x + 106 + vaisseau_x - 2*(r+1)) and (vaisseau_x - 15 - r) <= x <= (vaisseau_x - r):
            dx = -dx
            dy = -dy
        elif y >= (x + 106 - (vaisseau_y+15) + 2*(r+1)) and (vaisseau_x_2 + 15 + r) >= x >= (vaisseau_x_2 + r):
            dx = -dx
            dy = -dy
    return x, y, dx, dy, vaisseau_x, vaisseau_y

def score_timer(score):
    """augmente le score au fur et a mesure du temps"""
    if balle_y < 128:
        score += 1
    return score

def vies_counter(vies, x, y, dx, dy):
    """compte le nombre de vies restantes et arrete le jeu lorsqu'il n'en reste plus"""
    if y >= 128:
        vies -= 1
        x = 64
        y = 94
        dx = 1
        dy = -1
    return vies, x, y, dx, dy

def briques_reactualisation(brique_1, brique_2, brique_3, brique_4, brique_5):
    """reactualisation des briques lorsquelles sont toutes eliminées"""
    if (brique_1 == False) and (brique_2 == False) and (brique_3 == False) and (brique_4 == False) and (brique_5 == False):
        brique_1 == True
        brique_2 == True
        brique_3 == True
        brique_4 == True
        brique_5 == True
    return brique_1, brique_2, brique_3, brique_4, brique_5

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
    balle_x, balle_y, dx, dy, brique_1, brique_2, brique_3, brique_4, brique_5, b_y, b_1_x, b_2_x, b_3_x, b_4_x, b_5_x, score = balle_deplacement(balle_x, balle_y, dx, dy, brique_1, brique_2, brique_3, brique_4, brique_5, b_y, b_1_x, b_2_x, b_3_x, b_4_x, b_5_x, score)   
    
    #mise a jour de la reapparition des briques
    brique_1, brique_2, brique_3, brique_4, brique_5 = briques_reactualisation(brique_1, brique_2, brique_3, brique_4, brique_5)
    
    # mise a jour du score et des vies (30 par seconde)
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
        """disparition des briques lorsqu'elles se font touchées par la balle"""
        if brique_1 == True:
            pyxel.rect(22, 40, 16, 4, 11)
        if brique_2 == True:
            pyxel.rect(39, 40, 16, 4, 4)
        if brique_3 == True:
            pyxel.rect(56, 40, 16, 4, 9)
        if brique_4 == True:
            pyxel.rect(73, 40, 16, 4, 4)
        if brique_5 == True:
            pyxel.rect(90, 40, 16, 4, 11)
        """réapparition des briques si elles sont toutes disparues"""
        if (brique_1 == False) and (brique_2 == False) and (brique_3 == False) and (brique_4 == False) and (brique_5 == False):
            pyxel.rect(22, 40, 16, 4, 11)
            pyxel.rect(39, 40, 16, 4, 4)
            pyxel.rect(56, 40, 16, 4, 9)
            pyxel.rect(73, 40, 16, 4, 4)
            pyxel.rect(90, 40, 16, 4, 11)

pyxel.run(update, draw)
