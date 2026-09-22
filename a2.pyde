
import random

# =========================
# GAME SETTINGS
# =========================

ROWS = 5
COLS = 5

CELL_SIZE = 65
CELL_GAP = 5

OFFSET_X = 37
OFFSET_Y = 100

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 480


# =========================
# GAME VARIABLES
# =========================

grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

moves = 0
game_over = False


# =========================
# SETUP
# =========================

def setup():
    size(WINDOW_WIDTH, WINDOW_HEIGHT)
    reset_game()


# =========================
# RESET GAME
# =========================

def reset_game():
    global grid, moves, game_over

    grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

    moves = 0
    game_over = False

    # Create a random puzzle
    for _ in range(12):
        r = random.randint(0, ROWS - 1)
        c = random.randint(0, COLS - 1)

        toggle_cell(r, c)


# =========================
# TOGGLE CELL
# =========================

def toggle_cell(r, c):

    targets = [
        (r, c),
        (r - 1, c),
        (r + 1, c),
        (r, c - 1),
        (r, c + 1)
    ]

    for row, col in targets:

        if 0 <= row < ROWS and 0 <= col < COLS:
            grid[row][col] = 1 - grid[row][col]


# =========================
# CHECK WIN
# =========================

def check_win():

    for r in range(ROWS):
        for c in range(COLS):

            if grid[r][c] == 1:
                return False

    return True


# =========================
# DRAW
# =========================

def draw():

    background(15, 23, 42)

    draw_title()
    draw_grid()

    if game_over:
        draw_win_screen()


# =========================
# TITLE
# =========================

def draw_title():

    fill(255)
    textAlign(CENTER, CENTER)

    textSize(24)
    text("LIGHTS OUT", width / 2, 35)

    textSize(16)
    fill(148, 163, 184)

    text("Moves: " + str(moves), width / 2, 70)


# =========================
# DRAW GRID
# =========================

def draw_grid():

    for r in range(ROWS):
        for c in range(COLS):

            draw_cell(r, c)


# =========================
# DRAW ONE CELL
# =========================

def draw_cell(r, c):

    x = OFFSET_X + c * (CELL_SIZE + CELL_GAP)
    y = OFFSET_Y + r * (CELL_SIZE + CELL_GAP)

    strokeWeight(2)

    if grid[r][c] == 1:
        fill(250, 204, 21)
        stroke(234, 179, 8)

    else:
        fill(30, 41, 59)
        stroke(51, 65, 85)

    rect(x, y, CELL_SIZE, CELL_SIZE, 8)


# =========================
# WIN SCREEN
# =========================

def draw_win_screen():

    fill(0, 0, 0, 210)
    rect(0, 0, width, height)

    textAlign(CENTER, CENTER)

    fill(34, 197, 94)
    textSize(32)

    text("YOU CLEARED IT!", width / 2, height / 2 - 20)

    fill(255)
    textSize(16)

    text("Total Moves: " + str(moves),
         width / 2,
         height / 2 + 20)

    text("Press 'R' to Restart",
         width / 2,
         height / 2 + 50)


# =========================
# MOUSE CLICK
# =========================

def mousePressed():

    global moves, game_over

    if game_over:
        return

    cell = get_clicked_cell()

    if cell != None:

        r = cell[0]
        c = cell[1]

        toggle_cell(r, c)

        moves += 1

        if check_win():
            game_over = True


# =========================
# FIND CLICKED CELL
# =========================

def get_clicked_cell():

    for r in range(ROWS):
        for c in range(COLS):

            x = OFFSET_X + c * (CELL_SIZE + CELL_GAP)
            y = OFFSET_Y + r * (CELL_SIZE + CELL_GAP)

            if (x <= mouseX <= x + CELL_SIZE and
                y <= mouseY <= y + CELL_SIZE):

                return (r, c)

    return None


# =========================
# KEYBOARD
# =========================

def keyPressed():

    if key == 'r' or key == 'R':
        reset_game()

