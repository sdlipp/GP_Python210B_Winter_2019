#Gina Saifullah

# Returns True if divisible by 3
def MultipleOfThree(num):
	if (num % 3 == 0):
		return True
	return False

# Returns True if divisible by 5
def MultipleOfFive(num):
	if (num % 5 == 0):
		return True
	return False	


def main():
	pass

# Main
main()

print()
print("The FizzBuzz Problem")
print()

for i in range(1, 101, 1):
	out_str = ""
	if (MultipleOfThree(i) is True):
		out_str += "Fizz"
	if (MultipleOfFive(i) is True):
		out_str += "Buzz"
	if (len(out_str) == 0):
		out_str = i
	print(out_str)
		