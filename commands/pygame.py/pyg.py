#pgzero

WIDTH = 600
HEIGHT = 400

TITLE = "Clicker animal"
FPS = 30

# Objetos
animal = Actor("giraffe", (150, 250))
background = Actor("background")
bonus_1 = Actor("bonus", (450, 100))
bonus_2 = Actor("bonus", (450, 200))
play = Actor("play", (300, 100))
cross = Actor("cross", (580, 20))
shop = Actor("tienda", (300, 200))
collection = Actor("coleccion", (300, 300))
crocodile = Actor("crocodile", (120,200))
hippo = Actor("hippo", (300,200))
walrus = Actor("walrus, (480,200")
# Variables
count = 3000
click = 1
mode = 'menu'
animals = []

def draw():
    if mode == 'menu':
        background.draw()
        play.draw()
        screen.draw.text(count, center=(30, 20), color="white", fontsize = 36)
        shop.draw()
        collection.draw()
   
    elif mode == 'game':    
        background.draw()
        animal.draw()
        screen.draw.text(count, center=(150, 100), color="white", fontsize = 96)
        bonus_1.draw()
        screen.draw.text("+1$ cada 2s", center=(450, 80), color="black", fontsize = 20)
        screen.draw.text("PRECIO: 15$", center=(450, 110), color="black", fontsize = 20)
        bonus_2.draw()
        screen.draw.text("+15$ cada 2s", center=(450, 180), color="black", fontsize = 20)
        screen.draw.text("PRECIO: 200$", center=(450, 210), color="black", fontsize = 20)
        cross.draw()
    elif mode == "shop":
        background.draw()
        screen.draw.text(count, center=(30, 20), color="white", fontsize = 36)
        cross.draw()
        crocodile.draw()
        hippo.draw()
        screen.draw.text("500$", center= (120, 300), color="white", fontsize = 36)
        screen.draw.text("2500$", center= (300, 300), color="white", fontsize = 36)
        
    elif mode == "collection":
        background.draw()
        screen.draw.text(count, center=(30, 20), color="white", fontsize = 36)
        cross.draw()
        screen.draw.text("+2$", center=(120,300), color="white", fontsize = 36)
        screen.draw.text("+3$", center= (300, 300), color="white", fontsize = 36)
        for i in range(len(animals)):
            animals[i].draw()
        
        
def for_bonus_1():
    global count
    count += 1

def for_bonus_2():
    global count
    count += 15

def on_mouse_down(button, pos):
    global count
    global mode
    global click
    if button == mouse.LEFT and mode == 'game':
        # Click en el objeto animal
        if animal.collidepoint(pos):
            count += click
            animal.y = 200
            animate(animal, tween='bounce_end', duration=0.5, y=250)
        # Click en el botón bonus_1  
        elif bonus_1.collidepoint(pos):
            if count >= 15:
                schedule_interval(for_bonus_1, 2)
                count -= 15
        # Click en el botón bonus_2
        elif bonus_2.collidepoint(pos):
            if count >= 200:
                schedule_interval(for_bonus_2, 2)
                count -= 200
        # Modo menú
        elif cross.collidepoint(pos):
            mode = 'menu'
    
    elif mode == 'menu' and button == mouse.LEFT:
        if play.collidepoint(pos):
            mode = "game"
        elif shop.collidepoint(pos):
            mode = "shop"
        elif collection.collidepoint(pos):
            mode = "collection"
            
    elif mode == "shop" and button == mouse.LEFT:
        if cross.collidepoint(pos):
            mode = "menu"
        if crocodile.collidepoint(pos):
            if crocodile in animals:
                animal.image = "crocodile"
            elif count >= 500:
                count -=500
                click = 2
                animal.image = "crocodile"
                animals.append(crocodile)
        elif hippo.collidepoint(pos):
            if hippo in animals:
                animal.image = "hippo"
            if count >= 2500:
                count -=2500
                click = 3
                animal.image = "hippo"
                animals.append(hippo)
    elif mode == "collection" and button == mouse.LEFT:
        if cross.collidepoint(pos):
            mode = "menu"
        elif crocodile.collidepoint(pos):
            if crocodile in animals:
                animal.image = "crocodile"
        elif hippo.collidepoint(pos):
            if hippo in animals:
                animal.image = "hippo"