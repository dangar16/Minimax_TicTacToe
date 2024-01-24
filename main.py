import time
from typing import Iterator


def casillas_libres(board) -> Iterator[tuple[int, int]]:
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "":
                yield i, j


def comprobacion(fila=-1, columna=-1, board=None):
    if board is None:
        board = []
    while fila < 1 or fila > 3 or columna < 1 or columna > 3 or board[fila - 1][columna - 1] != "":
        print("Introduce el numero de fila: ")
        fila = int(input("Fila: "))

        print("Introduce el numero de columna: ")
        columna = int(input("Columna: "))

    return fila, columna


def minmax(es_robot, board, profundidad):
    if ganador(board):
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


def hacer_movimiento(es_robot, board):
    if not es_robot:
        fila, columna = comprobacion(board=board)
        board[fila - 1][columna - 1] = "O"
    else:
        minmax(True, board, 0)


def ganador(board) -> bool:
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


def print_board(board):
    for fila in board:
        print(fila)

    print()


def run(board):
    es_robot = True
    ganadores = False
    while not ganadores and len(list(casillas_libres(board))) != 0:
        hacer_movimiento(es_robot := not es_robot, board)
        ganadores = ganador(board)

        print_board(board)

    print("Ha ganado la IA" if ganadores else "empate")


if __name__ == '__main__':
    board: list[list[str]] = [["", "", ""], ["", "", ""], ["", "", ""]]
    run(board)
