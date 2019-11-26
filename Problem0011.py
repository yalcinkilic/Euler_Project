"""
This program solves 11th problem of Euler Project
"""
def compute_largest_diagonal2_product(grid):
    """
    Find largest diagonal product
    """
    max_product = 0
    for row in range(len(grid) - 1 , 2 , -1):
        for column in range(len(grid) - 3):
            current_product = 1
            for j in range(4):
                current_product *= grid[row - j][column + j]
            if current_product > max_product:
                max_product = current_product

            if current_product == 70600674:
                print(row , column)
    return max_product

def compute_largest_diagonal1_product(grid):
    """
    Find largest diagonal product
    """
    max_product = 0
    for row in range(len(grid) - 3):
        for column in range(len(grid) -3):
            current_product = 1
            for j in range(4):
                current_product *= grid[row + j][column + j]
            if current_product > max_product:
                max_product = current_product
    return max_product

def compute_largest_column_product(grid):
    """
    Find largest column product
    """
    max_product = 0
    for column in range(len(grid)):
        for row in range(len(grid) - 3):
            current_product = 1
            for j in range(4):
                current_product *= grid[row + j][column]
            if current_product > max_product:
                max_product = current_product
    return max_product

def compute_largest_row_product(grid):
    """
    Find largest row_product
    """
    max_product = 0
    for row in grid:
        for column in range(len(grid) - 3):
            current_product = 1
            for j in range(4):
                current_product *= row[column + j]
            if current_product > max_product :
                max_product = current_product

    return max_product


def compute_largest_product(grid):
    """
    Find largest product in the grid via 4 adjacent numbers
    """
    row_largest = compute_largest_row_product(grid)
    column_largest = compute_largest_column_product(grid)
    diagonal1_largest = compute_largest_diagonal1_product(grid)
    diagonal2_largest = compute_largest_diagonal2_product(grid)

    my_list = [row_largest , column_largest , diagonal1_largest , diagonal2_largest]
    return max(my_list)


def read_grid():
    """
    This function reads txt file to construct a grid.
    """
    file = open("grid_problem11.txt" , 'r')
    grid = []
    for line in file:
        line_list = line.split(" ")
        row = []
        for element in line_list:
            int_element = int(element)
            row.append(int_element)

        grid.append(row)

    return grid

our_grid = read_grid()
print("The largest product found in the grid is" , compute_largest_product(our_grid))
