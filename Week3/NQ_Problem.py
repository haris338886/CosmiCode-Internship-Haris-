import tkinter as tk

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col]:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j]:
            return False
    return True

def solve(board, row, n):
    if row == n:
        return True
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve(board, row + 1, n):
                return True
            board[row][col] = 0
    return False

def draw_board(canvas, board, n):
    canvas.delete("all")
    cell_size = 50
    for i in range(n):
        for j in range(n):
            x1 = j * cell_size
            y1 = i * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            color = "white" if (i + j) % 2 == 0 else "gray"
            canvas.create_rectangle(x1, y1, x2, y2, fill=color)
            if board[i][j]:
                canvas.create_text(x1 + 25, y1 + 25, text="♛", font=("Arial", 24), fill="red")

def start_gui_solution(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve(board, 0, n)

    window = tk.Tk()
    window.title(f"{n}-Queens Solution")

    canvas = tk.Canvas(window, width=50*n, height=50*n)
    canvas.pack()

    draw_board(canvas, board, n)
    window.mainloop()

start_gui_solution(4)
