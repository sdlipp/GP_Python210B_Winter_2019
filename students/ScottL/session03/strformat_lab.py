seq = (2, 123.4567, 10000, 12345.67)

str = "file_{:03d} :\t{:.2f}, {:.2e}, {:.2e}".format(seq[0], seq[1], seq[2], seq[3])
print(str)

str2 = f"file_{seq[0]:03d} :\t{seq[1]:.2f}, {seq[2]:.2e}, {seq[3]:.2e}"
print(str2)


def formatter(sequence):
    """Return a comma-separated and formatted string from an input sequence"""
    str = ("The {} numbers are: " + ", ".join(["{}"] * len(sequence))).format(len(sequence), *sequence)
    return str

seq2 = (1, 2, 3, 4, 5)
print(formatter(seq2))

x = 1.2
seq3 = ["oranges", 1.3, "lemons", 1.1]
str3 = f"The weight of an {seq3[0][:-1].upper()} is {seq3[1]*x} and the weight of a {seq3[2][:-1].upper()} is {seq3[3]*x}"
print(str3)

seq4 = (4, 30, 2017, 2, 7)
str4 = (" ".join(["{:02}"] * len(seq4))).format(*seq4[::-1])
print(str4)

seq5 = [["Couch", 0, 2000], ["Bed", 3, 3500], ["Chair", 12, 250], ["Lamp", 25, 40]]
for item in seq5:
    print("{:<18}{:>5}\t\t${:>6}".format(item[0], item[1], item[2]))
