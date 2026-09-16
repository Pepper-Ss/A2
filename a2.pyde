import random

ROWS = 5
COLS = 5
CELL_SIZE = 65
OFFSET_X = 37
OFFSET_Y = 100

grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
moves = 0
game_over = False


def setup():
    size(400, 480)
    reset_game()


def reset_game():
    global grid, moves, game_over

    grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    moves = 0
    game_over = False

    for _ in range(12):
        r = random.randint(0, ROWS - 1)
        c = random.randint(0, COLS - 1)
        toggle(r, c)

    moves = 0


def toggle(r, c):
    targets = [
        (r, c),
        (r - 1, c),
        (r + 1, c),
        (r, c - 1),
        (r, c + 1)
    ]

    for dr, dc in targets:
        if 0 <= dr < ROWS and 0 <= dc < COLS:
            grid[dr][dc] = 1 - grid[dr][dc]


def check_win():
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                return False

    return True


def draw():
    background(15, 23, 42)

    # Title
    fill(255)
    textSize(24)
    textAlign(CENTER, CENTER)
    text("LIGHTS OUT", width / 2, 35)

    # Move counter
    textSize(16)
    fill(148, 163, 184)
    text("Moves: " + str(moves), width / 2, 70)

    # Draw grid
    for r in range(ROWS):
        for c in range(COLS):

            x = OFFSET_X + c * (CELL_SIZE + 5)
            y = OFFSET_Y + r * (CELL_SIZE + 5)

            if grid[r][c] == 1:
                fill(250, 204, 21)
                stroke(234, 179, 8)
            else:
                fill(30, 41, 59)
                stroke(51, 65, 85)

            strokeWeight(2)
            rect(x, y, CELL_SIZE, CELL_SIZE, 8)

    # Win screen
    if game_over:
        fill(0, 0, 0, 210)
        rect(0, 0, width, height)

        fill(34, 197, 94)
        textSize(32)
        textAlign(CENTER, CENTER)
        text("YOU CLEARED IT!", width / 2, height / 2 - 20)

        textSize(16)
        fill(255)
        text("Total Moves: " + str(moves), width / 2, height / 2 + 20)
        text("Press 'R' to Restart", width / 2, height / 2 + 50)


def mousePressed():
    global moves, game_over

    if game_over:
        return

    for r in range(ROWS):
        for c in range(COLS):

            x = OFFSET_X + c * (CELL_SIZE + 5)
            y = OFFSET_Y + r * (CELL_SIZE + 5)

            if x <= mouseX <= x + CELL_SIZE and y <= mouseY <= y + CELL_SIZE:

                toggle(r, c)
                moves += 1

                if check_win():
                    game_over = True

                return


def keyPressed():
    if key == 'r' or key == 'R':
        reset_game()
