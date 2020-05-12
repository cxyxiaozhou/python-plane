import sys
from game_stats import GameStats
import pygame
from alien import Alien
from settings import Settings
from pygame.sprite import Group
from ship import Ship
import game_functions as gf
from button import Button
from scoreboard import Socreboard
def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建Play按钮
    play_button=Button(ai_settings,screen,"Play")
    #创建一艘飞船，一个子弹编组和一个外星人编组
    ship=Ship(ai_settings,screen)
    bullets=Group()
    aliens=Group()
    
    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)
    """
    #创建一个外星人
    alien=Alien(ai_settings,screen)
    #创建一艘飞船
    ship=Ship(ai_settings,screen)
    #创建一个用于储存子弹的编组"""
    #创建一个用于储存的游戏统计信息的实列,并创建记分牌
    stats=GameStats(ai_settings)
    sb=Socreboard(ai_settings,screen,stats)
    while True:

        # for event in pygame.event.get():
            # if event.type==pygame.QUIT:
                # sys.gfexit()
        # gf.create_fleet(ai_settings,screen,ship,aliens)
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            # bullets.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
        # gf.update_screen(ai_settings,screen,ship,alien,bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()
        # pygame.display.flip()
run_game()