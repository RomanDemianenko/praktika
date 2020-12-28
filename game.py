from exceptions import GameOver, EnemyDown
from models import Player, Enemy


def play():
    '''Запускаем  игру'''
    "You can see the scores result"
    player_name = input('Enter your name ')
    lvl = 1
    enemy = Enemy(lvl)
    player = Player(player_name)

    while True:

        try:
            player.attack(enemy)
            player.defence(enemy)
            # if not enemy.enemy_lives:
            #     Player.player_score += 5
        except EnemyDown:
            player.player_score += 5
            lvl += 1
            enemy = Enemy(lvl)


if __name__ == '__main__':
    try:
        play()
    except GameOver as err:
        err.save_score()
        print('Game Over')
    except KeyboardInterrupt:
        pass
    finally:
        print('Good Bye!!!')
