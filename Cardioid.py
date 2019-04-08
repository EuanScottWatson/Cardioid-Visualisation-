import pygame, os, math
from pygame.locals import *


class Visualise:
    def __init__(self, lines, screen, clock):
        self.lines = [[] for _ in range(lines*2)]
        self.points = []
        self.no_lines = lines

        self.add_points()
        self.add_lines(screen)

    def display(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (500, 500), 450, 1)

        for point in self.points:
            pygame.draw.circle(screen, (255, 255, 255), point, 2, 0)

        for points in self.lines:
            if len(points) > 1:
                pygame.draw.lines(screen, (255, 255, 255), False, points, 1)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return True

    def add_points(self):
        for i in range(self.no_lines):
            angle = math.pi/self.no_lines * i * 2
            x = int(500 - 450 * math.sin(angle))
            y = int(500 - 450 * math.cos(angle))
            self.points.append([x, y])

    def add_lines(self, screen):
        for i in range(self.no_lines):
            self.lines[i].append(self.points[i])
            adjoining = (i * 2) % self.no_lines
            self.lines[i].append(self.points[adjoining])

            self.display_screen(screen)

    def display_screen(self, screen):
        screen.fill((0, 0, 0))

        self.display(screen)

        pygame.display.update()
        pygame.display.flip()

    def run_logic(self):
        pass


def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Arcade Machine")

    os.environ['SDL_VIDEO_CENTERED'] = "True"

    width, height = 1000, 1000

    screen = pygame.display.set_mode((width, height))

    done = False
    clock = pygame.time.Clock()
    cardioid = Visualise(25, screen, clock)  ### Change the '25' to change how many lines you want

    while not done:
        done = cardioid.events()
        cardioid.run_logic()
        cardioid.display_screen(screen)

        clock.tick(120)


if __name__ == "__main__":
    main()
