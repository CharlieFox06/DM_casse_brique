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
score = 990

def vaisseau_deplacement(x, y):
    """déplacement avec les touches de directions"""
    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 80):
            x += 1
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 15):
            x -= 1
    return x, y

def balle_deplacement(x, y):
    x += dx
    y += dy
    return x, y

"""
def balle_deplacement(x, y):
    x += dx
    y += dy
    if y <= bord_gauche or y >= bord_droite:
        dy = -dy
    if x <= bord_haut:
        dx = -dx
    return x, y
"""

# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y, balle_x, balle_y, x, y, dx, dy

    # mise à jour de la position du vaisseau
    vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)
    
    # mise a jour de la position de la balle
    balle_x, balle_y = balle_deplacement(balle_x, balle_y)

# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""
    
    global vaisseau_x, vaisseau_y, balle_x, balle_y, x, y, dx, dy

    # vide la fenetre
    pyxel.cls(0)

    # vaisseau (rectanle 32x4)
    pyxel.rect(vaisseau_x, vaisseau_y, 32, 16, 12)
    pyxel.tri(vaisseau_x, vaisseau_y, vaisseau_x, vaisseau_y+15, vaisseau_x-15, vaisseau_y+15, 12)
    pyxel.tri(vaisseau_x+32, vaisseau_y, vaisseau_x+32, vaisseau_y+15, vaisseau_x+47, vaisseau_y+15, 12)
    pyxel.rect(vaisseau_x-15, vaisseau_y+15, 63, 4, 12)
    
    # balle (cercle de rayon 4)
    pyxel.circ(balle_x, balle_y, 4, 10)
    
    # score
    pyxel.text(2, 2, f"score: {score}", 7)
    # briques
    pyxel.rect(56, 40, 16, 4, 4)   
    pyxel.rect(36, 40, 16, 4, 4) 
    pyxel.rect(76, 40, 16, 4, 4) 
pyxel.run(update, draw)
