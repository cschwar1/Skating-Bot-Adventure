from kivy.core.image import Image as CoreImage
from kivy.graphics import Rectangle

# Load images
background = CoreImage("src/assets/images/winter_background.png")
robot_texture = CoreImage("src/assets/images/robot_skater.png").texture
snowball_texture = CoreImage("src/assets/images/snowball.png").texture
ice_block_texture = CoreImage("src/assets/images/ice_block.png").texture
slope_texture = CoreImage("src/assets/images/slope.png").texture
menu_background = CoreImage("src/assets/images/menu_background.png").texture
button_texture = CoreImage("src/assets/images/button.png").texture

def draw_background(canvas):
    canvas.add(Rectangle(texture=background.texture, pos=(0, 0), size=(800, 600)))

def draw_robot(canvas, x, y, width, height):
    canvas.add(Rectangle(texture=robot_texture, pos=(x, y), size=(width, height)))

def draw_snowball(canvas, x, y, width, height):
    canvas.add(Rectangle(texture=snowball_texture, pos=(x, y), size=(width, height)))

def draw_ice_block(canvas, x, y, width, height):
    canvas.add(Rectangle(texture=ice_block_texture, pos=(x, y), size=(width, height)))

def draw_slope(canvas, x, y, width, height):
    canvas.add(Rectangle(texture=slope_texture, pos=(x, y), size=(width, height)))

def draw_menu_background(canvas):
    canvas.add(Rectangle(texture=menu_background, pos=(0, 0), size=(800, 600)))

def draw_button(canvas, x, y, width, height):
    canvas.add(Rectangle(texture=button_texture, pos=(x, y), size=(width, height)))