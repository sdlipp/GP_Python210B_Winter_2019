#Gina Saifullah

# Function that builds the border line and the body lines of the grid and then prints it. 
# Probably better broken into smaller functions
def make_grid(edge_char, horizontal_char, vertical_char, filler_char, units, side_size):
	
	#Initialize strings
	border = ""
	basic = ""
	
	#Build Border Line
	h_char_str = units * horizontal_char
	h_char_str += edge_char
	h_line = h_char_str * side_size
	border = edge_char + h_line
	
	#Build Body
	body_str = units * filler_char
	body_str += vertical_char
	basic_line = body_str * side_size
	basic = vertical_char + basic_line
	
	#Print Grid
	print(border)
	for i in range(side_size):
		for i in range(units):
			print(basic)
		print(border)
	return
	

# Part 1 - Basic Grid Printer - No arguments
def print_grid():
	border = ""
	string_line = ""
	plus = "+"
	pipe = "|"
	num_dashes = 4
	dashes = num_dashes * "-"
	blanks = num_dashes * " "
	border = plus + dashes + plus + dashes + plus
	basic = pipe + blanks + pipe + blanks + pipe
	
	print(border)
	for i in range(num_dashes):
		print(basic)
	print(border)
	for i in range(num_dashes):
		print(basic)
	print(border)
	return


# Part 2 - The Grid Printer that takes 1 argument.
# int size - number of units in each side of the grid 	
def print_grid_by_size(size):
	make_grid("+", "-", "|", " ", size, 2)


# Part 3 - The Grid Printer with 2 arguments.
# int size - number of units in each side of the grid
# int rows - number of rows and columns in the grid
def print_grid_by_size_and_row(size, rows):
	make_grid("+", "-", "|", " ", size, rows)

def main():
	print("Grid Printer")

# Main and invoke functions
main()

print("Part 1 - Print Grid")
print_grid()

print("Part 2 = Print Grid Function")
print_grid_by_size(8)

print("Part 3 = Print Grid Function with Rows")
print_grid_by_size_and_row(3,5)