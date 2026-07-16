import pygame
from config import *




class Button:
    def __init__(self, body):
        self.body = body
        self.draw_radius = self.body.draw_radius
        self.screen_position = pygame.Vector2(0, 0)
        self.rect = pygame.Rect(self.screen_position.x - self.draw_radius//2, 
                                self.screen_position.y - self.draw_radius//2, 
                                self.draw_radius + 10 , self.draw_radius + 10)
        
        self.clicked = False

    def update_position(self) -> None:
        self.screen_position = self.body.screen_position.copy()
        self.rect.center = self.screen_position

    def draw(self, screen) -> None:
        self.update_position()
        action = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False


        pygame.draw.rect(screen, (255, 0, 0), self.rect, width=1)

        return action
