# Program for four in a row game
# Michael Maseko
# 13-12-2022


positions_list = []
positions_empty_row = {"A": 11, "B": 11, "C": 11, "D": 11, "E": 11, "F": 11, "G": 11}
positions_column = {"A": 1, "B": 3, "C": 5, "D": 7, "E": 9, "F": 11, "G": 13}


def create_grid():
    matrix = []
    for count in range(15):
        matrix.append(['   '] * 15)
    for row2n in range(0, 15, 2):
        for column2n in range(1, 14, 2):
            matrix[row2n][column2n] = '---'
            matrix[column2n][row2n] = ' | '
    return matrix


def drawGrid(matrix):
    print("     A     B     C     D     E     F     G     ")
    for row in range(13):
        print(' ', end='')
        for column in range(15):
            print(matrix[row][column], end='')
        print("\n", end='')


def check_validity(position, variable):
    positions_list.append(position)
    if len(position) != 1:
        print("Your response should be just 1 characters, the Letter for the column, no space or anything else "
              "eg.'B'.\nEnter the position where you want to place", variable + ':')
        position = input().upper()
        positions_list.append(position)
        return check_validity(position, variable)

    elif position not in "ABCDEFG":
        print("Invalid input, please enter just one of the alphabets between A and G that corresponds to where you "
              "want to place", variable)
        position = input().upper()
        positions_list.append(position)
        return check_validity(position, variable)
    elif positions_empty_row[position.upper()] < 0:
        print("Sorry, the column is full, try another column:")
        position = input().upper()
        positions_list.append(position)
        return check_validity(position, variable)
    return positions_list[-1]


def insert(matrix, position, variable):
    matrix[positions_empty_row[position.upper()]][positions_column[position.upper()]] = variable
    positions_empty_row[position] -= 2


def check_left_right(matrix, row=1):
    if row <= 11:
        for column in range(1, 8, 2):
            if matrix[row][column] == " X " == matrix[row][column + 2] == matrix[row][column + 4] == \
                    matrix[row][column + 6]:
                return "X"
            elif matrix[row][column] == " O " == matrix[row][column + 2] == matrix[row][column + 4] == \
                    matrix[row][column + 6]:
                return "O"
        return check_left_right(matrix, row + 2)


def check_up_down(matrix, column=1):
    if column <= 13:
        for row in range(1, 6, 2):
            if matrix[row][column] == " X " == matrix[row + 2][column] == matrix[row + 4][column] == \
                    matrix[row + 6][column]:
                return "X"
            elif matrix[row][column] == " O " == matrix[row + 2][column] == matrix[row + 4][column] == \
                    matrix[row + 6][column]:
                return "O"
        return check_up_down(matrix, column + 2)


def check_botLeft_topRight(matrix):
    # Start checking diagonals from the first diagonal having at least 4 diagonal boxes
    if matrix[5][1] == ' X ' == matrix[7][3] == matrix[9][5] == matrix[11][7]:
        return "X"
    elif matrix[5][1] == ' O ' == matrix[7][3] == matrix[9][5] == matrix[11][7]:
        return "O"
    # The ff is for checking the diagonal from D
    if matrix[1][7] == ' X ' == matrix[3][9] == matrix[5][11] == matrix[7][13]:
        return "X"
    if matrix[1][7] == ' O ' == matrix[3][9] == matrix[5][11] == matrix[7][13]:
        return "O"

    for index in range(3, 7, 2):
        if matrix[index][index - 2] == ' X ' == matrix[index + 2][index] == matrix[index + 4][index + 2] == \
                matrix[index + 6][index + 4]:
            return "X"
        elif matrix[index][index - 2] == ' O ' == matrix[index][index] == matrix[index + 4][index + 2] == \
                matrix[index + 6][index + 4]:
            return "O"
        # The ff is for the diagonal from C
        elif matrix[index - 2][index + 2] == ' X ' == matrix[index][index + 4] == matrix[index + 2][index + 6] == \
                matrix[index + 4][index + 8]:
            return "X"
        elif matrix[index - 2][index + 2] == ' O ' == matrix[index][index + 4] == matrix[index + 2][index + 6] == \
                matrix[index + 4][index + 8]:
            return "O"

    for index in range(1, 7, 2):
        if matrix[index][index] == ' X ' == matrix[index + 2][index + 2] == matrix[index + 4][index + 4] == \
                matrix[index + 6][index + 6]:
            return "X"
        elif matrix[index][index] == ' O ' == matrix[index + 2][index + 2] == matrix[index + 4][index + 4] == \
                matrix[index + 6][index + 6]:
            return "O"
        # The following is for checking the diagonal row starting from B
        elif matrix[index][index + 2] == ' X ' == matrix[index + 2][index + 4] == matrix[index + 4][index + 6] == \
                matrix[index + 6][index + 8]:
            return "X"
        elif matrix[index][index + 2] == ' O ' == matrix[index + 2][index + 4] == matrix[index + 4][index + 6] == \
                matrix[index + 6][index + 8]:
            return "O"


