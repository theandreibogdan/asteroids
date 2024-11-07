import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from bullet import Bullet
from asteroidfrield import AsteroidField

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    AsteroidField.containers = updatable
    Asteroid.containers = (asteroids, updatable, drawable)
    Bullet.containers = (bullets, updatable, drawable)
    Player.containers = (updatable, drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x,y)
    asteroid_field = AsteroidField()
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("black")

        for update in updatable:
            update.update(dt)
        
        for draw in drawable:
            draw.draw(screen)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()
            
            for bullet in bullets:
                if bullet.collision(asteroid):
                    bullet.kill()
                    asteroid.split()
        

        pygame.display.flip()
    
        dt = clock.tick(60) / 1000


    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()