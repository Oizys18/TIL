# $ pip install pokedex.py 
# -*- encoding = uft-8 -*-

from pokedex import pokedex
from pprint import pprint
import random
import tkinter as tk
from PIL import ImageTk, Image
import os
import requests
from io import BytesIO
import time

# import Tkinter
# import tkinter.messagebox
# from tkinter import ttk

# window = Tkinter.Tk()
    

#     #centre screen message
#     window.geometry("1x1+"+str(window.winfo_screenwidth()/2)
#                     +"+"+str(window.winfo_screenheight()/2))
#     tkMessageBox.showinfo(title=" ", message=" ")

print("""               888                                           
                        888                                           
                        888                                           
        88888b.  .d88b. 888  888 .d88b. 88888b.d88b.  .d88b. 88888b.  
        888 "88bd88""88b888 .88Pd8P  Y8b888 "888 "88bd88""88b888 "88b 
        888  888888  888888888K 88888888888  888  888888  888888  888 
        888 d88PY88..88P888 "88bY8b.    888  888  888Y88..88P888  888 
        88888P"  "Y88P" 888  888 "Y8888 888  888  888 "Y88P" 888  888 
        888                                                           
        888                                                           
        888 """)
print("""
                 ."-,.__
                 `.     `.  ,
              .--'  .._,'"-' `.
             .    .'         `'
             `.   /          ,'
               `  '--.   ,-"'
                `"`   |  \\
                   -. \\, |
                    `--Y.'      ___.
                         \\     L._, \\
               _.,        `.   <  <\\                _
             ,' '           `, `.   | \\            ( `
          ../, `.            `  |    .\\`.           \\ \\_
         ,' ,..  .           _.,'    ||\\l            )  '".
        , ,'   \\           ,'.-.`-._,'  |           .  _._`.
      ,' /      \\ \\        `' ' `--/   | \\          / /   ..\\
    .'  /        \\ .         |\\__ - _ ,'` `        / /     `.`.
    |  '          ..         `-...-"  |  `-'      / /        . `.
    | /           |L__           |    |          / /          `. `.
   , /            .   .          |    |         / /             ` `
  / /          ,. ,`._ `-_       |    |  _   ,-' /               ` \\
 / .           \\"`_/. `-_ \\_,.  ,'    +-' `-'  _,        ..,-.    \\`.
  '         .-f    ,'   `    '.       \\__.---'     _   .'   '     \\ \\
' /          `.'    l     .' /          \\..      ,_|/   `.  ,'`     L`
|'      _.-""` `.    \\ _,'  `            \\ `.___`.'"`-.  , |   |    | \\
||    ,'      `. `.   '       _,...._        `  |    `/ '  |   '     .|
||  ,'          `. ;.,.---' ,'       `.   `.. `-'  .-' /_ .'    ;_   ||
|| '              V      / /           `   | `   ,'   ,' '.    !  `. ||
||/            _,-------7 '              . |  `-'    l         /    `||
 |          ,' .-   ,' ||               | .-.        `.      .'     ||
 `'        ,'    `".'    |               |    `.        '. -.'       `'
          /      ,'      |               |,'    \\-.._,.'/'
          .     /        .               .       \\    .''
        .`.    |         `.             /         :_,'.'
          \\ `...\\   _     ,'-.        .'         /_.-'
           `-.__ `,  `'   .  _.>----''.  _  __  /
                .'        /"'          |  "'   '_
               /_|.-'\\ ,".             '.'`__'-( \\
                 / ,"'"\\,'               `/  `-.|" mh""")

pokedex = pokedex.Pokedex(version='v1')
starting = ['Bulbasaur', 'Charmander', 'Squirtle', 'Pikachu']

