import random

ROWS = 5
COLS = 5
CELL_SIZE = 65
OFFSET_X = 37
OFFSET_Y = 100

def create_grid():
    grid = []

    r = 0
    while r < ROWS:
        row = []

        c = 0
        while c < COLS:
            row.append(0)
            c += 1

        grid.append(row)
        r += 1

    return grid


grid = create_grid()
moves = 0
game_over = False


def setup():
    size(400, 480)
    reset_game()


def reset_game():
    global grid, moves, game_over

    grid = create_grid()
    moves = 0
    game_over = False

    # สร้างปริศนาแบบสุ่ม
    count = 0

    while count < 12:
        row = random.randint(0, ROWS - 1)
        col = random.randint(0, COLS - 1)

        toggle(row, col)

        count += 1


def toggle(r, c):

    # ตำแหน่งที่ต้องเปลี่ยน
    directions = [
        (0, 0),
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    i = 0

    while i < len(directions):

        nr = r + directions[i][0]
        nc = c + directions[i][1]

        if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS:
            grid[nr][nc] = 1 - grid[nr][nc]

        i += 1


def check_win():

    for r in range(ROWS):
        for c in range(COLS):

            if grid[r][c] != 0:
                return False

    return True


def save_game():

    try:
        file = open("savegame.txt", "w")

        file.write(str(moves) + "\n")
        file.write(str(int(game_over)) + "\n")

        for r in range(ROWS):

            line = ""

            for c in range(COLS):
                line += str(grid[r][c])

                if c != COLS - 1:
                    line += " "

            file.write(line + "\n")

        file.close()

        print("Game saved!")

    except:
        print("Unable to save game.")


def load_game():

    global grid, moves, game_over

    try:
        file = open("savegame.txt", "r")
        lines = file.readlines()
        file.close()

        moves = int(lines[0].strip())
        game_over = int(lines[1].strip()) == 1

        new_grid = []

        for r in range(ROWS):

            numbers = lines[r + 2].split()
            row = []

            for c in range(COLS):
                row.append(int(numbers[c]))

            new_grid.append(row)

        grid = new_grid

        print("Game loaded!")

    except:
        print("Unable to load game.")


def draw():

    background(15, 23, 42)

    fill(255)
    textAlign(CENTER, CENTER)

    textSize(24)
    text("LIGHTS OUT", width / 2, 25)

    textSize(13)
    fill(180)
    text("Moves: " + str(moves), width / 2, 52)
    text("[R] Reset  [S] Save  [L] Load", width / 2, 70)

    # วาดตาราง
    r = 0

    while r < ROWS:

        c = 0

        while c < COLS:

            x = OFFSET_X + c * (CELL_SIZE + 5)
            y = OFFSET_Y + r * (CELL_SIZE + 5)

            if grid[r][c] == 1:
                fill(250, 204, 21)
            else:
                fill(30, 41, 59)

            stroke(100)
            strokeWeight(2)

            rect(x, y, CELL_SIZE, CELL_SIZE, 8)

            c += 1

        r += 1

    if game_over:

        fill(0, 0, 0, 210)
        rect(0, 0, width, height)

        fill(50, 220, 100)
        textSize(32)
        text("YOU CLEARED IT!", width / 2, height / 2 - 20)

        fill(255)
        textSize(16)
        text("Total Moves: " + str(moves),
             width / 2, height / 2 + 20)

        text("Press R to Restart",
             width / 2, height / 2 + 50)


def mousePressed():

    global moves, game_over

    if game_over:
        return

    for r in range(ROWS):

        for c in range(COLS):

            x = OFFSET_X + c * (CELL_SIZE + 5)
            y = OFFSET_Y + r * (CELL_SIZE + 5)

            inside_x = x <= mouseX <= x + CELL_SIZE
            inside_y = y <= mouseY <= y + CELL_SIZE

            if inside_x and inside_y:

                toggle(r, c)
                moves += 1

                if check_win():
                    game_over = True

                return


def keyPressed():

    global game_over

    if key in ['r', 'R']:
        reset_game()

    elif key in ['s', 'S']:
        save_game()

    elif key in ['l', 'L']:
        load_game()

    elif key == '0' or key == '1':

        for r in range(ROWS):

            for c in range(COLS):

                x = OFFSET_X + c * (CELL_SIZE + 5)
                y = OFFSET_Y + r * (CELL_SIZE + 5)

                if x <= mouseX <= x + CELL_SIZE:
                    if y <= mouseY <= y + CELL_SIZE:

                        grid[r][c] = int(key)

                        if check_win():
                            game_over = True

                        return
