import pygame

from Game import Game
from network import Network
import pickle
from Board import Board

pygame.font.init()

width = 700
height = 700
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


class Checkers:
    def __init__(self, win):
        self.win = win
        self.run = True


def _draw(board):
    board.draw(win)
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = int(n.getP())
    board_size = 8
    tile_width, tile_height = 700 // board_size, 700 // board_size
    board = Board(tile_width, tile_height, board_size)
    games = Game(2)
    print("You are player", player)

    while run:
        clock.tick(60)
        games.check_jump(board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if not games.is_game_over(board):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    board.handle_click(event.pos)
            else:
                games.message()
                run = False

        _draw(board)


def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        win.fill((128, 128, 128))
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Click to Play!", 1, (255, 0, 0))
        win.blit(text, (100, 200))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()


while True:
    menu_screen()
