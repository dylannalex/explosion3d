import pygame
from explosion.constants import screen_settings, animation, colors
from explosion.screen import Explosion, Screen


def start_animation(screen, explosion, clock) -> None:
    while True:
        clock.tick(animation.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                explosion.set_particles(mx, my)
                screen.clear()
        explosion.move_particles()
        pygame.display.update()


def main():
    pygame.init()
    # Screen setup
    screen = Screen(
        screen_settings.WINDOW_TITLE,
        screen_settings.HEIGHT,
        screen_settings.WIDTH,
        screen_settings.RESIZABLE,
        colors.BLACK,
    )
    # Explosion setup
    particle_size = 1
    total_particles = 45
    x_expansion = 8
    y_expansion = 16
    explosion = Explosion(
        particle_size, total_particles, x_expansion, y_expansion, screen.window
    )

    # Start animation
    clock = pygame.time.Clock()
    start_animation(screen, explosion, clock)
    pygame.quit()


if __name__ == "__main__":
    main()