# game 클래스 
class Game:
    player_Dict = {}
    def __init__(self,name): 
        self.name = name
        self.poke = Game.starter(self)

        # 플레이어 프로필 저장 
        Game.player_Dict[self.name] = self.poke

        # 기본설정 
        self.level = 5
        self.hp = self.level * 15
        self.exp = 0

        # 상세 정보
        pokemon = pokedex.get_pokemon_by_name(f'{self.poke}')[0]
        self.type = pokemon.get('types')
        self.abil = pokemon.get('abilities')

        # 시작 출력 
        print(': : 내 포켓몬의 정보 : :\n')
        print(f'{self.name}의 포켓몬 : {self.poke}\n레벨:{self.level}\nHP:{self.hp}\n')
        Game.info(self)
        Game.paint(self)

    #starting poketmon 정하기 
    def starter(self):
        mystarter = random.sample(starting,1)[0] 
        return mystarter

    # 정보출력 함수 
    def info(self):
        pokemon = pokedex.get_pokemon_by_name(f'{self.poke}')[0]
        print(f"종 : {pokemon.get('species')}\n타입 : {self.type}\n기술 : {self.abil}\n설명 : {pokemon.get('description')}\n")
    
    # 포켓몬 부르기 
    def __repr__(self):
        if self.hp <= 0:
            return '이미 죽은 포켓몬입니다..'
        else:
            return Game.info(self)

    # 포켓몬 사진 출력     
    def paint(self):
        root = tk.Tk()
        img_url = str(pokedex.get_pokemon_by_name(f'{self.poke}')[0].get('sprite'))
        response = requests.get(img_url)
        img_data = response.content
        img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
        panel = tk.Label(root, image=img)
        panel.pack(side="bottom", fill="both", expand="yes")
        def close_window ():
            root.destroy()
        button = tk.Button(text = "Click and Quit", command = close_window)
        button.pack()

        root.mainloop()
        
#상세 정보 저장 
    def hp_vs(self):
        return '♥'*int(self.hp/10)

    #type calc , 타입별 데미지 증감 
    #@staticmethod
    #def poke_type():
    def skillDamage(self):
        skill_type, skill_name = random.choice(list((self.abil).items()))
        if skill_type == 'normal':
            damageX = random.randint(1,3)            
        elif skill_type == 'hidden':
            damageX = random.randint(3,6)
        return skill_name,damageX


    def fight(self,other):
        #둘다 체력 0이상일 때만 싸움 
        while self.hp > 0 and other.hp > 0:
            atk_turn = random.choice([self.name,other.name])
            
            # P1 atk_turn
            if atk_turn == self.name:
                print(f"{self.name}의 턴! 가라 {self.poke}!\n")
                p1skill,p1DamageX = Game.skillDamage(self) 
                print(f"{self.poke}가 {p1skill}을(를) 써서 {other.poke}를 공격했다!\n")
                other.hp -= self.level * p1DamageX
                
                print(f"{other.name}의 반격! 가라 {other.poke}!\n")
                p2skill,p2DamageX = Game.skillDamage(other) 
                print(f"{other.poke}가 {p2skill}을(를) 써서 {self.poke}를 공격했다!\n")
                self.hp -= other.level * p2DamageX

            # P2 atk_turn 
            elif atk_turn == other.name:
                print(f"{other.name}의 턴! 가라 {other.poke}!\n")
                p2skill,p2DamageX = Game.skillDamage(other) 
                print(f"{other.poke}가 {p2skill}을(를) 써서 {self.poke}를 공격했다!\n")
                self.hp -= other.level * p2DamageX

                print(f"{self.name}의 반격! 가라 {self.poke}!\n")
                p1skill,p1DamageX = Game.skillDamage(self) 
                print(f"{self.poke}가 {p1skill}을(를) 써서 {other.poke}를 공격했다!\n")
                other.hp -= self.level * p1DamageX

            # P1 & P2 hp 표시 
            print(f'\n{self.name}의 {self.poke}\n HP:{self.hp} {Game.hp_vs(self)}')
            print(f'{other.name}의 {other.poke}\n HP:{other.hp} {Game.hp_vs(other)}\n')
        
            # time delay 주기 : 2초
            time.sleep(2)

        if self.hp > 0 and other.hp <= 0:
            print(f"{other.name}의 {other.poke}가 주겄슴다 ㅠ {self.name}의 승리!")     
        elif self.hp <= 0 and other.hp > 0:
            print(f"{self.name}의 {self.poke}가 주겄슴다 ㅠ {other.name}의 승리!") 

        #이하 미구현
        elif self.hp < 0 and other.hp < 0:
            print(f'띠용? 둘다 죽었슴다!!')
        else:
            print('엥; 이게 나오면 안되는디;; 에러임당!')


