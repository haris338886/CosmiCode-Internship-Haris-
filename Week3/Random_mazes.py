import tkinter as tk
import random
import time
from collections import deque

CELL_SIZE = 20
ROWS = 21
COLS = 21
DELAY = 0.01

def draw_cell(canvas, r, c, color):
    x1 = c * CELL_SIZE
    y1 = r * CELL_SIZE
    x2 = x1 + CELL_SIZE
    y2 = y1 + CELL_SIZE
    canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
    canvas.update()
    time.sleep(DELAY)

def generate_maze(canvas, maze, visited, r, c):
    visited[r][c] = True
    maze[r][c] = 0
    draw_cell(canvas, r, c, "white")
    directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
    random.shuffle(directions)
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 1 <= nr < ROWS - 1 and 1 <= nc < COLS - 1 and not visited[nr][nc]:
            wall_r, wall_c = r + dr // 2, c + dc // 2
            maze[wall_r][wall_c] = 0
            draw_cell(canvas, wall_r, wall_c, "white")
            generate_maze(canvas, maze, visited, nr, nc)

def solve_maze(canvas, maze, start, end):
    queue = deque([start])
    visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
    parent = {}
    visited[start[0]][start[1]] = True
    while queue:
        r, c = queue.popleft()
        if (r, c) == end:
            break
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS and not visited[nr][nc] and maze[nr][nc] == 0:
                visited[nr][nc] = True
                parent[(nr, nc)] = (r, c)
                queue.append((nr, nc))
                draw_cell(canvas, nr, nc, "lightblue")
    r, c = end
    while (r, c) != start:
        draw_cell(canvas, r, c, "yellow")
        r, c = parent[(r, c)]

def main():
    root = tk.Tk()
    root.title("Maze Generator + BFS Solver")
    canvas = tk.Canvas(root, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE, bg="black")
    canvas.pack()
    maze = [[1 for _ in range(COLS)] for _ in range(ROWS)]
    visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
    generate_maze(canvas, maze, visited, 1, 1)
    maze[0][1] = 0
    maze[ROWS - 1][COLS - 2] = 0
    draw_cell(canvas, 0, 1, "lightgreen")
    draw_cell(canvas, ROWS - 1, COLS - 2, "red")
    solve_maze(canvas, maze, (0, 1), (ROWS - 1, COLS - 2))
    root.mainloop()

main()
