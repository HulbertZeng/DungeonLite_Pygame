import pygame
import math
import random
from levels import start, easy, medium, hard, expert, extreme
from player import player, projectile
from enemy import enemy

if __name__ == '__main__':
    #set up levels
    levels = 0
    difficulty = start()
    if difficulty == '1':
        levels = easy
    elif difficulty == '2':
        levels = medium
    elif difficulty == '3':
        levels = hard
    elif difficulty == '4':
        levels = expert
    else:
        levels = extreme

    #set up background
    pygame.init()
    screen = pygame.display.set_mode((600, 600), pygame.FULLSCREEN)
    pygame.display.set_caption("DungeonLite")
    floor = pygame.image.load('images/dungeonFloor.png')

    #set up characters
    person = player(10, 300)
    demons = levels.pop(0)
    font = pygame.font.SysFont('comicsans', 30, True)
    total_score = 0
    lvl = 1

    def redraw(curr_level, curr_score):
        #update background, level, and score
        score = 0
        screen.blit(floor, (0,0))
        score_text = font.render('Score: ' + str(curr_score), 1, (255, 0, 0))
        screen.blit(score_text, (450, 10))
        level_text = font.render('Level: ' + str(curr_level), 1, (255, 0, 0))
        screen.blit(level_text, (20, 10))

        #update player position and health bar
        pygame.draw.rect(screen, (255, 0, 0), (person.x - 5, person.y - 20, 60, 10))
        pygame.draw.rect(screen, (0, 255, 0), (person.x - 5, person.y - 20, 60 - (.5 * (120 - person.health)), 10))
        if person.left:
            screen.blit(person.left_img, (person.x, person.y))
        if person.right:
            screen.blit(person.right_img, (person.x, person.y))

        #update check for player attack
        person.fireSpell(pygame, screen)

        #demon interactions
        for demon in demons[:]:
            if person.fired:
                for s in person.spell:
                    if demon.x < s.x + 21 < demon.x + demon.width and demon.y < s.y + 21 < demon.y + demon.height:
                        demon.health -= person.attack
                        score += 10
                        person.spell.remove(s)
                    if len(person.spell) == 0:
                        person.fired = False
                        break
                if demon.health <= 0:
                    score += 10
                    screen.blit(demon.explode_img, (demon.x, demon.y))
                    demons.remove(demon)
                    if random.randint(0, 60) == 0:
                        person.fireLimit += 1
            if not demon.dist:
                demon.follow(person.x, person.y)
                if person.x - 20 < demon.x + 40 < person.x + 70 and person.y - 20 < demon.y + 35 < person.y + 84:
                    screen.blit(demon.attack_img, (person.x, person.y))
                    score -= 15
                    person.health -= demon.attack
            pygame.draw.rect(screen, (255, 0, 0), (demon.x - 5, demon.y - 20, 60, 10))
            pygame.draw.rect(screen, (0, 255, 0), (demon.x - 5, demon.y - 20, 60 - ((2/3) * (90 - demon.health)), 10))
            demon.update(screen)

        pygame.display.update()
        return score

    run = True
    while run:
        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.blit
        person.move()
        total_score += redraw(lvl, total_score)
        if person.health <= 0:
            print('You have been slain...')
            run = False

        if len(demons) == 0 and lvl != 6:
            lvl += 1
            demons = levels.pop(0)
        elif len(demons) == 0 and len(levels) == 0:
            print('All demons have been slain. You win')
            run = False
    print('Highest level reached: ' + str(lvl))
    print('Your score: ' + str(total_score))
    pygame.quit()

