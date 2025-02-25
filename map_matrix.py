import pygame
import csv
# from Button import Button

# Initialisation de Pygame
pygame.init()
screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption('Map Matrix')

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (50, 50, 50)

class Button:
    def __init__(self, x, y, image, scale = ""):
        # Redimensionnement initial de l'image
        width = image.get_width()
        height = image.get_height()

        self.original_image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale)))    
        self.image = self.original_image

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.clicked = False

        self.u = "water"
        self.r = "water"
        self.d = "water"
        self.l = "water"

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Affichage de l'image actuelle
        screen = pygame.display.get_surface()
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

    def set_image(self, new_image):
        """Redimensionne et applique la nouvelle image."""
        if new_image == "water":
            self.image = pygame.transform.scale(water, (self.rect.width, self.rect.height))
            self.u = "water"
            self.r = "water"
            self.d = "water"
            self.l = "water"
        if new_image == "grass":
            self.image = pygame.transform.scale(grass, (self.rect.width, self.rect.height))
            self.u = "grass"
            self.r = "grass"
            self.d = "grass"
            self.l = "grass"
        if new_image == "sand":
            self.image = pygame.transform.scale(sand, (self.rect.width, self.rect.height))
            self.u = "sand"
            self.r = "sand"
            self.d = "sand"
            self.l = "sand"

    def update(self):

        if self.u == "grass":

            if self.r == "grass":

                if self.d == "grass":

                    if self.l == "grass":
                        self.image = pygame.transform.scale(grass, (self.rect.width, self.rect.height))
                    if self.l == "water":
                        self.image = pygame.transform.scale(GGGW, (self.rect.width, self.rect.height))
                    if self.l == "sand":
                        self.image = pygame.transform.scale(GGGS, (self.rect.width, self.rect.height))

                if self.d == "sand":
                    if self.l == "grass":
                        self.image = pygame.transform.scale(GGSG, (self.rect.width, self.rect.height))
                    if self.l == "sand":
                        self.image = pygame.transform.scale(GGSS, (self.rect.width, self.rect.height))
                    
                    

                if self.d == "water":

                    if self.l == "grass":
                        self.image = pygame.transform.scale(GGWG, (self.rect.width, self.rect.height))
                    if self.l == "water":
                        self.image = pygame.transform.scale(GGWW, (self.rect.width, self.rect.height))

            if self.r == "water":

                if self.d == "grass":

                    if self.l == "grass":
                        self.image = pygame.transform.scale(GWGG, (self.rect.width, self.rect.height))
                    if self.l == "water":
                        self.image = pygame.transform.scale(GWGW, (self.rect.width, self.rect.height))

                if self.d == "water":

                    if self.l == "grass":
                        self.image = pygame.transform.scale(GWWG, (self.rect.width, self.rect.height))
                    if self.l == "water":
                        self.image = pygame.transform.scale(GWWW, (self.rect.width, self.rect.height))
            
            if self.r == "sand":

                if self.d == "grass":

                    if self.l == "grass":
                        self.image = pygame.transform.scale(GSGG, (self.rect.width, self.rect.height))
                    if self.l == "sand":
                        self.image = pygame.transform.scale(GSGS, (self.rect.width, self.rect.height))

                if self.d == "sand":

                    if self.l == "grass":
                        self.image = pygame.transform.scale(GSSG, (self.rect.width, self.rect.height))
                    if self.l == "sand":
                        self.image = pygame.transform.scale(GSSS, (self.rect.width, self.rect.height))


        if self.u == "water":

            if self.r == "grass":

                if self.d == "grass":

                    if self.l == "grass":
                        self.image = pygame.transform.scale(WGGG, (self.rect.width, self.rect.height))
                    if self.l == "water":
                        self.image = pygame.transform.scale(WGGW, (self.rect.width, self.rect.height))

                if self.d == "water":

                    if self.l == "grass":
                        self.image = pygame.transform.scale(WGWG, (self.rect.width, self.rect.height))
                    if self.l == "water":
                        self.image = pygame.transform.scale(WGWW, (self.rect.width, self.rect.height))

            if self.r == "water":

                if self.d == "grass":

                    if self.l == "grass":
                        self.image = pygame.transform.scale(WWGG, (self.rect.width, self.rect.height))
                    if self.l == "water":
                        self.image = pygame.transform.scale(WWGW, (self.rect.width, self.rect.height))

                if self.d == "water":

                    if self.l == "grass":
                        self.image = pygame.transform.scale(WWWG, (self.rect.width, self.rect.height))
                    if self.l == "water":
                        self.image = pygame.transform.scale(water, (self.rect.width, self.rect.height))
                    if self.l == "sand":
                        self.image = pygame.transform.scale(WWWS, (self.rect.width, self.rect.height))

                if self.d == "sand":

                    if self.l == "sand":
                        self.image = pygame.transform.scale(WWSS, (self.rect.width, self.rect.height))
                    if self.l == "water":
                        self.image = pygame.transform.scale(WWSW, (self.rect.width, self.rect.height))

            
            if self.r == "sand":

                if self.d == "sand":

                    if self.l == "sand":
                        self.image = pygame.transform.scale(WSSS, (self.rect.width, self.rect.height))
                    if self.l == "water":
                        self.image = pygame.transform.scale(WSSW, (self.rect.width, self.rect.height))

                if self.d == "water":

                    if self.l == "sand":
                        self.image = pygame.transform.scale(WSWS, (self.rect.width, self.rect.height))
                    if self.l == "water":
                        self.image = pygame.transform.scale(WSWW, (self.rect.width, self.rect.height))
        
            
        if self.u == "sand":

            if self.r == "sand":

                if self.d == "sand":

                    if self.l == "sand":
                        self.image = pygame.transform.scale(sand, (self.rect.width, self.rect.height))
                    if self.l == "water":
                        self.image = pygame.transform.scale(SSSW, (self.rect.width, self.rect.height))
                    if self.l == "grass":
                        self.image = pygame.transform.scale(SSSG, (self.rect.width, self.rect.height))

                if self.d == "water":

                    if self.l == "sand":
                        self.image = pygame.transform.scale(SSWS, (self.rect.width, self.rect.height))
                    if self.l == "water":
                        self.image = pygame.transform.scale(SSWW, (self.rect.width, self.rect.height))

                if self.d == "grass":

                    if self.l == "sand":
                        self.image = pygame.transform.scale(SSGS, (self.rect.width, self.rect.height))
                    if self.l == "grass":
                        self.image = pygame.transform.scale(SSGG, (self.rect.width, self.rect.height))

            if self.r == "water":

                if self.d == "sand":

                    if self.l == "sand":
                        self.image = pygame.transform.scale(SWSS, (self.rect.width, self.rect.height))
                    if self.l == "water":
                        self.image = pygame.transform.scale(SWSW, (self.rect.width, self.rect.height))

                if self.d == "water":

                    if self.l == "sand":
                        self.image = pygame.transform.scale(SWWS, (self.rect.width, self.rect.height))
                    if self.l == "water":
                        self.image = pygame.transform.scale(SWWW, (self.rect.width, self.rect.height))
            
            if self.r == "grass":

                if self.d == "sand":

                    if self.l == "sand":
                        self.image = pygame.transform.scale(SGSS, (self.rect.width, self.rect.height))
                    if self.l == "grass":
                        self.image = pygame.transform.scale(SGSG, (self.rect.width, self.rect.height))

                if self.d == "grass":

                    if self.l == "sand":
                        self.image = pygame.transform.scale(SGGS, (self.rect.width, self.rect.height))
                    if self.l == "grass":
                        self.image = pygame.transform.scale(SGGG, (self.rect.width, self.rect.height))

                    
            

