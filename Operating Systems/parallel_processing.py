#!/usr/bin/env python3
import time 
import sys

def process_files(file1, file2, output):
    """
    Reads the entire content of file1 and file2 (which are chunks),
    adds corresponding lines, and writes the result to the output file.
    """
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output, 'w') as out:
        for line1, line2 in zip(f1, f2):
            try:
                total = int(line1.strip()) + int(line2.strip())
            except ValueError:
                continue
            out.write(f"{total}\n")

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python script.py <file1> <file2> <output>")
        sys.exit(1)
 
        process_files(sys.argv[1], sys.argv[2], sys.argv[3])

        
 

