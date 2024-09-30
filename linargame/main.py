import os
import pygame as pg
import random 
import sys
pg.init()
pg.mixer.init(44100, -16,2,2048)
screen = pg.display.set_mode(flags= pg.FULLSCREEN)
background_image = pg.image.load("fon3.png")
damage = pg.mixer.Sound("damage.mp3")
laser = pg.mixer.Sound("laser.mp3")
laser2 = pg.mixer.Sound("laser2.mp3")
bonuss = pg.mixer.Sound("bonus.mp3")
exlposion = pg.image.load("explosion.png")
exlposion2 = pg.image.load("explosion2.png")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
GAMESPEED = 30
FPS = 60
ENEMYHP = 30
WINSIZE = screen.get_size()
PLAYERSPAWN = [WINSIZE[0] / 2,WINSIZE[1] -200]
ENEMYSPAWN = [0,0]
HP = 100
BONUSTYPE = 0
PLAYERSIZE = [100, 100]
PLAYERSPEED = GAMESPEED
BULLETSIZE = [5, 10]
BULLETSPEED = GAMESPEED / 1.5
ENEMYBULLETSPEED = GAMESPEED / 1.3
ENEMYSIZE = [100, 100]
ENEMYSPEED = GAMESPEED - GAMESPEED / 10
EXPLOSIONSIZE = [350, 250]
BACKGROUNDSIZE = [WINSIZE[0] * 1.5, WINSIZE[1] + 2000]
background_image = pg.transform.scale(background_image, BACKGROUNDSIZE)
exlposion = pg.transform.scale(exlposion, EXPLOSIONSIZE)
exlposion2 = pg.transform.scale(exlposion2, EXPLOSIONSIZE)
def main(): 
    HP = 100
    ENEMYHP = 30
    GAMESPEED = 30
    DIFFICULTY = 2
    HASGUN2 = False
    HASBOSS = False
    DAMAGE = 10
    purpose = 0
    file = open('save.txt', 'r', encoding='utf-8')
    SOUND = file.read()
    file2 = open('save2.txt', 'r', encoding='utf-8')
    strdiff = file2.read()
    if strdiff == 'easy':
        DIFFICULTY = 1
        GAMESPEED = 20
        ENEMYHP = 20
        HP = 150
    if strdiff == 'normal':
        DIFFICULTY = 2
        GAMESPEED = 30
        ENEMYHP = 30
        HP = 100
    if strdiff == 'hard':
        DIFFICULTY = 3
        GAMESPEED = 50
        ENEMYHP = 40
        HP = 50
    screen = pg.display.set_mode(WINSIZE)
    pg.font.init()
    font = pg.font.Font(None, 74)  
    button_font = pg.font.Font(None, 50)  

    def draw_text(surface, text, font, color, x, y):
        text_surface = font.render(text, True, color)
        surface.blit(text_surface, (x, y))

    def draw_button(surface, text, font, color, rect, border_color):
        pg.draw.rect(surface, border_color, rect, 2)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=rect.center)
        surface.blit(text_surface, text_rect)
    menu = True
    shop = False
    twoplayers = False
    speed = -2000
    while menu:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if start_button.collidepoint(mouse_x, mouse_y):
                    menu = False  
                if twoplayers_button.collidepoint(mouse_x, mouse_y):
                    twoplayers = True
                    menu = False  
                elif settings_button.collidepoint(mouse_x, mouse_y):
                    menu = False
                    shop = True
                elif quit_button.collidepoint(mouse_x, mouse_y):
                    pg.quit()
                    sys.exit()

        
        speed += 1
        screen.blit(background_image ,(0, speed))
        
        if speed >= -WINSIZE[1] / 4 - WINSIZE[1]/ 4.25:
            speed = -WINSIZE[1] - WINSIZE[1] / 1.1
        draw_text(screen, 'Linar Game 3000', font, WHITE, WINSIZE[0] //2.1 - 150, 100)

        start_button = pg.Rect(WINSIZE[0] // 2.1 - 100, 250, 330, 50)
        twoplayers_button = pg.Rect(WINSIZE[0] // 2.1 - 100, 350, 330, 50)
        settings_button = pg.Rect(WINSIZE[0] // 2.1 - 100, 450, 330, 50)
        quit_button = pg.Rect(WINSIZE[0] // 2.1 - 100, 550, 330, 50)

        draw_button(screen, 'One player', button_font, WHITE, start_button, WHITE)
        draw_button(screen, 'Two players', button_font, WHITE, twoplayers_button, WHITE)
        draw_button(screen, 'Settings', button_font, WHITE, settings_button, WHITE)
        draw_button(screen, 'Quit', button_font, WHITE, quit_button, WHITE)

        pg.display.update()
    while shop:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if start_button.collidepoint(mouse_x, mouse_y):
                    shop = False  
                if twoplayers_button.collidepoint(mouse_x, mouse_y):
                    twoplayers = True
                    menu = False  
                elif difficulty_button.collidepoint(mouse_x, mouse_y):
                    DIFFICULTY = DIFFICULTY + 1
                elif sounds_button.collidepoint(mouse_x, mouse_y):
                    if SOUND == 'true':
                        SOUND = 'false'
                    else:
                        SOUND = 'true'
                elif quit_button.collidepoint(mouse_x, mouse_y):
                    main()
        if DIFFICULTY > 3:
            DIFFICULTY = 1
        speed += 1
        screen.blit(background_image ,(0, speed))
        
        if speed >= -WINSIZE[1] / 4 - WINSIZE[1]/ 4.25:
            speed = -WINSIZE[1] - WINSIZE[1] / 1.1
        draw_text(screen, 'Game', font, WHITE, WINSIZE[0] // 1.83 - 150, 100)

        start_button = pg.Rect(WINSIZE[0] // 2.1 - 100, 250, 330, 50)
        twoplayers_button = pg.Rect(WINSIZE[0] // 2.1 - 100, 350, 330, 50)
        difficulty_button = pg.Rect(WINSIZE[0] // 2.1 - 100, 450, 330, 50)
        sounds_button = pg.Rect(WINSIZE[0] // 2.1 - 100, 550, 330, 50)
        quit_button = pg.Rect(WINSIZE[0] // 2.1 - 100, 650, 330, 50)
            
            
        draw_button(screen, 'One player', button_font, WHITE, start_button, WHITE)
        draw_button(screen, 'Two players', button_font, WHITE, twoplayers_button, WHITE)
        if DIFFICULTY == 1:
            draw_button(screen, 'Easy', button_font, WHITE, difficulty_button, WHITE)
            strdiff = 'easy'
            file2 = open('save2.txt', 'w+', encoding='utf-8')
            file2.write(strdiff)
            file2.close
            GAMESPEED = 20
            ENEMYHP = 20
            HP = 150
        if DIFFICULTY == 2:
            draw_button(screen, 'Normal', button_font, WHITE, difficulty_button, WHITE)
            strdiff = 'normal'
            file2 = open('save2.txt', 'w+', encoding='utf-8')
            file2.write(strdiff)
            file2.close
            GAMESPEED = 30
            ENEMYHP = 30
            HP = 100
        if DIFFICULTY == 3:
            draw_button(screen, 'Hard', button_font, WHITE, difficulty_button, WHITE)
            strdiff = 'hard'
            file2 = open('save2.txt', 'w+', encoding='utf-8')
            file2.write(strdiff)
            file2.close
            GAMESPEED = 60
            ENEMYHP = 40
            HP = 50
        if SOUND == 'true':
            draw_button(screen, 'Sounds: ON', button_font, WHITE, sounds_button, WHITE)
            file = open('save.txt', 'w+', encoding='utf-8')
            file.write(SOUND)
            file.close
        else:
            draw_button(screen, 'Sounds: OFF', button_font, WHITE, sounds_button, WHITE)
            file = open('save.txt', 'w+', encoding='utf-8')
            file.write(SOUND)
            file.close
        draw_button(screen, 'Back', button_font, WHITE, quit_button, WHITE)
        pg.display.update() 
    class Player(pg.sprite.Sprite):
        def __init__(self) :
            pg.sprite.Sprite.__init__(self)
            self.image = pg.image.load("player2.png")
            self.resized_image = pg.transform.smoothscale(self.image, (PLAYERSIZE[0] * 2, PLAYERSIZE[1] * 2 ))
            self.image2 = pg.image.load("player.png")
            self.resized_image2 = pg.transform.smoothscale(self.image2, (PLAYERSIZE[0] * 1.8, PLAYERSIZE[1] * 3 ))
            self.rect = self.rect = pg.Rect(0,0, 130, 80)
            self.rect.x = PLAYERSPAWN[0]
            self.rect.y = PLAYERSPAWN[1]
            self.hp = HP
            self.cooldown = 0
        def right(self):
            if self.rect.x >= WINSIZE[0] - PLAYERSIZE[1]: return 
            self.rect.x += PLAYERSPEED
        def left(self):
            if self.rect.x <= 0: return 
            self.rect.x -= PLAYERSPEED
    enemybullets = []
    class Boss(pg.sprite.Sprite):
        def __init__(self) :
            pg.sprite.Sprite.__init__(self)
            self.image3 = pg.image.load("enemy3.png")
            self.resized_image3 = pg.transform.smoothscale(self.image3, (PLAYERSIZE[0] * 13, PLAYERSIZE[1] * 7 ))
            self.rect = self.rect = pg.Rect(0,0, 760, 550)
            self.rect.x = WINSIZE[0] / 3
            self.rect.y = WINSIZE[1] - WINSIZE[1] / 0.9
            self.hp = 2000
            self.cooldown = 0
        def right(self):
            if self.rect.x >= WINSIZE[0] - PLAYERSIZE[1]: return 
            self.rect.x += PLAYERSPEED
        def left(self):
            if self.rect.x <= 0: return 
            self.rect.x -= PLAYERSPEED
        def shoot(self):
            if SOUND == 'true':
                laser2.play()
            enemybullets.append(EnemyBullet(self.rect.x + 50, 200))
            enemybullets.append(EnemyBullet(self.rect.x + 180, 200))
            enemybullets.append(EnemyBullet(self.rect.x + 560, 200))
            enemybullets.append(EnemyBullet(self.rect.x + 430, 200))
    class Enemy(pg.sprite.Sprite):
        def __init__(self, x, y) :  
            pg.sprite.Sprite.__init__(self)    
            self.image = pg.image.load("enemy2.png")
            self.resized_image = pg.transform.smoothscale(self.image, (ENEMYSIZE[0] * 2, ENEMYSIZE[1] * 2 ))
            self.rect = self.rect = pg.Rect(x, y, 130, 80)
            self.rect.x = random.randint(0,WINSIZE[0] - 100)
            self.rect.y = random.randint(-WINSIZE[1] ,-WINSIZE[1]  /2)
            self.hp = ENEMYHP
        def down(self):
            self.rect.y += ENEMYSPEED
        def shoot(self):
            if SOUND == 'true':
                laser2.play()
            enemybullets.append(EnemyBullet(self.rect.x, self.rect.y))
    class Bonus(pg.sprite.Sprite):
        def __init__(self, x, y) :  
            pg.sprite.Sprite.__init__(self)    
            self.image = pg.image.load("crate.jpg")
            self.resized_image = pg.transform.smoothscale(self.image, (ENEMYSIZE[0] / 2, ENEMYSIZE[1] / 2 ))
            self.rect = self.rect = pg.Rect(x, y, 100, 80)
            self.rect.x = random.randint(0,WINSIZE[0] - 100)
            self.rect.y = random.randint(-WINSIZE[1] ,-WINSIZE[1]  /2)
        def down(self):
            self.rect.y += ENEMYSPEED
    class Bullet(pg.sprite.Sprite):
        def __init__(self, x, y):
            pg.sprite.Sprite.__init__(self)
            self.image = pg.image.load("shoot.png")
            self.image2 = pg.image.load("bonusshot.png")
            self.resized_image = pg.transform.smoothscale(self.image, (PLAYERSIZE[0] / 1.5, PLAYERSIZE[1] / 1.5 ))
            self.resized_image2 = pg.transform.smoothscale(self.image2, (PLAYERSIZE[0] / 1.8, PLAYERSIZE[1] / 1.2 ))
            self.rect = self.resized_image.get_rect()
            self.rect.x = x + PLAYERSIZE[0] / 2 -1
            self.rect.y = y
        def up(self):
            self.rect.y -= BULLETSPEED
    
    class EnemyBullet(pg.sprite.Sprite):
        def __init__(self, x, y):
            pg.sprite.Sprite.__init__(self)
            self.image = pg.image.load("shoot2.png")
            self.resized_image = pg.transform.smoothscale(self.image, (ENEMYSIZE[0] / 2, ENEMYSIZE[1] * 1.7))
            self.rect = self.resized_image.get_rect()
            self.rect.x = x +ENEMYSIZE[0] / 2 -1
            self.rect.y = y
        def up(self):
            self.rect.y += ENEMYBULLETSPEED * 2

    pg.display.set_caption("Strelalka2.0")
    clock = pg.time.Clock()
    player = Player()
    boss = Boss()
    if twoplayers == True:
        player2 = Player()
    enemies = []
    bullets = []
    bonuses = []
    BACKGROUNDSPEED = 0   
    ENEMYCOOLDOWN = 0
    SPAWNCOOLDOWN = 0
    BONUSCOOLDOWN = 0
    BOSSCOOLDOWN = 0
    SCORE = 0
    game = True
    while game:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                pg.quit()
                sys.exit()              
        keys = pg.key.get_pressed() 
        if HASBOSS != True: 
            if SPAWNCOOLDOWN >20:
                SPAWNCOOLDOWN = 0
                enemies.append(Enemy(player.rect.x, player.rect.y))
            elif SPAWNCOOLDOWN >= 0:
                SPAWNCOOLDOWN += 1    
        if BONUSCOOLDOWN >250:
            BONUSCOOLDOWN = 0
            bonuses.append(Bonus(player.rect.x, player.rect.y))
        elif BONUSCOOLDOWN >= 0:
            BONUSCOOLDOWN += 1    
        if player.hp > 0:
            if keys[pg.K_a]:
                player.left()
            elif keys[pg.K_d]:
                player.right()
            if keys[pg.K_SPACE]:
                if player.cooldown >10:
                    player.cooldown = 0
                    if SOUND == 'true':
                        laser.play()
                    bullets.append(Bullet(player.rect.x, player.rect.y))
                    for bullet in bullets:
                        if bullet.rect.y < 0:    
                            bullets.pop(bullets.index(bullet))   
                elif player.cooldown >= 0:
                    player.cooldown += 1
        if twoplayers == True:
            if player2.hp > 0:
                if keys[pg.K_LEFT]:
                    player2.left()
                elif keys[pg.K_RIGHT]:
                    player2.right()
                if keys[pg.K_UP]:
                    if player2.cooldown >10:
                        player2.cooldown = 0
                        if SOUND == 'true':
                            laser.play()
                        bullets.append(Bullet(player2.rect.x, player2.rect.y))
                        for bullet in bullets:
                            if bullet.rect.y < 0:    
                                bullets.pop(bullets.index(bullet))   
                    elif player2.cooldown >= 0:
                        player2.cooldown += 1
        
            
          

        if keys[pg.K_ESCAPE]:
            main() 
        screen.blit(background_image ,(0, BACKGROUNDSPEED))
        BACKGROUNDSPEED += GAMESPEED - GAMESPEED / 3 
        if player.hp > 0:
            screen.blit(player.resized_image, (player.rect.x - 50 , player.rect.y - 15))
        if twoplayers == True:
            if player2.hp > 0:
                screen.blit(player2.resized_image2, (player2.rect.x - 40 , player2.rect.y - 55))
        for enemybullet in enemybullets:
            enemybullet.up()
            screen.blit(enemybullet.resized_image, (enemybullet.rect.x - 17 , enemybullet.rect.y +30))
            if enemybullet.rect.colliderect(player):
                if player.hp > 0:
                    player.hp = player.hp - 10
                    if SOUND == 'true':
                        damage.play()
                    screen.blit(exlposion, (player.rect.x - 110, player.rect.y - 25))
                    enemybullets.pop(enemybullets.index(enemybullet))
            if twoplayers == True:        
                if enemybullet.rect.colliderect(player2):
                    if player2.hp > 0:
                        if SOUND == 'true':
                            damage.play()
                        screen.blit(exlposion, (player2.rect.x - 110, player2.rect.y - 25))
                        enemybullets.pop(enemybullets.index(enemybullet))
                        player2.hp = player2.hp - 10
            if enemybullet.rect.y < 0:
                enemybullets.pop(enemybullets.index(enemybullet))   
        if SCORE >= 100:
            HASBOSS = True
        if HASBOSS == True:
            if boss.hp > 0:
                if ENEMYCOOLDOWN >15:
                    ENEMYCOOLDOWN = 0
                    boss.shoot()
                elif ENEMYCOOLDOWN >= 0:
                    ENEMYCOOLDOWN += 1
                if BOSSCOOLDOWN >50:
                    BOSSCOOLDOWN = 0
                    if twoplayers == True:
                        if player.hp > 0 and player2.hp > 0:
                            purpose = random.randint(1, 2)
                        elif player.hp > 0 and player2.hp <= 0:
                            purpose = 1
                        else:
                            purpose = 2
                    else:
                        purpose = 1
                elif BOSSCOOLDOWN >= 0:
                    
                    BOSSCOOLDOWN += 1
                if BOSSCOOLDOWN < 25:
                    if twoplayers == True:
                        if purpose == 1:
                            if boss.rect.x  + 370> player.rect.x:
                                boss.left()
                            else:
                                boss.right()
                        else:
                            if boss.rect.x  + 370> player2.rect.x:
                                boss.left()
                            else:
                                boss.right()
                    else:
                        if boss.rect.x  + 370> player.rect.x:
                            boss.left()
                        else:
                            boss.right()
                screen.blit(boss.resized_image3, (boss.rect.x - 285 , boss.rect.y - 15))

            for enemy in enemies:
                screen.blit(exlposion, (enemy.rect.x - 110,enemy.rect.y - 50))
                enemies.pop(enemies.index(enemy))
            if boss.hp <= 0:
                main()   
        for bullet in bullets:
            bullet.up()
            if HASGUN2 == True:
                screen.blit(bullet.resized_image2, (bullet.rect.x - 32 , bullet.rect.y - 15))
            else:
                screen.blit(bullet.resized_image, (bullet.rect.x - 32 , bullet.rect.y - 15))
            for enemy in enemies:
                if bullet.rect.colliderect(enemy):
                    if HASGUN2 == True:
                        enemy.hp = enemy.hp - (DAMAGE * 2.5)
                        screen.blit(exlposion2, (enemy.rect.x - 110,enemy.rect.y - 50))
                    else:
                        enemy.hp = enemy.hp - DAMAGE
                        screen.blit(exlposion, (enemy.rect.x - 110,enemy.rect.y - 50))
                    if SOUND == 'true':
                        damage.play()
                    bullets.pop(bullets.index(bullet))
                
                    if enemy.hp <= 0:
                        SCORE += 5
                        enemies.pop(enemies.index(enemy))  
            if boss.hp > 0:
                if HASBOSS == True:
                    if bullet.rect.colliderect(boss):
                        if HASGUN2 == True:
                            boss.hp = boss.hp - (DAMAGE * 2.5)
                            screen.blit(exlposion2, (bullet.rect.x - 160,bullet.rect.y - 90))
                        else:
                            boss.hp = boss.hp - DAMAGE
                            screen.blit(exlposion, (bullet.rect.x - 160,bullet.rect.y - 90))
                        if SOUND == 'true':
                            damage.play()
                        bullets.pop(bullets.index(bullet))

 
                      
        for enemy in enemies:
            enemy.down()
            if ENEMYCOOLDOWN >15:
                ENEMYCOOLDOWN = 0
                enemy.shoot()
            elif ENEMYCOOLDOWN >= 0:
                ENEMYCOOLDOWN += 1
            screen.blit(enemy.resized_image, (enemy.rect.x - 40 , enemy.rect.y - 15))
            if player.rect.colliderect(enemy):
                if player.hp > 0:
                    if SOUND == 'true':
                        damage.play()
                    screen.blit(exlposion, (player.rect.x - 110, player.rect.y - 25))
                    player.hp = player.hp - 10
                if twoplayers == True:
                    if player2.rect.colliderect(enemy):
                        if player2.hp > 0:
                            if SOUND == 'true':
                                damage.play()
                            screen.blit(exlposion, (player2.rect.x - 110, player2.rect.y - 25))
                            player2.hp = player2.hp - 10
            if enemy.rect.y >= WINSIZE[0] + 100:
                enemies.pop(enemies.index(enemy))   
        for bonus in bonuses:
            bonus.down()
            screen.blit(bonus.resized_image, (bonus.rect.x - 40 , bonus.rect.y - 15))
            if player.rect.colliderect(bonus):
                if player.hp > 0:
                    if SOUND == 'true':
                        laser2.stop()
                        laser.stop()
                        bonuss.play()
                    BONUSTYPE = random.randint(1, 2)
                    if BONUSTYPE == 1:
                        HASGUN2 = True
                    if BONUSTYPE == 2:
                        player.hp = player.hp + 50
                    bonuses.pop(bonuses.index(bonus))
            if twoplayers == True:
                if player2.rect.colliderect(bonus):
                    if player2.hp > 0:
                        if SOUND == 'true':
                            laser2.stop()
                            laser.stop()
                            bonuss.play()
                        BONUSTYPE = random.randint(1, 2)
                        if BONUSTYPE == 1:
                            HASGUN2 = True
                        if BONUSTYPE == 2:
                            player2.hp = player2.hp + 50
                            bonuses.pop(bonuses.index(bonus))
            if bonus.rect.y >= WINSIZE[0] + 100:
                bonuses.pop(bonuses.index(bonus))   
        if twoplayers == True: 
            if player.hp <= 0 and player2.hp <= 0:
                main() 
        else:
            if player.hp <= 0:
                main() 
        if BACKGROUNDSPEED >= -WINSIZE[1] / 4 - WINSIZE[1]/ 4.25:
            BACKGROUNDSPEED = -WINSIZE[1] - WINSIZE[1] / 1.1
        clock.tick(FPS)
        font_name = pg.font.match_font('arial')
        def draw_text(surf, text, size, x, y):
            font = pg.font.Font(font_name, size)
            text_surface = font.render(text, True, (0, 255, 0))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x, y)
            surf.blit(text_surface, text_rect)
        def draw_text2(surf, text, size, x, y):
            font = pg.font.Font(font_name, size)
            text_surface = font.render(text, True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x, y)
            surf.blit(text_surface, text_rect)
        
        draw_text(screen, str(f'score: {SCORE}'), 35, WINSIZE[0] / 2, 10)
        draw_text2(screen, str(f'player1: {player.hp}'), 35, WINSIZE[0] / 2, 60)
        if twoplayers == True:
            draw_text2(screen, str(f'player2: {player2.hp}'), 35, WINSIZE[0] / 2, 110)
        pg.display.update()
if __name__ == '__main__':
    main()
    pg.quit()   

