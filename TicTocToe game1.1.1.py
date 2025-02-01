import pygame
import sys

# مقداردهی اولیه 
pygame.init()

# تنظیمات صفحه
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 10
BOARD_SIZE = 3
SQUARE_SIZE = WIDTH // BOARD_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# رنگ‌ها
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW =(255,200,0)
GREEN =(0,255,150)

# بازی
class TicTacToe:
    def __init__(self):
        self.board = [['' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        #for _ in range(BOARD_SIZE):
        #   for _ in range(BOARD_SIZE):
        #       print("")
        self.current_player = 'X'
        self.winner = None


    def draw_board(self):
        screen.fill(YELLOW)
        for row in range(1, BOARD_SIZE):
            pygame.draw.line(screen, BLACK, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
            pygame.draw.line(screen, BLACK, (row * SQUARE_SIZE, 0), (row * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        self.draw_markers()

    def draw_markers(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self.board[row][col] == 'X':
                    pygame.draw.line(screen, RED, (col * SQUARE_SIZE + 20, row * SQUARE_SIZE + 20),
                                     (col * SQUARE_SIZE + SQUARE_SIZE - 20, row * SQUARE_SIZE + SQUARE_SIZE - 20), LINE_WIDTH)
                    pygame.draw.line(screen, RED, (col * SQUARE_SIZE + SQUARE_SIZE - 20, row * SQUARE_SIZE + 20),
                                     (col * SQUARE_SIZE + 20, row * SQUARE_SIZE + SQUARE_SIZE - 20), LINE_WIDTH)
                elif self.board[row][col] == 'O':
                    pygame.draw.circle(screen, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 20, LINE_WIDTH)

    def place_marker(self, row, col):
        if self.board[row][col] == '' and not self.winner:
            self.board[row][col] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        # بررسی سطرها و ستون‌ها
        for i in range(BOARD_SIZE):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return True
        # بررسی قطرها
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        return False

# بازی اصلی
def main():
    clock = pygame.time.Clock()
    game = TicTacToe()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                col = x // SQUARE_SIZE
                row = y // SQUARE_SIZE
                game.place_marker(row, col)

        game.draw_board()
        if game.winner:
            font = pygame.font.SysFont(None, 48)
            text = font.render(f'Player {game.winner} wins!', True, GREEN)
            screen.blit(text, (WIDTH // 5, HEIGHT //2))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()



