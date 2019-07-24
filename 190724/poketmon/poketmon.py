# $ pip install pokedex
from pokedex import pokedex
from pprint import pprint
import random

pokedex = pokedex.Pokedex(version='v1')
starting = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Pikachu']

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
        self.hp = self.level * 2
        self.exp = 0
        
        # #상세 정보 저장 
        # def hp_vs(self):
        #     return '♥'*(self.hp)

        pokemon = pokedex.get_pokemon_by_name(f'{self.poke}')[0]
        self.type = pokemon.get('types')
        self.abil = pokemon.get('abilities')

        # 시작 출력 
        print(': : 내 포켓몬의 정보 : :')
        print(f'{self.name}의 포켓몬 : {self.poke}\n레벨:{self.level}\nHP:{self.hp}')
        Game.info(self)

    def starter(self):
        mystarter = random.sample(starting,1)[0] 
        return mystarter

    def info(self):
        pokemon = pokedex.get_pokemon_by_name(f'{self.poke}')[0]
        print(f"종 : {pokemon.get('species')}\n타입 : {self.type}\n기술 : {self.abil}\n설명 : {pokemon.get('description')}\n")
        
    def __repr__(self):
        if self.hp <= 0:
            return '이미 죽은 포켓몬입니다..'
        else:
            return Game.info(self)
    
    #type calc , 타입별 데미지 증감 
    #@staticmethod
    #def poke_type():

    def fight(self,other):
        #둘다 체력 0이상일 때만 싸움 
        while self.hp >= 0 and other.hp >= 0:
            atk_turn = random.choice([1,2])
            if atk_turn == 1:
                print(f"{self.poke}가 {random.choice(list((self.abil).values()))}을(를) 써서 {other.poke}를 공격했다!")
                other.hp -= self.level * random.randint(0,3)
                print(f'{other.poke}의 HP:{other.hp}')
            elif atk_turn == 2:
                print(f"{other.poke}가 {random.choice(list((other.abil).values()))}을(를) 써서 {self.poke}를 공격했다!")
                self.hp -= other.level * random.randint(0,3)
                print(f'{self.poke}의 HP:{self.hp}')
        if self.hp > 0 and other.hp <= 0:
            print(f"{other.poke}가 주겄슴다 ㅠ {self.name}의 승리!")     
        elif self.hp <= 0 and other.hp > 0:
            print(f"{self.poke}가 주겄슴다 ㅠ {other.name}의 승리!") 
        elif self.hp < 0 and other.hp < 0:
            print(f'띠용? 둘다 죽었슴다!!')
        else:
            print('엥; 이게 나오면 안되는디;;')






P1 = input('player1의 이름을 입력하세요!: ')
P1 = Game(f'{P1}')
P2 = input('player1의 이름을 입력하세요!: ')
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




