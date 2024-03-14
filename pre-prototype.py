# principal funcion for the contruction of the Grid using for loops and one conditional with the staetment __name__ == '__main__'
def print_grid(grid):
    
    for row in grid:
        for column in row:
            print(column, end=' ')
        print()


if __name__ == '__main__':
    # list of numbers for the values inside the grid 
    numbers = [[1, 2, 3, 1],[4, 5, 6, 2],[3, 6, 5, 4]]


print_grid(numbers)
