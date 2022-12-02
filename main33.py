import pyxel

# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(128, 128, title="Nuit du c0de")

# position initiale du vaisseau et de la balle
# (origine des positions : coin haut gauche)
vaisseau_x = 48
vaisseau_y = 110
balle_x = 64
balle_y = 105

def vaisseau_deplacement(x, y):
    """déplacement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 96) :
            x = x + 2
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 0) :
            x = x - 2
    return x, y

def balle_deplacement(x, y):
    x = x + 1
    y = y - 1
    if (y == 123) or (y == 5):
        y = -1 * y
    if (x == 5):
        x = -1 * x
    
    return x, y

# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y, balle_x, balle_y

    # mise à jour de la position du vaisseau
    vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)
    
    #mise a jour de la position de la balle
    balle_x, balle_y = balle_deplacement(balle_x, balle_y)


# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""
    
    global vaisseau_x, vaisseau_y, balle_x, balle_y

    # vide la fenetre
    pyxel.cls(0)

    # vaisseau (rectanle 32x4)
    pyxel.rect(vaisseau_x, vaisseau_y, 32, 4, 6)
    
    # balle (cercle de rayon 4)
    pyxel.circ(balle_x, balle_y, 4, 3)

pyxel.run(update, draw)