P1 = input('player1의 이름을 입력하세요!: ')
P1 = Game(f'{P1}')
P2 = input('player2의 이름을 입력하세요!: ')
P2 = Game(f'{P2}')

Game.fight(P1,P2)


# class Poke(Game):
#     def __init__(self,name):
#         super().__init__(self)
#         self.poke = Game.starter(self)
#         self.level = 5
#         self.hp = self.level * 20 
#         self.exp = 0

#     def pkhp(self):
#         if self:
#             if self.hp <= 0:
#                 print(f'{self.poke}이(가) 비명을 지릅니다!')
#                 self.__del__()
#             else:
#                 print(f'{self.poke}의 hp : {self.hp}')

#     # def pklevel(self):
#     #     pass

#     def __del__(self):
#         print(f'{self.poke}가 죽었슴다 ㅡㅠ;')
    
#     def __repr__(self):
#         if self.hp <= 0:
#             return '이미 죽은 포켓몬입니다..'
#         else:
#             return super().info()

#     def attack(self,other):
#         other.hp -= self.level * 5





# # Initialise Pygame + Clock

# pygame.init()
# mainClock = pygame.time.Clock()

# # Window Setup

# WINDOWHEIGHT = 480
# WINDOWWIDTH = 600
# windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
# pygame.display.set_caption('Pokemon')

# # Player Variables

# player = pygame.Rect(20, 20, 20, 20)
# # Movement Variables

# moveLEFT = False
# moveRIGHT = False
# moveUP = False
# moveDOWN = False

# MOVESPEED = 7

# x,y = 0,0
# charx,chary = 0,0
# movex,movey = 0,0

# # Colour Setup
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# BLUE = (0, 0, 255)
# GREEN = (0, 255, 0)

# # keyboard input
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#         # Change the keyboard variables
#         if event.type == KEYDOWN:
#             if event.key == K_LEFT or event.key == ord('a'):
#                 moveLEFT = True
#             elif event.key == K_RIGHT or event.key == ord('d'):
#                 moveRIGHT = True
#             elif event.key == K_UP or event.key == ord('w'):
#                 moveUP = True
#             elif event.key == K_DOWN or event.key == ord('s'):
#                 moveDOWN = True
#         elif event.type == KEYUP:
#             if event.key == K_ESCAPE:
#                 pygame.quit()
#                 sys.exit()
#             elif event.key == K_LEFT or event.key == ord('a'):
#                 moveLEFT = False
#             elif event.key == K_RIGHT or event.key == ord('d'):
#                 moveRIGHT = False
#             elif event.key == K_UP or event.key == ord ('w'):
#                 moveUP = False
#             elif event.key == K_DOWN or event.key == ord('s'):
#                 moveDOWN = False
#             elif event.key == K_SPACE:
#                 name = input("이름 입력! ")
#                 name = Game(name)

#          # <-- Dedent

#     # Background Setup
#     windowSurface.fill(WHITE)
#     # Player Setup + Updating Screen
#     if moveDOWN and player.bottom < WINDOWHEIGHT:
#         player.top += MOVESPEED
#     if moveUP and player.top > 0:
#         player.top-= MOVESPEED
#     if moveLEFT and player.left > 0:
#         player.left -= MOVESPEED
#     if moveRIGHT and player.right < WINDOWWIDTH:
#         player.right += MOVESPEED
#     pygame.draw.rect(windowSurface, GREEN, player)
#     pygame.display.update()
#     mainClock.tick(40)




