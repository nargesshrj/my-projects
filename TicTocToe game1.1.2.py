import pygame
import sys
import random

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
YELLOW = (255, 200, 0)
GREEN = (0, 255, 150)

# نشانه‌های بازیکن و هوش مصنوعی
PLAYER_MARKER = 'X'
AI_MARKER = 'O'

class TicTacToe:
    def __init__(self):
        self.board = [['' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.current_player = PLAYER_MARKER
        self.winner = None
        self.current_color = (255, 255, 255)
        self.target_color = self.get_random_color()

    def draw_board(self):
        # تغییر رنگ پس زمینه به صورت نرم
        self.current_color = self.lerp_color(self.current_color, self.target_color, 0.01)
        screen.fill(self.current_color)

        for row in range(1, BOARD_SIZE):
            pygame.draw.line(screen, BLACK, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
            pygame.draw.line(screen, BLACK, (row * SQUARE_SIZE, 0), (row * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        self.draw_markers()

    def draw_markers(self):
        # رسم نشان‌های X و O
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self.board[row][col] == 'X':
                    pygame.draw.line(screen, RED, (col * SQUARE_SIZE + 20, row * SQUARE_SIZE + 20),
                                     (col * SQUARE_SIZE + SQUARE_SIZE - 20, row * SQUARE_SIZE + SQUARE_SIZE - 20), LINE_WIDTH)
                    pygame.draw.line(screen, RED, (col * SQUARE_SIZE + SQUARE_SIZE - 20, row * SQUARE_SIZE + 20),
                                     (col * SQUARE_SIZE + 20, row * SQUARE_SIZE + SQUARE_SIZE - 20), LINE_WIDTH)
                elif self.board[row][col] == 'O':
                    pygame.draw.circle(screen, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 20, LINE_WIDTH)

        # مکان نشان ها
    def place_marker(self, row, col):
        if self.board[row][col] == '' and not self.winner:
            self.board[row][col] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
            self.current_player = AI_MARKER if self.current_player == PLAYER_MARKER else PLAYER_MARKER
            if not self.winner and not self.is_draw() and self.current_player == AI_MARKER: # فقط اگر بازی تمام نشده و نوبت هوش مصنوعی بود، حرکت کند
                row, col = self.ai_move(self.board)
                self.board[row][col] = AI_MARKER
                if self.check_winner():
                    self.winner = AI_MARKER
                self.current_player = PLAYER_MARKER

    def check_winner(self):
        # ... کد بررسی برنده
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
    
    def is_draw(self):
        # بررسی تساوی بازی
        for row in self.board:
            if '' in row:
                return False
        return not self.winner

    def get_random_color(self):
        # تولید رنگ تصادفی
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    def lerp_color(self, current, target, t):
        # تغییر نرم رنگ با جلوگیری از خروج از محدوده RGB
        return tuple(max(0, min(255, int(current[i] + (target[i] - current[i]) * t))) for i in range(3))
    
    def reset_game(self):
        # ریست بازی
        self.board = [['' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.current_player = 'X'
        self.winner = None
        self.target_color = self.get_random_color()

        # کد بازی با هوش مصنوعی بااستفاده از الگوریتم Minimax
    def ai_move(self, board):
        best_score = -float('inf')
        best_move = None

        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if board[row][col] == '':
                    board[row][col] = AI_MARKER
                    score = self.minimax(board, 0, False)
                    board[row][col] = '' # بازگرداندن خانه به حالت خالی (خیلی مهم!)
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)

        return best_move

    def minimax(self, board, depth, is_maximizing):
        if self.check_winner_for_minimax(board, PLAYER_MARKER): # اگر بازیکن برده
            return -1
        if self.check_winner_for_minimax(board, AI_MARKER): # اگر هوش مصنوعی برده
            return 1
        if self.is_draw_for_minimax(board): # اگر بازی مساوی شده
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for row in range(BOARD_SIZE):
                for col in range(BOARD_SIZE):
                    if board[row][col] == '':
                        board[row][col] = AI_MARKER
                        score = self.minimax(board, depth + 1, False)
                        board[row][col] = ''
                        best_score = max(score, best_score)
            return best_score
        else: # minimizing player
            best_score = float('inf')
            for row in range(BOARD_SIZE):
                for col in range(BOARD_SIZE):
                    if board[row][col] == '':
                        board[row][col] = PLAYER_MARKER
                        score = self.minimax(board, depth + 1, True)
                        board[row][col] = ''
                        best_score = min(score, best_score)
            return best_score

    def check_winner_for_minimax(self, board, player):
        for i in range(BOARD_SIZE):
            if board[i][0] == board[i][1] == board[i][2] == player:
                return True
            if board[0][i] == board[1][i] == board[2][i] == player:
                return True
        if board[0][0] == board[1][1] == board[2][2] == player:
            return True
        if board[0][2] == board[1][1] == board[2][0] == player:
            return True
        return False
    
    def is_draw_for_minimax(self, board):
        for row in board:
            if '' in row:
                return False
        return True


# بازی اصلی
def main():
    clock = pygame.time.Clock()
    game = TicTacToe()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not game.winner and not game.is_draw():
                x, y = event.pos
                col = x // SQUARE_SIZE
                row = y // SQUARE_SIZE
                game.place_marker(row, col)
            elif game.winner or game.is_draw():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    game.reset_game()

        # حرکت هوش مصنوعی
        if game.current_player == 'O' and not game.winner and not game.is_draw():
            game.ai_move()

        # به‌روزرسانی و رسم صفحه
        color_distance = sum((game.current_color[i] - game.target_color[i]) ** 2 for i in range(3)) ** 0.5
        if color_distance < 5:
            game.target_color = game.get_random_color()

        game.draw_board()

        # نمایش پیام برنده یا تساوی
        if game.winner:
            font = pygame.font.SysFont(None, 48)
            text = font.render(f'Player {game.winner} wins!', True, GREEN)
            screen.blit(text, (WIDTH // 5, HEIGHT // 2))
        elif game.is_draw():
            font = pygame.font.SysFont(None, 48)
            text = font.render('Game is a draw!', True, GREEN)
            screen.blit(text, (WIDTH // 5, HEIGHT // 2))

        if game.winner or game.is_draw():
            font = pygame.font.SysFont(None, 24)
            restart_text = font.render('Press R to restart', True, YELLOW)
            screen.blit(restart_text, (WIDTH // 4, HEIGHT // 1.5))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()
if __name__ == "__main__":
    main()