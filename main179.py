import pyxel
#https://kitao.github.io/pyxel/wasm/launcher/?run=CharlieFox06.DM_casse_brique.main162

# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(128, 128, title="Charlie Casse Brique")

# position initiale du vaisseau et de la balle
# (origine des positions : coin haut gauche)
vaisseau_x = 48
vaisseau_y = 100
balle_x = 64
balle_y = 95
dx = 10
dy = -10
bord_haut = 4
bord_gauche = 4
bord_droite = 123
score = 0
vies = 3
bord_gauche_briques = 106
bord_droite_briques = 22
bord_haut_briques = 44
bord_bas_briques = 40

def vaisseau_deplacement(x, y):
    """déplacement avec les touches de directions"""
    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 80):
            x += 1
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 15):
            x -= 1
    return x, y

def balle_deplacement(x, y, dx, dy):
    x += dx
    y += dy
    if x <= bord_gauche:
        dx = -dx
    if x >= bord_droite:
        dx = -dx
    if y <= bord_haut:
        dy = -dy
    
    if x == bord_gauche_briques and bord_bas_briques <= y <= bord_haut_briques:
        dx = -dx
    if x == (bord_droite_briques - 5) and bord_bas_briques <= y <= bord_haut_briques:
        dx = -dx
    if y == (bord_haut_briques + 4) and bord_droite_briques <= x <= bord_gauche_briques:
        dy = -dy
    if y == (bord_bas_briques - 5) and bord_droite_briques <= x <= bord_gauche_briques:
        dy = -dy
    
    return x, y, dx, dy

def bounce_off_vaisseau(x, y, dx, dy, vaisseau_x, vaisseau_y):
    """ rebondi sur le haut du vaisseau """
    if y == (vaisseau_y - 5) and vaisseau_x <= x <= (vaisseau_x + 32):
        dy = -dy
    """ rebondi sur le triangle gauche du vaisseau """
    #if y and x
    """ rebondi sur le triangle droit du vaisseau """
    #if y and x
    return x, y, dx, dy, vaisseau_x, vaisseau_y

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
    
    # vies (rectangle) (x, y, "texte", couleur)
    pyxel.text(2, 8, f"vies: {vies}", 7)
    
    # briques (rectangle) (x, y, taille_x, taille_y, couleur)
    pyxel.rect(22, 40, 16, 4, 4) 
    pyxel.rect(39, 40, 16, 4, 4)   
    pyxel.rect(56, 40, 16, 4, 4) 
    pyxel.rect(73, 40, 16, 4, 4) 
    pyxel.rect(90, 40, 16, 4, 4) 
    
pyxel.run(update, draw)
