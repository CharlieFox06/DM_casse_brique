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
balle_x = 64
balle_y = 95
dx = 1
dy = -1
bord_haut = 0
bord_gauche = 0
bord_droite = 128
score = 0
bord_droite_briques = 106
bord_gauche_briques = 22
bord_bas_briques = 44
bord_haut_briques = 40
r = 4

def vaisseau_deplacement(x, y):
    """déplacement avec les touches de directions"""
    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 80):
            x += 2
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 15):
            x -= 2
    return x, y

def balle_deplacement(x, y, dx, dy):
    x += dx
    y += dy
    if x <= bord_gauche + r:
        dx = -dx
    if x >= bord_droite - r:
        dx = -dx
    if y <= bord_haut + r:
        dy = -dy
    
    if x == bord_droite_briques and bord_haut_briques <= y <= bord_bas_briques:
        dx = -dx
    if x == (bord_gauche_briques - r) and bord_haut_briques <= y <= bord_bas_briques:
        dx = -dx
    if y == (bord_bas_briques + r) and bord_gauche_briques <= x <= bord_droite_briques:
        dy = -dy
    if y == (bord_haut_briques - r) and bord_gauche_briques <= x <= bord_droite_briques:
        dy = -dy
    
    return x, y, dx, dy

def bounce_off_vaisseau(x, y, dx, dy, vaisseau_x, vaisseau_y):
#    """ rebondi sur le haut du vaisseau """
#    if y == (vaisseau_y - 5) and vaisseau_x <= x <= (vaisseau_x + 32):
#        dy = -dy
#    """ rebondi sur le triangle gauche du vaisseau """
#    if (x == (vaisseau_x - 5) and y == (vaisseau_y - 4)) or (x == (vaisseau_x - 6) and y == (vaisseau_y - 3)) or (x == (vaisseau_x - 7) and y == (vaisseau_y - 2)) or (x == (vaisseau_x - 8) and y == (vaisseau_y - 1)) or (x == (vaisseau_x - 9) and y == (vaisseau_y)) or (x == (vaisseau_x - 10) and y == (vaisseau_y + 1)) or (x == (vaisseau_x - 11) and y == (vaisseau_y + 2)) or (x == (vaisseau_x - 12) and y == (vaisseau_y + 3)) or (x == (vaisseau_x - 13) and y == (vaisseau_y + 4)) or (x == (vaisseau_x - 14) and y == (vaisseau_y + 5)) or (x == (vaisseau_x - 15) and y == (vaisseau_y + 6)) or (x == (vaisseau_x - 16) and y == (vaisseau_y + 7)) or (x == (vaisseau_x - 17) and y == (vaisseau_y + 8)) or (x == (vaisseau_x - 18) and y == (vaisseau_y + 9)) or (x == (vaisseau_x - 19) and y == (vaisseau_y + 10)):
#        dx = -dx
#        dy = -dy
#    if (x == (vaisseau_x - 4) and y == (vaisseau_y - 4)) or (x == (vaisseau_x - 5) and y == (vaisseau_y - 3)) or (x == (vaisseau_x - 6) and y == (vaisseau_y - 2)) or (x == (vaisseau_x - 7) and y == (vaisseau_y - 1)) or (x == (vaisseau_x - 8) and y == (vaisseau_y)) or (x == (vaisseau_x - 9) and y == (vaisseau_y + 1)) or (x == (vaisseau_x - 10) and y == (vaisseau_y + 2)) or (x == (vaisseau_x - 11) and y == (vaisseau_y + 3)) or (x == (vaisseau_x - 12) and y == (vaisseau_y + 4)) or (x == (vaisseau_x - 13) and y == (vaisseau_y + 5)) or (x == (vaisseau_x - 14) and y == (vaisseau_y + 6)) or (x == (vaisseau_x - 15) and y == (vaisseau_y + 7)) or (x == (vaisseau_x - 16) and y == (vaisseau_y + 8)) or (x == (vaisseau_x - 17) and y == (vaisseau_y + 9)) or (x == (vaisseau_x - 18) and y == (vaisseau_y + 10)):
#        dx = -dx
#        dy = -dy
#    """ rebondi sur le triangle droit du vaisseau """
#    if (x == (vaisseau_x_2 + 2) and y == (vaisseau_y + 1)) or (x == (vaisseau_x_2 + 4) and y == (vaisseau_y + 2)) or (x == (vaisseau_x_2 + 6) and y == (vaisseau_y + 3)) or (x == (vaisseau_x_2 + 8) and y == (vaisseau_y + 4)) or (x == (vaisseau_x_2 + 10) and y == (vaisseau_y + 5)) or (x == (vaisseau_x_2 + 12) and y == (vaisseau_y + 6)) or (x == (vaisseau_x_2 + 14) and y == (vaisseau_y + 7)) or (x == (vaisseau_x_2 + 16) and y == (vaisseau_y + 8)) or (x == (vaisseau_x_2 + 18) and y == (vaisseau_y + 9)) or (x == (vaisseau_x_2 + 20) and y == (vaisseau_y + 10)) or (x == (vaisseau_x_2 + 22) and y == (vaisseau_y + 11)) or (x == (vaisseau_x_2 + 24) and y == (vaisseau_y + 12)) or (x == (vaisseau_x_2 + 26) and y == (vaisseau_y + 13)) or (x == (vaisseau_x_2 + 28) and y == (vaisseau_y + 14)) or (x == (vaisseau_x_2 + 30) and y == (vaisseau_y + 15)):
#        dx = -dx
#        dy = -dy
#    if (x == (vaisseau_x_2 + 1) and y == (vaisseau_y + 1)) or (x == (vaisseau_x_2 + 3) and y == (vaisseau_y + 2)) or (x == (vaisseau_x_2 + 5) and y == (vaisseau_y + 3)) or (x == (vaisseau_x_2 + 7) and y == (vaisseau_y + 4)) or (x == (vaisseau_x_2 + 9) and y == (vaisseau_y + 5)) or (x == (vaisseau_x_2 + 11) and y == (vaisseau_y + 6)) or (x == (vaisseau_x_2 + 13) and y == (vaisseau_y + 7)) or (x == (vaisseau_x_2 + 15) and y == (vaisseau_y + 8)) or (x == (vaisseau_x_2 + 17) and y == (vaisseau_y + 9)) or (x == (vaisseau_x_2 + 19) and y == (vaisseau_y + 10)) or (x == (vaisseau_x_2 + 21) and y == (vaisseau_y + 11)) or (x == (vaisseau_x_2 + 23) and y == (vaisseau_y + 12)) or (x == (vaisseau_x_2 + 25) and y == (vaisseau_y + 13)) or (x == (vaisseau_x_2 + 27) and y == (vaisseau_y + 14)) or (x == (vaisseau_x_2 + 29) and y == (vaisseau_y + 15)):
#        dx = -dx
#        dy = -dy
#    return x, y, dx, dy, vaisseau_x, vaisseau_y


def score_timer(score):
    if balle_y < 128:
        score += 1
    return score

# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y, balle_x, balle_y, dx, dy, score
    # mise à jour de la position du vaisseau
    vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)
    
    # mise a jour de la position de la balle
    balle_x, balle_y, dx, dy = balle_deplacement(balle_x, balle_y, dx, dy)
    balle_x, balle_y, dx, dy, vaisseau_x, vaisseau_y = bounce_off_vaisseau(balle_x, balle_y, dx, dy, vaisseau_x, vaisseau_y)
    
    # mise a jour du score (30 par seconde)
    score = score_timer(score)
    
# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""
    
    global vaisseau_x, vaisseau_y, balle_x, balle_y, dx, dy, score

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
    pyxel.text(2, 2, f"score: {score}", 7)
    
    # briques (rectangle) (x, y, taille_x, taille_y, couleur)
    pyxel.rect(22, 40, 16, 4, 4) 
    pyxel.rect(39, 40, 16, 4, 4)   
    pyxel.rect(56, 40, 16, 4, 4) 
    pyxel.rect(73, 40, 16, 4, 4) 
    pyxel.rect(90, 40, 16, 4, 4) 
    
pyxel.run(update, draw)
