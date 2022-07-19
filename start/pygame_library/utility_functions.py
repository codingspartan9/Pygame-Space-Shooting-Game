from pygame_library import library_abstraction
from pygame_library.keys import keyboard_keys_to_game_engine_keys
import pygame
import time

fonts = {}
images = {}

def convert_to_int(*args):
    return_value = []

    for arg in args:
        return_value.append(int(arg))

    return return_value

def load_image(path_to_image):
    if images.get(path_to_image) is None:
        images[path_to_image] = pygame.image.load(path_to_image).convert_alpha()

def load_text(name, font_size, background_color, text_color):
    if fonts.get(font_size) is None:
        fonts[font_size] = pygame.font.Font("freesansbold.ttf", font_size)

def render_text(left_edge, top_edge, text_color, background_color, text, font_size, is_centered, name):
    left_edge, top_edge = convert_to_int(left_edge, top_edge)

    font = fonts.get(font_size)
    rendered_text = font.render(text, True, text_color, background_color)
    text_rectangle = rendered_text.get_rect()

    if is_centered:
        text_rectangle.center = [left_edge, top_edge]

    else:
        text_rectangle.left = left_edge
        text_rectangle.top = top_edge

    library_abstraction.window.blit(rendered_text, text_rectangle)

def render_image(path_to_image, left_edge, top_edge, length, height):
    left_edge, top_edge, length, height = convert_to_int(left_edge, top_edge, length, height)
    image = images.get(path_to_image)
    image = pygame.transform.scale(image, (length, height))
    library_abstraction.window.blit(image, (left_edge, top_edge))


def render_rectangle(left_edge, top_edge, length, height, color):
    left_edge, top_edge, length, height = convert_to_int(left_edge, top_edge, length, height)
    pygame.draw.rect(library_abstraction.window, color, [left_edge, top_edge, length, height])


def set_up_window(length, height, background_color, title):
    length, height = convert_to_int(length, height)
    library_abstraction.window = pygame.display.set_mode((length, height))
    pygame.display.set_caption(title)
    library_abstraction.background_color = background_color


def key_is_pressed(keyboard_key):
    game_engine_key = keyboard_keys_to_game_engine_keys.get(keyboard_key)

    controls = pygame.key.get_pressed()
    return controls[game_engine_key]


def mouse_was_pressed():
    return pygame.mouse.get_pressed()[0]


def call_every_cycle(function):
    while True:
        start_time = time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        library_abstraction.window.fill(library_abstraction.background_color)

        function(start_time, True)
        pygame.display.update()


def is_mouse_collision(dimensions):
    area = pygame.Rect(dimensions.left_edge, dimensions.top_edge, dimensions.length, dimensions.height)
    mouse_left_edge, mouse_top_edge = pygame.mouse.get_pos()
    return area.collidepoint(mouse_left_edge, mouse_top_edge)


def get_time_passed(start_time):
    return time.time() - start_time

