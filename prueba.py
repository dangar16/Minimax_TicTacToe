from tkinter import *
from tkinter import messagebox
from typing import Iterator

root = Tk()
root.title("Tic-Tac-Toe")
# root.geometry("1200x710")

# X starts to true
clicked = True
count = 0


# disable all the buttons
def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


# Check to see if someone won
def checkifwon():
    # Filas
    for fila in board:
        if fila.count("X") == 3 or fila.count("O") == 3:
            return True

    # Diagonales

    diagonal1 = []
    diagonal2 = []
    for i in range(len(board)):
        diagonal1.append(board[i][i])
        diagonal2.append(board[i][len(board) - i - 1])

    if diagonal1.count("X") == 3 or diagonal1.count("O") == 3 or diagonal2.count("X") == 3 or diagonal2.count("O") == 3:
        return True

    # Columnas

    for i in range(3):
        res = []
        for j in range(3):
            res.append(board[j][i])
        if res.count("X") == 3 or res.count("O") == 3:
            return True

    return False

def addDecision(row, col):
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    v = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

    for button in v:
        if button.grid_info()["row"] == row and button.grid_info()["column"] == col:
            button["text"] = "X"
            break


# button clicked function
def b_click(b, row, col):
    global clicked, count

    if b["text"] == " " and clicked == False:
        print(f'{row, col}')
        b["text"] = "O"
        clicked = True
        board[row][col] = "O"
        count += 1
        r = checkifwon()

        if r:
            disable_all_buttons()
            messagebox.showinfo("Ganador", "Ha ganado el humano")

        if count == 9:
            disable_all_buttons()
            messagebox.showinfo("Empate", "ha habido un empate")

        fila, columna = minmax(True, board, 0)
        clicked = False
        addDecision(fila, columna)
        board[fila][columna] = "X"
        count += 1
        r = checkifwon()

        if r:
            messagebox.showinfo("Ganador", "ha ganado la IA")
            disable_all_buttons()
    else:
        messagebox.showerror("Tic Tac Toe", "Hey! That box has already been selected\nPick Another Box...")


def casillas_libres(board) -> Iterator[tuple[int, int]]:
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "":
                yield i, j


def minmax(es_robot, board, profundidad):
    if checkifwon():
        # Si ha hecho el turno el humano y le toca al robot
        if es_robot:
            return -1, profundidad
        # Si ha hecho el turno el robot y le toca al humano
        else:
            return 1, profundidad

    if len(list(casillas_libres(board))) == 0:
        return 0, profundidad

    if es_robot:
        mejor = -1
        mejorFila = -1
        mejorColumna = -1
        mejorProfundidad = float('inf')

        for libre in casillas_libres(board):
            i = libre[0]
            j = libre[1]

            board[i][j] = "X"
            resultado, prof = minmax(False, board, profundidad + 1)

            if resultado > mejor:
                mejor = resultado
                mejorFila = i
                mejorColumna = j
                mejorProfundidad = prof
            elif resultado == mejor and prof < mejorProfundidad:
                mejorFila = i
                mejorColumna = j
                mejorProfundidad = prof

            board[i][j] = ""

        if profundidad == 0:
            board[mejorFila][mejorColumna] = "X"
            return mejorFila, mejorColumna

        return mejor, mejorProfundidad

    else:
        mejor = 1
        mejorProfundidad = float('inf')

        for libre in casillas_libres(board):
            i = libre[0]
            j = libre[1]

            board[i][j] = "O"
            resultado, prof = minmax(True, board, profundidad + 1)

            if resultado < mejor:
                mejor = resultado
                mejorProfundidad = prof
            elif resultado == mejor and prof < mejorProfundidad:
                mejorProfundidad = prof

            board[i][j] = ""

        return mejor, mejorProfundidad


# Start the game over!
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = False
    count = 0
    # build our buttons
    b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b1, b1.grid_info()["row"], b1.grid_info()["column"]))
    b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b2, b2.grid_info()["row"], b2.grid_info()["column"]))
    b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b3, b3.grid_info()["row"], b3.grid_info()["column"]))

    b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b4, b4.grid_info()["row"], b4.grid_info()["column"]))
    b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b5, b5.grid_info()["row"], b5.grid_info()["column"]))
    b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b6, b6.grid_info()["row"], b6.grid_info()["column"]))

    b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b7, b7.grid_info()["row"], b7.grid_info()["column"]))
    b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b8, b8.grid_info()["row"], b8.grid_info()["column"]))
    b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b9, b9.grid_info()["row"], b9.grid_info()["column"]))

    # grid buttons to the screen
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


# Create menue
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Options Menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)
board: list[list[str]] = [["", "", ""], ["", "", ""], ["", "", ""]]

reset()

root.mainloop()