def check_topLeft_botRight(matrix):
    if matrix[1][7] == ' X ' == matrix[3][5] == matrix[5][3] == matrix[7][1]:
        return "X"
    elif matrix[1][7] == ' O ' == matrix[3][5] == matrix[5][3] == matrix[7][1]:
        return "O"
    elif matrix[5][13] == ' X ' == matrix[7][11] == matrix[9][9] == matrix[11][7]:
        return "X"
    elif matrix[5][13] == ' O ' == matrix[7][11] == matrix[9][9] == matrix[11][7]:
        return "O"
    # Now from E and the corresponding
    indices1 = [1, 3]
    indices2 = [13, 11]
    for index1, index2 in zip(indices1, indices2):
        if matrix[index1][index2 - 4] == " X " == matrix[index1 + 2][index2 - 6] == matrix[index1 + 4][index2 - 8] == \
                matrix[index1 + 6][index2 - 10]:
            return "X"
        elif matrix[index1][index2 - 4] == " O " == matrix[index1 + 2][index2 - 6] == matrix[index1 + 4][index2 - 8] == \
                matrix[index1 + 6][index2 - 10]:
            return "O"
        # The corresponding
        elif matrix[index1 + 2][index2] == " X " == matrix[index1 + 4][index2 - 2] == matrix[index1 + 6][index2 - 4] == \
                matrix[index1 + 8][index2 - 6]:
            return "X"
        elif matrix[index1 + 2][index2] == " O " == matrix[index1 + 4][index2 - 2] == matrix[index1 + 6][index2 - 4] == \
                matrix[index1 + 8][index2 - 6]:
            return "O"
    # Now from f
    indices1 = [1, 3, 5]
    indices2 = [13, 11, 9]
    for index1, index2 in zip(indices1, indices2):
        if matrix[index1][index2 - 2] == " X " == matrix[index1 + 2][index2 - 4] == matrix[index1 + 4][index2 - 6] == \
                matrix[index1 + 6][index2 - 8]:
            return "X"
        elif matrix[index1][index2 - 2] == " O " == matrix[index1 + 2][index2 - 4] == matrix[index1 + 4][index2 - 6] == \
                matrix[index1 + 6][index2 - 8]:
            return "O"
        # Now from G
        elif matrix[index1][index2] == " X " == matrix[index1 + 2][index2 - 2] == matrix[index1 + 4][index2 - 4] == \
                matrix[index1 + 6][index2 - 6]:
            return "X"
        elif matrix[index1][index2] == " O " == matrix[index1 + 2][index2 - 2] == matrix[index1 + 4][index2 - 4] == \
                matrix[index1 + 6][index2 - 6]:
            return "O"


def check_winner(matrix):
    if check_left_right(matrix) is not None:
        return check_left_right(matrix)
    elif check_up_down(matrix) is not None:
        return check_up_down(matrix)
    elif check_topLeft_botRight(matrix) is not None:
        return check_topLeft_botRight(matrix)
    elif check_botLeft_topRight(matrix) is not None:
        return check_botLeft_topRight(matrix)


def stay_leave(decision):
    if decision == '1':
        for item in positions_empty_row:    # Resetting the empty rows
            positions_empty_row[item] = 11
        matrix = create_grid()
        Multiplayer_main(matrix)
        if check_winner(matrix) is None:
            print("Game over, It's a draw!! Thanks for playing!, see you again.")
        else:
            print("Game over!! The winner is", check_winner(matrix) + ", Thanks for playing!, see you again.")
        decision = input("Select 1 to play again or any other key to exit:\n")
        if decision == "1":
            print(

            )
        stay_leave(decision)
    else:
        print("We're sad to see you leave, hoping to see you soon again.")
        exit(0)


def Multiplayer_main(matrix, count=0):
    if count < 42:
        drawGrid(matrix)
        if count > 6 and check_winner(matrix) is not None:
            print("Game over!!The winner is", check_winner(matrix) + ", Thanks for playing!, see you again.")
            decision = input("Select 1 to play again or any other key to exit:\n")
            if decision == "1":
                print("We're glad to see you back again!!")
            stay_leave(decision)
        if count % 2 == 0:
            variable = ' X '
        else:
            variable = ' O '
        print("Enter the position where you want to place "+variable + ":")
        position = check_validity(input().upper(), variable)
        insert(matrix, position.upper(), variable)
        Multiplayer_main(matrix, count+1)
    drawGrid(matrix)


def main():
    print("Welcome to Sir Michael\'s Tic-Tac-Toe Game!\nThe instructions are:\nEnter the column's Alphabet where you"
          "want to enter 'X' or 'O', note that the variable 'X' or 'O' will go to the most bottom \nempty box, for "
          "example 'B'  will result in the following:")
    matrix = create_grid()
    insert(matrix, "B", " X ")
    positions_empty_row["B"] = 11
    drawGrid(matrix)
    input("Press enter to start playing:\n")
    stay_leave("1")
    if check_winner(matrix) is None:
        print("Game over, It's a draw!! Thanks for playing!, see you again.")
    else:
        print("Game over!! The winner is", check_winner(matrix) + ", Thanks for playing!, see you again.")
    decision = input("Select 1 to play again or any other key to exit:\n")
    if decision == "1":
        print("We're glad to see you back again!!")
    stay_leave(decision)


if __name__ == '__main__':
    main()
