class GameOver(Exception):
    """Прописуем возможность запись в файл"""
    def __init__(self, player):
        super().__init__()
        self.player = player
        # sorted(player, key=lambda player: player.player_score, reverse=True)

    def save_score(self):
        with open('scores.txt', 'a+') as file:
            file.write(f'{self.player.player_name} {self.player.player_score} \n')


class EnemyDown(Exception):
    """Для выхода"""