# Chargement des images
try:
    water = pygame.image.load('images/Eau.png').convert_alpha()
    grass = pygame.image.load('images/Herbe.png').convert_alpha()
    sand = pygame.image.load('images/Sable.png').convert_alpha()

    water_menu = pygame.image.load('images/water_menu.png').convert_alpha()
    grass_menu = pygame.image.load('images/grass_menu.png').convert_alpha()
    sand_menu= pygame.image.load('images/sand_menu.png').convert_alpha()

    GGGW = pygame.image.load('images/GGGW.png').convert_alpha()
    GGWG = pygame.image.load('images/GGWG.png').convert_alpha()
    GGWW = pygame.image.load('images/GGWW.png').convert_alpha()
    GWGG = pygame.image.load('images/GWGG.png').convert_alpha()
    GWGW = pygame.image.load('images/GWGW.png').convert_alpha()
    GWWG = pygame.image.load('images/GWWG.png').convert_alpha()
    GWWW = pygame.image.load('images/GWWW.png').convert_alpha()
    WGGG = pygame.image.load('images/WGGG.png').convert_alpha()
    WGGW = pygame.image.load('images/WGGW.png').convert_alpha()
    WGWG = pygame.image.load('images/WGWG.png').convert_alpha()
    WGWW = pygame.image.load('images/WGWW.png').convert_alpha()
    WWGG = pygame.image.load('images/WWGG.png').convert_alpha()
    WWGW = pygame.image.load('images/WWGW.png').convert_alpha()
    WWWG = pygame.image.load('images/WWWG.png').convert_alpha()
    SSSW = pygame.image.load('images/SSSW.png').convert_alpha()
    SSWS = pygame.image.load('images/SSWS.png').convert_alpha()
    SSWW = pygame.image.load('images/SSWW.png').convert_alpha()
    SWSS = pygame.image.load('images/SWSS.png').convert_alpha()
    SWSW = pygame.image.load('images/SWSW.png').convert_alpha()
    SWWS = pygame.image.load('images/SWWS.png').convert_alpha()
    SWWW = pygame.image.load('images/SWWW.png').convert_alpha()
    WSSS = pygame.image.load('images/WSSS.png').convert_alpha()
    WSSW = pygame.image.load('images/WSSW.png').convert_alpha()
    WSWS = pygame.image.load('images/WSWS.png').convert_alpha()
    WSWW = pygame.image.load('images/WSWW.png').convert_alpha()
    WWSS = pygame.image.load('images/WWSS.png').convert_alpha()
    WWSW = pygame.image.load('images/WWSW.png').convert_alpha()
    WWWS = pygame.image.load('images/WWWS.png').convert_alpha()
    GGGS = pygame.image.load('images/GGGS.png').convert_alpha()
    GGSG = pygame.image.load('images/GGSG.png').convert_alpha()
    GGSS = pygame.image.load('images/GGSS.png').convert_alpha()
    GSGG = pygame.image.load('images/GSGG.png').convert_alpha()
    GSGS = pygame.image.load('images/GSGS.png').convert_alpha()
    GSSG = pygame.image.load('images/GSSG.png').convert_alpha()
    GSSS = pygame.image.load('images/GSSS.png').convert_alpha()
    SGGG = pygame.image.load('images/SGGG.png').convert_alpha()
    SGGS = pygame.image.load('images/SGGS.png').convert_alpha()
    SGSG = pygame.image.load('images/SGSG.png').convert_alpha()
    SGSS = pygame.image.load('images/SGSS.png').convert_alpha()
    SSGG = pygame.image.load('images/SSGG.png').convert_alpha()
    SSGS = pygame.image.load('images/SSGS.png').convert_alpha()
    SSSG = pygame.image.load('images/SSSG.png').convert_alpha()
    
