import pyscreenshot
import pyautogui
import time
import cv2
import numpy as np
from math import ceil
from solve import draw_board, solve

SITE = "https://www.livesudoku.com/en/sudoku/evil/"


def bot_solve():

    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    while True:
        pos = pyautogui.locateCenterOnScreen("assets/goodluck.png")
        if pos is not None:
            x = pos[0]
            y = pos[1]
            print("Grabbed board")
            start_time = time.time()
            break

    x1 = x - 195
    x2 = x + 199
    y1 = y + 7
    y2 = y + 395
    length = 394
    square_length = length / 9

    bbox = (x1, y1, x2, y2)
    im = pyscreenshot.grab(bbox)
    im.save("assets/board.png")

    for i in range(1, 10):
        # open board image and template image
        board_img = cv2.imread("assets/board.png", cv2.IMREAD_GRAYSCALE)
        img_1 = cv2.imread("assets/online/" + str(i) + ".png", cv2.IMREAD_GRAYSCALE)

        result = cv2.matchTemplate(board_img, img_1, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        w = img_1.shape[1]
        h = img_1.shape[0]

        threshold = .90
        y_loc, x_loc = np.where(result >= threshold)

        for (x, y) in zip(x_loc, y_loc):
            x = ceil(x/square_length)-1
            y = ceil(y/square_length)-1
            board[y][x] = i


    print("Solving...")
    board = solve(board)
    solve_time = (time.time() - start_time)
    print("solve time: " + str(solve_time))

    presses = []
    for row in range(9):
        for column in range(9):
            presses.append(str(board[row][column]))
            presses.append("tab")

    pyautogui.click(x1+10, y1+10)
    pyautogui.press(presses)


def back_to_game():
    time.sleep(2)
    pos = pyautogui.locateCenterOnScreen("assets/online/lobby.png")
    pyautogui.click(pos)

    time.sleep(2)
    pos = pyautogui.locateCenterOnScreen("assets/online/practice.png")
    pyautogui.click(pos)

    time.sleep(2)
    pos = pyautogui.locateCenterOnScreen("assets/online/easy.png")
    pyautogui.click(pos)


for i in range(5):
    print("Game: " + str(i))
    bot_solve()
    back_to_game()
