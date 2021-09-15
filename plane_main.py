import pygame

from plane_sprites import *

class PlaneGame(object):
    '''飞机大战主游戏'''

    def __init__(self):
        print('游戏初始化...')
        pygame.init()
        #1. 创建游戏窗口  pygame.display.set_mode((屏幕宽，高))
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #2.创建游戏时钟
        self.clock = pygame.time.Clock()
        #3.调用私有方法，精灵和精灵组
        self.__create_sprites()
        #4.设置定时器事件——创建敌机 1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 700)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):

        #创建背景精灵和精灵组
        bg1 = Background('./images/background.png')
        bg2 = Background('./images/background.png')
        bg2.rect.y = -bg2.rect.height

        self.back_group = pygame.sprite.Group(bg1, bg2)

        #创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()

        #创建精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print('游戏开始...')

        while True:
            #1设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            #2事件监听
            self.__event_handler()
            #3碰撞检测
            self.__check_collide()
            #4更新/绘制精灵组
            self.__update_sprites()
            #5更新显示
            pygame.display.update()




    #监听事件
    def __event_handler(self):

        for event in pygame.event.get():

            #判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                #print('敌机出场...')
                #创建敌机精灵
                enemy = Enemy()

                #将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)

            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

            #按键元组
            keys_pressed = pygame.key.get_pressed()
            #判断元组中对应的按键索引值 1
            if keys_pressed[pygame.K_RIGHT]:
                self.hero.speed = 2
            elif keys_pressed[pygame.K_LEFT]:
                self.hero.speed = -2
            else:
                self.hero.speed = 0


    def __check_collide(self):

        #子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

        #敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

        #判断列表是否有内容
        if len(enemies) > 0:

            #让英雄牺牲
            self.hero.kill()

            #结束游戏
            PlaneGame.__game_over()




    def __update_sprites(self):

        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print('游戏结束')

        pygame.quit()
        exit()

if __name__ == '__main__':

    #创建游戏对象
    game = PlaneGame()

    #直接在VScode里run 启动游戏
    game.start_game()
