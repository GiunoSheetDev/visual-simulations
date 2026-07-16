import pygame
import math

from config import *
from button import Button


class CelestialBody:
    def __init__(self,  
                mass_kg: int = 0,
                diameter_m: int = 0,
                velocity: pygame.Vector2 = None,
                color: tuple[int] = (255, 255, 255),
                name: str = None,
                draw_radius: int = 1,
                scale_multiplier: int = 1):
        
        self.mass = mass_kg
        self.diameter = diameter_m
        self.color = color
        self.scale_multiplier = scale_multiplier
        
        self.position = pygame.Vector2(0, 0)
        self.velocity = velocity
        self.draw_radius = draw_radius

        self.name = name
        self.button = None
        
    def draw_simple(self, screen, camera_position, origin=pygame.Vector2(0, 0)) -> None:
        relative_position = self.position - origin

        self.screen_position = relative_position * self.scale
        self.screen_position += camera_position

        if self.button is not None and self.button.draw(screen):
            return self
        

        pygame.draw.circle(screen, self.color, self.screen_position, self.draw_radius)

    def draw_focus(self, screen, camera_position, origin=pygame.Vector2(0, 0)) -> None:
        relative_position = self.position - origin

        self.screen_position = relative_position * self.scale
        self.screen_position += camera_position

        if self.button is not None and self.button.draw(screen):
            return self
        

        pygame.draw.circle(screen, self.color, self.screen_position, self.draw_radius * self.scale_multiplier)

class Star(CelestialBody):
    def __init__(self, mass_kg=0, diameter_m=0, velocity = pygame.Vector2(0, 0), color = (255, 255, 255), draw_radius: int = 1, name: str = None, scale_multiplier: int = 1):
        super().__init__(mass_kg=mass_kg,
                        diameter_m=diameter_m, 
                        velocity=velocity, 
                        color=color, 
                        draw_radius=draw_radius, 
                        name=name,
                        scale_multiplier=scale_multiplier)
        
        

class MovingBody(CelestialBody):
    def __init__(
            self, 
            mass_kg = 0, 
            diameter_m = 0, 
            velocity = None, 
            color = (255, 255, 255), 
            name = None, 
            draw_radius = 1,
            eccentricity: float = 0,
            semimajor_axis_m : int = 0,
            reference_body: CelestialBody = None,
            scale_multiplier: int = 1):
        super().__init__(mass_kg=mass_kg, 
                        diameter_m=diameter_m, 
                        velocity=velocity, 
                        color=color, 
                        name=name, 
                        draw_radius=draw_radius,
                        scale_multiplier=scale_multiplier
                        )

        self.eccentricity = eccentricity
        self.semimajor_axis_m = semimajor_axis_m

        periapsis = self.semimajor_axis_m * (1 - self.eccentricity)
        self.position = pygame.Vector2(0, periapsis)

        self.reference_body = reference_body

        if velocity is None:
            a = self.semimajor_axis_m
            e = self.eccentricity

            periapsis = a * (1 - e)

            r = periapsis

            speed = math.sqrt(
                G * self.reference_body.mass * (2/r - 1/a)
            )

            radius_direction = pygame.Vector2(0, 1)
            tangent_direction = pygame.Vector2(-radius_direction.y, radius_direction.x)

            self.position = (
                self.reference_body.position + radius_direction * periapsis
            )

            self.velocity = (
                self.reference_body.velocity + tangent_direction * speed
            )

    def update_position_simple(self, physics_dt: float) -> None:
        distance_vector = self.reference_body.position - self.position
        distance = distance_vector.length()
        direction = distance_vector.normalize()

        acceleration = direction * (
        G * self.reference_body.mass / (distance ** 2))

        self.velocity += acceleration * (physics_dt / 2)
        self.position += self.velocity * physics_dt

        distance_vector = self.reference_body.position - self.position
        distance = distance_vector.length()
        direction = distance_vector.normalize()

        acceleration = direction * (
        G * self.reference_body.mass / (distance ** 2))

        self.velocity += acceleration * (physics_dt / 2)

    def update_position_complex(self, physics_dt: float, celestial_bodies: list[CelestialBody]) -> None:
        
        def calculate_acceleration():
            total_acceleration = pygame.Vector2(0, 0)

            for body in celestial_bodies:
                if body == self:
                    continue

                distance_vector = body.position - self.position
                distance = distance_vector.length()

                if distance == 0:
                    continue

                direction = distance_vector.normalize()

                acceleration = direction * (
                    G * body.mass / (distance ** 2)
                )
        
                total_acceleration += acceleration
            
            return total_acceleration

        acceleration = calculate_acceleration()
        self.velocity += acceleration * (physics_dt / 2)

        self.position += self.velocity * physics_dt

        acceleration = calculate_acceleration()
        self.velocity += acceleration * (physics_dt / 2)

class Planet(MovingBody):
    def __init__(self, mass_kg=0, diameter_m=0, velocity=None, color=(255, 255, 255), name=None, draw_radius=1, eccentricity = 0, semimajor_axis_m = 0, reference_body = None, scale_multiplier: int = 1):
        super().__init__(mass_kg=mass_kg, 
                        diameter_m=diameter_m, 
                        velocity=velocity, 
                        color=color, 
                        name=name, 
                        draw_radius=draw_radius, 
                        eccentricity=eccentricity, 
                        semimajor_axis_m=semimajor_axis_m, 
                        reference_body=reference_body,
                        scale_multiplier=scale_multiplier)
        
        self.button = Button(self)

class Moon(MovingBody):
    def __init__(self, mass_kg=0, diameter_m=0, velocity=None, color=(255, 255, 255), name=None, draw_radius=1, eccentricity = 0, semimajor_axis_m = 0, reference_body = None):
        super().__init__(mass_kg=mass_kg, 
                        diameter_m=diameter_m, 
                        velocity=velocity, 
                        color=color, 
                        name=name, 
                        draw_radius=draw_radius, 
                        eccentricity=eccentricity, 
                        semimajor_axis_m=semimajor_axis_m, 
                        reference_body=reference_body,
                        )


