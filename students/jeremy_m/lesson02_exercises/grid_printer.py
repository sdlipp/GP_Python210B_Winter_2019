# Lesson 02 Exercise: Grid Printer
# Jeremy Monroe

p = '+'
l = '|'

def grid_printer(g_size):
    """ Prints a 4x4 grid where the length & width of each cell == g_size """
    half_g = g_size // 2
    m = '-' * (half_g)
    s = ' ' * (half_g)

    # This grid is always 2x2. So, loop twice
    for i in range(2):
        # print one + sign on each side of - sign times half the g_size
        print(p + m + p + m + p)
        # loop half the g_size to print vertical sides for each cell.
        for i in range(half_g):
            print(l + s + l + s + l)
    
    # print the final row of + and - signs to finish bottom of the grid
    print(p + m + p + m + p)

# grid_printer(15)

def fancy_grid_printer(rowCol, length):
    """ Prints a grid where rowCol sets the number of rows and columns
        and length sets the length & width of each cell. """
    m = '-' * length
    s = ' ' * length

    # loops rowCol to create that many rows
    for i in range(rowCol):
        # loops rowCol to create that many columns
        for j in range(rowCol):
            # prints one + sign and - signs times the specified length
            # to create the top of each row
            print(p + m, end='')

        # prints a final + sign to finish each row
        print(p)

        # loops length to create the vertical sides of each cell
        for j in range(length):
            # loops rowCol to create the proper number of vertical sides
            for k in range(rowCol):
                # prints one | sign and ' ' times the length
                print(l + s, end="")

            # prints final | sign to finish vertical side on last cell
            print(l)

    # Finishes the grid by printing + and - signs across the bottom in
    # accordance witht the number of rowCol's
    for j in range(rowCol):
        print(p + m, end="")
    print(p)

# fancy_grid_printer(3, 2)
fancy_grid_printer(5, 3)