except FileNotFoundError:
    exit()



# Constantes
CASE_SIZE = 20
SPACING = 2
MENU_WIDTH = 200  # Largeur de la barre latérale
GRID_WIDTH = (screen.get_width() - MENU_WIDTH) // CASE_SIZE
GRID_HEIGHT = screen.get_height() // CASE_SIZE
BUTTON_SCALE = (CASE_SIZE - SPACING) / water.get_width()



# Offsets pour centrer la grille
grid_width_px = GRID_WIDTH * CASE_SIZE
grid_height_px = GRID_HEIGHT * CASE_SIZE
offset_x = (screen.get_width() - MENU_WIDTH - grid_width_px) // 2
offset_y = (screen.get_height() - grid_height_px) // 2



# Création de la grille
grid = []
for i in range(GRID_HEIGHT):
    row = []
    for j in range(GRID_WIDTH):
        x = offset_x + j * CASE_SIZE
        y = offset_y + i * CASE_SIZE
        button = Button(x, y, water, BUTTON_SCALE)
        row.append(button)
    grid.append(row)



# Création des boutons pour le menu latéral
menu_buttons = []
button_water = Button(screen.get_width() - MENU_WIDTH + 50, 100, water_menu, 0.12)
button_grass = Button(screen.get_width() - MENU_WIDTH + 50, 225, grass_menu, 0.1)
button_sand = Button(screen.get_width() - MENU_WIDTH + 50, 350, sand_menu, 0.1)
# button_export = Button(screen.get_width() - MENU_WIDTH + 50, 475, sand_menu, 0.1)
menu_buttons.append((button_water, "water"))
menu_buttons.append((button_grass, "grass"))
menu_buttons.append((button_sand, "sand"))
# menu_buttons.append((button_export, None))

