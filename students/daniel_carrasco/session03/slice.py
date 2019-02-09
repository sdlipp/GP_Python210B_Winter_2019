def firstandlast(value):
    return value[-1:]+value[1:-1]+value[:1]
def everyother(value):
    return value[::2]
def first4last4(value):
    return value[:4]+value[-4:]
def reversed(value):
    return value[::-1]
def third(value):
    third = int(len(value)/3)
    return value[-1*third:]+value[third:-1*third]+value[:third]

#first function
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

print(firstandlast(a_string))
print(firstandlast(a_tuple))
assert firstandlast(a_string) == "ghis is a strint"
assert firstandlast(a_tuple) == (32, 54, 13, 12, 5, 2)

#second function
print(everyother(a_string))
print(everyother(a_tuple))
assert everyother(a_string) == "ti sasrn"
assert everyother(a_tuple) == (2, 13, 5)

#third function
print(first4last4(a_string))
print(first4last4(a_tuple))
assert first4last4(a_string) == "thisring"
assert first4last4(a_tuple) == (2,54,13,12,13,12,5,32)

#fourth function
print(reversed(a_string))
print(reversed(a_tuple))
assert reversed(a_string) == "gnirts a si siht"
assert reversed(a_tuple) == (32,5,12,13,54,2)

#fifth function
print(third(a_string))
print(third(a_tuple))
#assert third(a_string) == "tringis a sthis"
#assert third(a_tuple) == (5,32,13,12,2,54)