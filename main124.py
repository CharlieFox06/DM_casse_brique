import pyxel

# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(128, 128, title="Charlie Casse Brique")

# position initiale du vaisseau et de la balle
# (origine des positions : coin haut gauche)
vaisseau_x = 48
vaisseau_y = 100
balle_x = 64
balle_y = 95
dx = 1
dy = -1
bord_haut = 5
bord_gauche = 5
bord_droite = 123
score = 0
vies = 3

def vaisseau_deplacement(x, y):
    """déplacement avec les touches de directions"""
    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 80):
            x += 1
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 15):
            x -= 1
    return x, y
"""
def balle_deplacement(x, y):
    x += dx
    y += dy
    return x, y
"""
def balle_deplacement(x, y):
    x += dx
    y += dy
    if y <= bord_gauche:
       """ dx = -dx"""
    if y >= bord_droite:
       """ dx = -dx"""
    if x <= bord_haut:
       """ dy = -dy"""
    return x, y

# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y, balle_x, balle_y, bord_haut, bord_gauche, bord_droite

    # mise à jour de la position du vaisseau
    vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)
    
    # mise a jour de la position de la balle
    balle_x, balle_y = balle_deplacement(balle_x, balle_y)

# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""
    
    global vaisseau_x, vaisseau_y, balle_x, balle_y, bord_haut, bord_gauche, bord_droite

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