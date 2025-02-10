import random
import time
import os
import numpy as np
import multiprocessing 

def optimized_random_numbers(file, start, end, chunk=100000):
    """ Optimization with Numpy and Chunks."""
    with open(file, "w") as f:
        for _ in range((end - start) // chunk):
            numbers = np.random.randint(0, 32767, size=chunk, dtype=np.int32)
            f.write("\n".join(map(str, numbers)) + "\n")

def removefile (file):
    os.remove(file) if os.path.exists(file) else print(f'{file} does not exist.')
def remove_files(num_files):
    for i in range(num_files):
        file_name = f"file_{i}.txt"
        if os.path.exists(file_name):
            os.remove(file_name)

def parallel_processing(num_files, total_rows=10000000):
    processes = []
    chunk_size = total_rows // num_files

    start_time = time.time()
    
    for i in range(num_files):
        file_name = f"file_{i}.txt"
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_files - 1 else total_rows
        
        p = multiprocessing.Process(target=optimized_random_numbers, args=(file_name, start, end))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()

    end_time = time.time()
    print(f"Parallel Processing Time ({num_files} files): {end_time - start_time:.4f} seconds")
    remove_files(num_files)

if __name__ == "__main__":
    removefile ("file1.txt")
    optimized_random_numbers("file1.txt", 0, 10000000)
    for num_files in [1, 2, 5, 10, 20]:
        parallel_processing(num_files=num_files) 	
