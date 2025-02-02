import random
import time
import os 
 
def RandomNumbers(file, start, end):
    seq_time_start = time.time()
    with open(file, "a") as f:
        for _ in range(start, end):
            f.write(f"{random.randint(0, 32767)}\n")
    seq_time_end = time.time()
    print(f'Sequential Streaming Processing Time: {seq_time_end - seq_time_start:.4f} seconds.')

def removefile (file):
    os.remove(file) if os.path.exists(file) else print(f'{file} does not exist.')

def batch(input_file, new_file):
    seq_time_start = time.time()
    with open(input_file, 'r') as file:
        lines = file.readlines()
    doubled_numbers = [str(int(number.strip()) * 2) + '\n' for number in lines]
    with open('newfile2.txt', 'w') as new_file:
        new_file.writelines(doubled_numbers)
    seq_time_end = time.time()
    print(f'Batch Processing Time: {seq_time_end - seq_time_start:.4f} seconds.')

def streaming (input_file, new_file):
    seq_time_start = time.time()
    with open(input_file, 'r') as input, open(new_file, 'w') as output:
        for line in input:
            doubled_number = int(line.strip())* 2
            output.write(f"{doubled_number}\n")
    seq_time_end = time.time()
    print(f'Streaming Processing Time: {seq_time_end - seq_time_start:.4f} seconds.')

def split (input_file, new_file):
    seq_time_start = time.time()
    with open(input_file, 'r') as file:
        lines = file.readlines()
    halfway = len(lines)// 2
    part1 = lines[:halfway]
    doubled_numbers1 = [str(int(number.strip()) * 2) + '\n' for number in part1]   
    part2 = lines[halfway:]  
    doubled_numbers2 = [str(int(number.strip()) * 2) + '\n' for number in part2] 
    doubled_numbers = doubled_numbers1 + doubled_numbers2
    with open(new_file, 'w') as output:
        output.writelines(doubled_numbers)
    seq_time_end = time.time()
    print(f'Split Processing Time: {seq_time_end - seq_time_start:.4f} seconds.')

if __name__ == "__main__":
    removefile ("file1.txt")
    RandomNumbers("file1.txt", 0, 1000000)
    batch ("file1.txt","newfile1.txt")
    streaming ("file1.txt","newfile1.txt")
    split ("file1.txt","newfile1.txt")

 
    
