import tkinter as tk
from tkinter import font, messagebox
import random

GRID_SIZE = 4
CELL_SIZE = 100
CELL_PADDING = 10
FONT_SIZE = 40
BG_COLOR_EMPTY = "#9e948a"
BG_COLOR_CELLS = {
    2: "#eee4da", 4: "#ede0c8", 8: "#f2b179", 16: "#f59563",
    32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72", 256: "#edcc61",
    512: "#edc850", 1024: "#edc53f", 2048: "#edc22e",
    4096: "#3c3a32", 8192: "#3c3a32", # 可以继续添加更大的数值颜色
}
COLOR_CELL_TEXT = {2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2",
                   32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2", 256: "#f9f6f2",
                   512: "#f9f6f2", 1024: "#f9f6f2", 2048: "#f9f6f2",
                   4096: "#f9f6f2", 8192: "#f9f6f2"}
BG_COLOR_GRID = "#bbada0"
FONT = ("Verdana", FONT_SIZE, "bold")


class Game2048(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        master.title("2048 Game")
        self.grid_cells = []
        self.init_grid()
        self.init_matrix()
        self.draw_grid_cells()
        self.draw_matrix()
        self.score = 0
        self.score_label = tk.Label(master, text="Score: 0", font=("Verdana", 16))
        self.score_label.pack(pady=10)
        self.bind_keys()
        self.mainloop()

    def init_grid(self):
        background = tk.Frame(self.master, bg=BG_COLOR_GRID, bd=3, relief=tk.SUNKEN)
        background.pack(pady=50)

        for i in range(GRID_SIZE):
            row_cells = []
            for j in range(GRID_SIZE):
                cell = tk.Frame(background, bg=BG_COLOR_EMPTY, width=CELL_SIZE, height=CELL_SIZE)
                cell.grid(row=i, column=j, padx=CELL_PADDING, pady=CELL_PADDING)
                t = tk.Label(master=cell, text="", bg=BG_COLOR_EMPTY, justify=tk.CENTER, font=FONT, width=4, height=2, fg=COLOR_CELL_TEXT[2] if 2 in COLOR_CELL_TEXT else "black") # 初始化时先用一个默认颜色，之后会更新
                t.grid()
                row_cells.append(t)
            self.grid_cells.append(row_cells)

    def init_matrix(self):
        self.matrix = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
        self.add_new_tile()
        self.add_new_tile()

    def draw_grid_cells(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                self.grid_cells[i][j].config(text="", bg=BG_COLOR_EMPTY)

    def draw_matrix(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.matrix[i][j] != 0:
                    number = self.matrix[i][j]
                    cell_text = str(number)
                    cell_color = BG_COLOR_CELLS.get(number, BG_COLOR_CELLS.get(2048)) # 如果数字没有定义颜色，则使用2048的颜色
                    text_color = COLOR_CELL_TEXT.get(number, "white") # 默认文字颜色为白色
                    self.grid_cells[i][j].config(text=cell_text, bg=cell_color, fg=text_color)
                else:
                    self.grid_cells[i][j].config(text="", bg=BG_COLOR_EMPTY)

    def add_new_tile(self):
        possible_cells = []
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.matrix[i][j] == 0:
                    possible_cells.append((i, j))
        if not possible_cells:
            return
        row, col = random.choice(possible_cells)
        self.matrix[row][col] = random.choice([2, 2, 2, 4]) # 2出现的概率比4大

    def bind_keys(self):
        self.master.bind("<KeyPress-Up>", self.move_up)
        self.master.bind("<KeyPress-Down>", self.move_down)
        self.master.bind("<KeyPress-Left>", self.move_left)
        self.master.bind("<KeyPress-Right>", self.move_right)

    def move_row_left(self, row):
        new_row = [cell for cell in row if cell != 0]
        merged_row = []
        i = 0
        while i < len(new_row):
            if i + 1 < len(new_row) and new_row[i] == new_row[i + 1]:
                merged_row.append(new_row[i] * 2)
                self.score += new_row[i] * 2
                i += 2
            else:
                merged_row.append(new_row[i])
                i += 1
        return merged_row + [0] * (GRID_SIZE - len(merged_row))

    def move_left(self, event):
        moved = False
        original_matrix = [row[:] for row in self.matrix] # 深拷贝，用于比较是否移动过
        for i in range(GRID_SIZE):
            new_row = self.move_row_left(self.matrix[i])
            if new_row != self.matrix[i]:
                self.matrix[i] = new_row
                moved = True

        if moved:
            self.add_new_tile()
            self.draw_matrix()
            self.update_score()
            if self.check_game_over():
                self.game_over()

    def move_right(self, event):
        moved = False
        original_matrix = [row[:] for row in self.matrix]
        for i in range(GRID_SIZE):
            reversed_row = self.matrix[i][::-1] # 反转行
            new_reversed_row = self.move_row_left(reversed_row) # 向左移动逻辑复用
            new_row = new_reversed_row[::-1] # 再次反转得到向右移动的结果
            if new_row != self.matrix[i]:
                self.matrix[i] = new_row
                moved = True

        if moved:
            self.add_new_tile()
            self.draw_matrix()
            self.update_score()
            if self.check_game_over():
                self.game_over()

    def move_up(self, event):
        moved = False
        original_matrix = [row[:] for row in self.matrix]
        for j in range(GRID_SIZE): # 遍历列
            column = [self.matrix[i][j] for i in range(GRID_SIZE)] # 获取列
            new_column = self.move_row_left(column) # 列的移动逻辑和行的向左移动逻辑相同
            for i in range(GRID_SIZE):
                if self.matrix[i][j] != new_column[i]:
                    self.matrix[i][j] = new_column[i]
                    moved = True

        if moved:
            self.add_new_tile()
            self.draw_matrix()
            self.update_score()
            if self.check_game_over():
                self.game_over()

    def move_down(self, event):
        moved = False
        original_matrix = [row[:] for row in self.matrix]
        for j in range(GRID_SIZE):
            column = [self.matrix[i][j] for i in range(GRID_SIZE)]
            reversed_column = column[::-1]
            new_reversed_column = self.move_row_left(reversed_column)
            new_column = new_reversed_column[::-1]
            for i in range(GRID_SIZE):
                if self.matrix[i][j] != new_column[i]:
                    self.matrix[i][j] = new_column[i]
                    moved = True

        if moved:
            self.add_new_tile()
            self.draw_matrix()
            self.update_score()
            if self.check_game_over():
                self.game_over()

    def check_game_over(self):
        # 检查是否还能移动，没有空位，且相邻的数字都不相等
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.matrix[i][j] == 0: # 有空位，游戏未结束
                    return False
                if i < GRID_SIZE - 1 and self.matrix[i][j] == self.matrix[i+1][j]: # 检查下方
                    return False
                if j < GRID_SIZE - 1 and self.matrix[i][j] == self.matrix[i][j+1]: # 检查右方
                    return False
        return True # 没有空位且无法合并，游戏结束

    def game_over(self):
        messagebox.showinfo("Game Over", f"Game Over! Your Score: {self.score}")
        self.init_matrix() # 重新开始游戏
        self.draw_matrix()
        self.score = 0
        self.update_score()


    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")


if __name__ == '__main__':
    root = tk.Tk()
    game = Game2048(root)
