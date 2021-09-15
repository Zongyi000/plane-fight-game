import random
import pygame

#屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 852)
#刷新帧率
FRAME_PER_SEC = 60
#创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
#英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    '''飞机大战游戏精灵'''

    def __init__(self, image_name, speed=1):
        #调用父类的初始化方法
        super().__init__()

        #定义对象的属性
        self.image = pygame.image.load(image_name)
        self.speed = speed
        self.rect = self.image.get_rect()

    def update(self):

        #屏幕的垂直方向上移动
        self.rect.y += self.speed


class Background(GameSprite):

    '''游戏背景精灵(子类，因为父类无法满足需求)'''

    def update(self):

        #调用父类的方法实现
        super().update()

        #判断是否移除屏幕，若移除则转移到屏幕上方
        if self.rect.y > SCREEN_RECT.height:
            self.rect.y = -self.rect.height

class Enemy(GameSprite):

    def __init__(self):

        #调用父类方法，创建敌机精灵，指定敌机图片
        super().__init__('./images/mabaoguo3.png')

        #指定敌机初始速度 1-3
        self.speed = random.randint(3, 10)

        #指定敌机初始随机位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):

        #调用父类方法, 保持垂直飞行
        super().update()
        #判断飞出屏幕则从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:

            #kill将精灵从精灵组移除销毁
            self.kill()



class Hero(GameSprite):
    '''英雄精灵'''

    def __init__(self):
        #调用父类方法，设置image/speed
        super().__init__('./images/cxk4.png', 0)
        #设置英雄初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        #创建子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):

        #英雄在水平方向移动
        self.rect.x += self.speed

        #控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        #print('发射子弹...')

        for i in (0, 1):
            #创建子弹精灵
            bullet = Bullet()

            #设置精灵位置
            bullet.rect.bottom = self.rect.y - i * 70
            bullet.rect.centerx = self.rect.centerx

            #将精灵添加到精灵组
            self.bullets.add(bullet)


class Bullet(GameSprite):
    '''子弹精灵'''

    def __init__(self):

        #调用父类，设置子弹图片，设置初始速度
        super().__init__('./images/lq4.png', -5)


    def update(self):

        #调用父类，让子弹垂直方向飞行
        super().update()

        #判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()





