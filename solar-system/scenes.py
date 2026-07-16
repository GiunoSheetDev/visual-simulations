import json
import pygame

from config import * 
from celestial_body import *


class Scene:
    def __init__(self, reference_body: CelestialBody):
        self.reference_body = reference_body
        self.origin = reference_body.position.copy()
        
        self.info : dict = None
        self.bodies : dict = None
        self.bodies_list : list = None
        
    def _load_info(self, path) -> dict:
        with open(path, "r") as file:
            data = json.load(file)

        return data[self.reference_body.name.capitalize()]

    def _calculate_system_scale(self) -> float:
        if len(self.info.values()) == 0:
            return min(SCREENW, SCREENH)

        max_distance = max(
            info["semimajor_axis_m"] * (1 + info["eccentricity"])
            for info in self.info.values()
        )
        
        return min(SCREENW, SCREENH) / (2 * max_distance)
    
    def update(self, physics_dt):
        body: CelestialBody
        for body in self.bodies.values():
            body.update_position_complex(physics_dt, self.bodies_list)
            

class PlanetScene(Scene):
    def __init__(self, reference_body):
        print(reference_body.scale_multiplier, reference_body.draw_radius)

        local_planet = CelestialBody(
            mass_kg=reference_body.mass,
            diameter_m=reference_body.diameter,
            velocity=pygame.Vector2(0, 0),
            color=reference_body.color,
            scale_multiplier=reference_body.scale_multiplier,
            draw_radius=reference_body.draw_radius,
            name=reference_body.name
        )

        local_planet.position = pygame.Vector2(0, 0)


        super().__init__(local_planet)
        self.info = self._load_info("moon_info.json")
        self.reference_body.scale = self._calculate_system_scale()
        self.bodies = self._create_moons()
        self.bodies_list = [self.reference_body] + list(self.bodies.values())
        
    def _create_moons(self) -> dict:
        out = {}

        for moon_name, info in self.info.items():
            moon = Moon(
                mass_kg=info["mass_kg"],
                diameter_m=info["diameter_m"],
                color=info["color"],
                reference_body=self.reference_body,
                draw_radius=info["draw_radius"] * self.reference_body.draw_radius * self.reference_body.scale_multiplier,
                eccentricity=info["eccentricity"],
                semimajor_axis_m=info["semimajor_axis_m"],
                name=moon_name,
            )

            moon.scale = self.reference_body.scale
            out[moon_name] = moon

        return out

    def draw(self, screen, camera_position):
        body: CelestialBody
        for body in self.bodies_list:
            if body.draw_focus(screen, camera_position, origin=self.reference_body.position) is None:
                continue
            
            if isinstance(body, MovingBody):
                return PlanetScene(body)
            
            if isinstance(body, Star):
                return SolarSystemScene(body)

class SolarSystemScene(Scene):
    def __init__(self, reference_body):
        super().__init__(reference_body)
        self.info = self._load_info("planet_info.json")
        self.reference_body.scale = self._calculate_system_scale()
        self.bodies = self._create_planets()
        self.bodies_list = [self.reference_body] + list(self.bodies.values())

    def _create_planets(self) -> dict:
        out = {}

        for planet_name, info in self.info.items():
            planet = Planet(
                mass_kg=info["mass_kg"],
                diameter_m=info["diameter_m"],
                color=info["color"],
                reference_body=self.reference_body,
                draw_radius=info["draw_radius"] * self.reference_body.draw_radius,
                eccentricity=info["eccentricity"],
                semimajor_axis_m=info["semimajor_axis_m"],
                name=planet_name,
                scale_multiplier=info["scale_multiplier"]
            )

            planet.scale = self.reference_body.scale
            out[planet_name] = planet

        return out

    def draw(self, screen, camera_position):
        body: CelestialBody
        for body in self.bodies_list:
            if body.draw_simple(screen, camera_position, origin=self.reference_body.position) is None:
                continue
            
            if isinstance(body, MovingBody):
                return PlanetScene(body)
            
            if isinstance(body, Star):
                return SolarSystemScene(body)