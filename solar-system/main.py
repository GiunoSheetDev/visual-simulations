import pygame

from celestial_body import *
from scenes import *
from config import *



if __name__ == "__main__":
    screen = pygame.display.set_mode((SCREENW, SCREENH))

    camera_position = pygame.Vector2(CAMERA_POSITION)
    clock = pygame.time.Clock()

    sol = Star( mass_kg=1.9891e30,
                diameter_m=1.39095e9,
                color=(226, 146, 47),
                draw_radius=6,
                name="sol"
    )
    
    solar_system = SolarSystemScene(sol)

    current_scene = solar_system

    accumulated_sim_time = 0

    scenes_stack = [solar_system]

    is_running = True
    while is_running:
        screen.fill((0, 0, 0))
        

        current_scene = scenes_stack[-1]

        if isinstance(current_scene, SolarSystemScene):
            physics_dt = HOUR
        elif isinstance(current_scene, PlanetScene):
            physics_dt = MINUTE

        

        accumulated_sim_time += physics_dt * time_warp

        while accumulated_sim_time >= physics_dt:
            current_scene.update(physics_dt)
            accumulated_sim_time -= physics_dt

        new_scene = current_scene.draw(screen, camera_position)
        if new_scene is not None:
            scenes_stack.append(new_scene)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_running = False

                if event.key == pygame.K_RIGHT:
                    time_warp *= 10
                    time_warp = min(MAX_TIME_WARP, time_warp)

                elif event.key == pygame.K_LEFT:
                    time_warp /= 10
                    time_warp = max(MIN_TIME_WARP, time_warp)

            if pygame.mouse.get_just_pressed()[2] and len(scenes_stack) != 1:
                scenes_stack.pop()

        pygame.display.update()




