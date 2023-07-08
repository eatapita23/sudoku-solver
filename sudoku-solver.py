def sudoku_solver(puzzle):
    x, y = (9, 9)
    rows = [[0 for i in range(x)] for j in range(y)]
    cols = [[0 for i in range(x)] for j in range(y)]
    regions = [[0 for i in range(x)] for j in range(y)]

    parse_puzzle_for_existing_nums(puzzle, rows, cols, regions)
    sudoku_helper(puzzle, 0, rows, cols, regions)

def sudoku_helper(puzzle, counter, rows, cols, regions):
    print_board(puzzle)
    print(rows)


    i, j = get_coordinates(counter)
    print(i)
    print(j)
    print(counter)

    if counter == 81:
        print_board(puzzle)
        return True
    # print(check_valid(puzzle, i, j, rows, cols, regions))
    # if not check_valid(puzzle, i, j, rows, cols, regions):
    #     print("HERE")
    #     return False
    print()

    if puzzle[i][j] != 0:
        return sudoku_helper(puzzle, counter + 1, rows, cols, regions)

    for num in range(1,10):
        print("Trying to add " + str(num) + " at " + str(i) +"," + str(j))
        print("Would it be valid? " + str(check_valid(puzzle, i, j, rows, cols, regions)))
        if not add_num(puzzle, i, j, num, rows, cols, regions):
            continue
        if sudoku_helper(puzzle, counter + 1, rows, cols, regions):
            return True
        remove_num(puzzle, i, j, num, rows, cols, regions)

def check_valid(puzzle, i, j, rows, cols, regions):
    if i == 0 and j == 0:
        return True # counter hasn't started

    new_num = puzzle[i][j]

    if rows[i][new_num-1] == 1:
        return False
    if cols[j][new_num-1] == 1:
        return False
    if regions[get_region(i,j)][new_num-1] == 1:
        return False

    return True

def get_coordinates(counter):
    i = counter // 9
    j = counter % 9
    return i, j

def get_region(i, j):
    return j // 3 + (i // 3 * 3)

def add_num(puzzle, i, j, num, rows, cols, regions):
    puzzle[i][j] = num

    if check_valid(puzzle, i, j, rows, cols, regions):
        rows[i][num - 1] = 1
        cols[j][num - 1] = 1
        regions[get_region(i, j)][num - 1] = 1
        return True
    else:
        puzzle[i][j] = 0
        return False

def remove_num(puzzle, i, j, num, rows, cols, regions):
    puzzle[i][j] = 0
    rows[i][num-1] = 0
    cols[j][num-1] = 0
    regions[get_region(i, j)][num-1] = 0

def print_board(puzzle):
    for i in range(0,9):
        for j in range(0,9):
            print(" " + str(puzzle[i][j]), end="")
        print()

def parse_puzzle_for_existing_nums(puzzle, rows, cols, regions):
    for i in range(0,9):
        for j in range(0,9):
            if puzzle[i][j] != 0:
                if not add_num(puzzle, i, j, puzzle[i][j], rows, cols, regions):
                    print("ERROR: wrong input puzzle!")


if __name__ == '__main__':
    puzzle = [[0, 0, 0, 7, 0, 2, 9, 0, 0],\
              [0, 9, 0, 0, 8, 1, 2, 0, 9],\
              [8, 7, 2, 4, 5, 0, 0, 1, 3],\
              [1, 0, 0, 0, 7, 0, 4, 2, 0],\
              [9, 0, 0, 1, 0, 5, 0, 0, 8],\
              [0, 4, 0, 0, 0, 0, 5, 6, 0],\
              [0, 3, 5, 8, 0, 4, 0, 9 ,6],\
              [0 ,8 ,0 ,0 ,3 ,6 ,7 ,0 ,0],\
              [0 ,0 ,0 ,5 ,0 ,0 ,0 ,3 ,2]]

    sudoku_solver(puzzle)
    # x, y = (9, 9)
    # rows = [[0 for i in range(x)] for j in range(y)]
    # cols = [[0 for i in range(x)] for j in range(y)]
    # regions = [[0 for i in range(x)] for j in range(y)]
    # add_num(puzzle, 0, 0, 1, rows, cols, regions)
    # print(add_num(puzzle, 0, 1, 2, rows, cols, regions))
    # print_board(puzzle)