# Texture par défaut
selection = grass


def exporter(grid):
    """
    Exporte la matrice `grid` dans un fichier CSV.
    Chaque case (button) est enregistrée sous la forme (u, r, d, l).
    """
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in grid:
            ligne = [(button.u, button.r, button.d, button.l)
                     for button in row]
            # Aplatir chaque tuple pour l'écriture dans le CSV
            writer.writerow([val for case in ligne for val in case])


def importer(GRID_WIDTH, GRID_HEIGHT, offset_x, offset_y, CASE_SIZE, Button, BUTTON_SCALE, water):
    """
    Importe la matrice de cases depuis un fichier CSV et retourne une grille reconstruite.
    """
    grid = []
    with open('output.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for i, line in enumerate(reader):
            row = []
            values = iter(line)  # On itère sur les valeurs à plat
            for j in range(GRID_WIDTH):
                x = offset_x + j * CASE_SIZE
                y = offset_y + i * CASE_SIZE
                button = Button(x, y, water, BUTTON_SCALE)
                # Lire les 4 paramètres de la case
                button.u = int(next(values))
                button.r = int(next(values))
                button.d = int(next(values))
                button.l = int(next(values))
                button.update()
                row.append(button)
            grid.append(row)
    return grid





# Boucle principale
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)

    # Dessiner la barre latérale
    pygame.draw.rect(screen, GREY, (screen.get_width() - MENU_WIDTH, 0, MENU_WIDTH, screen.get_height()))

    # Dessiner les boutons dans le menu
    for button, _ in menu_buttons:
        button.draw()

    # Événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gestion des clics dans le menu
    for button, texture_name in menu_buttons:
        if button.draw() and texture_name != None:  # Si le bouton est cliqué
            selection = texture_name
        if button.draw() and texture_name == None:
            exporter()

    # Dessiner la grille et appliquer la texture si cliquée
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            
            if grid[i][j].draw() and i >= 1 and i <= len(grid)-2 and j >= 1 and j <= len(grid[i])-2 :  # Si une case est cliquée
                
                grid[i][j].set_image(selection)      
                
                grid[i-1][j].d = selection
                grid[i-1][j].update()

                    
                grid[i+1][j].u = selection
                grid[i+1][j].update()

                    
                grid[i][j-1].r = selection
                grid[i][j-1].update()

                     
                grid[i][j+1].l = selection
                grid[i][j+1].update()    



    # Mise à jour de l'écran
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
