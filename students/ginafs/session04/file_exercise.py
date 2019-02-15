#!/usr/bin/env python3


if __name__ == "__main__":
    
    outfile = open('output.txt', 'w')
    for i in range(10):
        outfile.write("this is line: %i\n"%i)
    outfile.close()

    with open('output.txt', 'w') as f:
        for i in range(10):
           f.write("this is line: %i\n"%i)
           