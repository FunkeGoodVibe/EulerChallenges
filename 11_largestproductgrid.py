# Problem provided during AlliedCrowds programming session
# Task: Find greatest product of four adjacent numbers (up, down, left, right, or diagonally) in 20×20 grid
#       IMPORTANT NOTE: this code contains many print statements
#            this is only cosmetic as the print statements are not required to solve the problem
#            delete the print statements if code cleanliness is required.

# rc 01 02 03 04 05   'c'
# 10 11 12 13 14 15
# 20 21 22 23 24 25
# 30 31 32 33 34 35
# 40 41 42 43 44 45
# 50 51 52 53 54 55
#'r'


grid = [['08', '02', 22, 97, 38, 15, 00, 40, 00, 75, '04', '05', '07', 78, 52, 12, 50, 77, 91, '08'],
        [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, '04', 56, 62, 00],
        [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, '03', 49, 13, 36, 65],
        [52, 70, 95, 23, '04', 60, 11, 42, 69, 24, 68, 56, '01', 32, 56, 71, 37, '02', 36, 91],
        [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
        [24, 47, 32, 60, 99, '03', 45, '02', 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
        [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
        [67, 26, 20, 68, '02', 62, 12, 20, 95, 63, 94, 39, 63, '08', 40, 91, 66, 49, 94, 21],
        [24, 55, 58, '05', 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
        [21, 36, 23, '09', 75, 00, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95],
        [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, '03', 80, '04', 62, 16, 14, '09', 53, 56, 92],
        [16, 39, '05', 42, 96, 35, 31, 47, 55, 58, 88, 24, 00, 17, 54, 24, 36, 29, 85, 57],
        [86, 56, 00, 48, 35, 71, 89, '07', '05', 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
        [19, 80, 81, 68, '05', 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, '04', 89, 55, 40],
        ['04', 52, '08', 83, 97, 35, 99, 16, '07', 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
        [88, 36, 68, 87, 57, 62, 20, 72, '03', 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
        ['04', 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, '08', 46, 29, 32, 40, 62, 76, 36],
        [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, '04', 36, 16],
        [20, 73, 35, 29, 78, 31, 90, '01', 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, '05', 54],
        ['01', 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, '01', 89, 19, 67, 48]]


#---------------------------------------------------------------

def print_grid(arr):
        print("\n\n")
        for i in range(20):
                for j in range(20):
                        print('{0: <3}'.format(arr[i][j]), end = ' ')
                print("")
        print("\n\n")
print_grid(grid)
#---------------------------------------------------------------

#  1) from the starting index, search the grid EAST direction only (west is implied)
def horizontal_row_max(arr):

    max_res = 0          # initialise the current product, and the maximum product found so far.

    for row in range(0,20):   #go to the LAST row (check1)
        for col in range(0,17):   #go to the 4th to last column (i.e. do not fall off the grid)
            print_grid(grid)
            if (row < 0) or (row > 19) or (col < 0) or (col > 19):
                break
            curr_res = int(grid[row][col]) * int(grid[row][col + 1]) * int(grid[row][col + 2]) * int(grid[row][col + 3])
            print("HORIZONTAL (EAST) 4 POINTS: \nStart: [{0},{1}] \nSecond:[{2},{3}] \nThird: [{4},{5}] \nForth: [{6},{7}]".format(row,col, row, col+1, row, col+2, row, col+3))
            print("Current result for starting position [{0},{1}] is: {2}".format(row, col, curr_res))

            print("The values are", (grid[row][col]), "*", (grid[row][col+1]), "*", (grid[row][col+2]), "*", (grid[row][col+3]), "=", curr_res)

            if curr_res > max_res:
                max_res = curr_res             #update max value
                row_max_index = row            #store row/colum index
                col_max_index = col
                print("[{0},{1}]: is the current east direction maximum start point = {2}".format(row_max_index, col_max_index,max_res))

    return max_res

#---------------------------------------------------------------

# 2) from the starting index, search the grid SOUTH-EAST direction only (i.e. north-west is implied)
def diagonal_right_max(arr):

    max_res = 0  # initialise the current product, and the maximum product found so far.

    for row in range(0,17):  #
        for col in range(0,17):  # end at the bottom, left-most corner (without falling off the grid)
            print_grid(grid)
            if (row < 0) or (row > 19) or (col < 0) or (col > 19):
                break
            curr_res = int(grid[row][col]) * int(grid[row + 1][col + 1]) * int(grid[row + 2][col + 2]) * int(grid[row + 3][col + 3])
            print("RIGHT DIAGONAL (SOUTH EAST) 4 POINTS: \nStart: [{0},{1}] \nSecond:[{2},{3}] \nThird: [{4},{5}] \nForth: [{6},{7}]".format(row, col, row+1, col+1, row+2, col+2, row+3, col+33))
            print("Current result for starting position [{0},{1}] is: {2}".format(row, col, curr_res))
            print("The values are", (grid[row][col]), "*", (grid[row + 1][col + 1]), "*", (grid[row + 2][col + 2]),"*", (grid[row + 3][col + 3]), "=", curr_res)

            if curr_res > max_res:
                max_res = curr_res  # update max value
                row_max_index = row  # store row/colum index
                col_max_index = col
                print("[{0},{1}]: is the current south-east direction maximum start point = {2}".format(row_max_index, col_max_index, max_res))

    return max_res

#---------------------------------------------------------------

# 3) from the starting index, search the grid SOUTH direction only (north is implied)
def vertical_col_max(arr):

    max_res = 0          # initialise the current product, and the maximum product found so far.

    for row in range(0,17):   #go to the 4th to last row (i.e. do not fall off the grid row)
        for col in range(0,20):   #go to the last column
            print_grid(grid)
            if (row < 0) or (row > 19) or (col < 0) or (col > 19):
                break
            curr_res = int(grid[row][col]) * int(grid[row + 1][col]) * int(grid[row + 2][col]) * int(grid[row + 3][col])
            print("VERTICAL (SOUTH) 4 POINTS: \nStart: [{0},{1}] \nSecond:[{2},{3}] \nThird: [{4},{5}] \nForth: [{6},{7}]".format(row,col, row+1, col, row+2, col, row+3, col))
            print("Current result for starting position [{0},{1}] is: {2}".format(row, col, curr_res))
            print("The values are", (grid[row][col]), "*", (grid[row+1][col]), "*", (grid[row+2][col]), "*", (grid[row+3][col]), "=", curr_res)

            if curr_res > max_res:
                max_res = curr_res  # update max value
                row_max_index = row  # store row/colum index
                col_max_index = col
                print("[{0},{1}]: is the current southern direction maximum start point = {2}".format(row_max_index, col_max_index, max_res))

    return max_res

#---------------------------------------------------------------

# 4) from the starting index, search the grid SOUTH-WEST direction only (north-east is implied)
def diagonal_left_max(arr):

    max_res = 0          # initialise the current product, and the maximum product found so far.

    for row in range(3,17):   #end at to the 4th to last row (i.e. do not fall off the grid row) #start at position [3,3] to ensure you do not fall of the grid
        for col in range(3,20):   #go to the last column
            print_grid(grid)
            if (row < 0) or (row > 19) or (col < 0) or (col > 19):
                break
            curr_res = int(grid[row][col]) * int(grid[row - 1][col - 1]) * int(grid[row - 2][col - 2]) * int(grid[row - 3][col - 3])
            print("DIAGONAL LEFT (SOUTH WEST) 4 POINTS: \nStart: [{0},{1}] \nSecond:[{2},{3}] \nThird: [{4},{5}] \nForth: [{6},{7}]".format(row,col, row-1, col-1, row-2, col-2, row-3, col-3))
            print("Current result for starting position [{0},{1}] is: {2}".format(row, col, curr_res))
            print("The values are", (grid[row][col]), "*", (grid[row-1][col-1]), "*", (grid[row-2][col-2]), "*", (grid[row-3][col-3]), "=", curr_res)

            if curr_res > max_res:
                max_res = curr_res  # update max value
                row_max_index = row  # store row/colum index
                col_max_index = col
                print("[{0},{1}]: is the current south-west direction maximum start point = {2}".format(row_max_index, col_max_index, max_res))

    return max_res
# diagonal_left_max(grid)

#---------------------------------------------------------------

def determine_largest_product_in_grid():

    largest_product_final = 0

    if horizontal_row_max(grid) > diagonal_right_max(grid) and horizontal_row_max(grid) > vertical_col_max(grid) and horizontal_row_max(grid) > diagonal_left_max(grid):
        largest_product_final = horizontal_row_max(grid)

    elif diagonal_right_max(grid) > horizontal_row_max(grid) and diagonal_right_max(grid) > vertical_col_max(grid) and diagonal_right_max(grid) > diagonal_left_max(grid):
        largest_product_final = diagonal_right_max(grid)

    elif vertical_col_max(grid) > horizontal_row_max(grid) and vertical_col_max(grid) > diagonal_right_max(grid) and vertical_col_max(grid) > diagonal_left_max(grid):
        largest_product_final = vertical_col_max(grid)

    else:
        largest_product_final = diagonal_left_max(grid)


    print("\n\n\n\n\n\n\n\n THE LARGEST PRODUCT IN THE GRID IS: ", largest_product_final)

#---------------------------------------------------------------
#start here.
determine_largest_product_in_grid()

#---------------------------------------------------------------
#########################
# Test/Logic:

# Where i,j is the current pivot position
# is_max_result is int variable which stores the current largest product value
# for i,j values where (i >=0 and i <= 20) and (j >=0 and j <= 20)

        # HORIZONTAL
        # is_max_result = grid[0][0] * grid[0][1] * grid[0][2] * grid[0][3] (e.g.)
        #               = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]

        # DIAGONAL RIGHT
        # is_max_result = grid[0][0] * grid[1][1] * grid[2][2] * grid[3][3] (e.g.)
        #               = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]

        # VERTICAL
        # is_max_result = grid[0][0] * grid[1][0] * grid[2][0] * grid[3][0] (e.g.)
        #               = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]

        # DIAGONAL LEFT
        # is_max_result = grid[0][0] * grid[0][1] * grid[0][2] * grid[0][3] (e.g.)
        #               = grid[i][j] * grid[i-1][j-1] * grid[i-2][j-2] * grid[i-3][j-3]
