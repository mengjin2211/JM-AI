import random
import time
import threading
import os
from multiprocessing import Process, Queue
 
def RandomNumbers(file, start, end):
    """Generate random numbers and write them to a file."""
    with open(file, "a") as f:
        for _ in range(start, end):
            f.write(f"{random.randint(0, 32767)}\n")

def multithreading(num):
    start_time = time.time()
    chunk_size = 1000000 // num
    threads = []
    files = [f"file_thread_{i}.txt" for i in range(num)]   
    
    for i in range(num):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num-1 else 1000000
        thread = threading.Thread(target=RandomNumbers, args=(files[i], start, end))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    with open("file3.txt", "w") as outfile:
        for file in files:
            with open(file, "r") as infile:
                outfile.write(infile.read())
            os.remove(file)   
    
    end_time = time.time()
    return end_time - start_time

def multiprocessing_task(file, start, end, queue):
    RandomNumbers(file, start, end)
    queue.put(file)

def multiprocessing(num):
    start_time = time.time()
    chunk_size = 1000000 // num
    processes = []
    files = [f"file_process_{i}.txt" for i in range(num)]
    queue = Queue()
    
    for i in range(num):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num-1 else 1000000
        process = Process(target=multiprocessing_task, args=(files[i], start, end, queue))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
    
    with open("file4.txt", "w") as outfile:
        while not queue.empty():
            file = queue.get()
            with open(file, "r") as infile:
                outfile.write(infile.read())
            os.remove(file)
    
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
 
    seq_time_start = time.time()
    RandomNumbers("file2.txt", 0, 1000000)
    seq_time_end = time.time()
    print(f'Sequential Processing Time: {seq_time_end - seq_time_start:.4f} seconds.')

    multithreading_time = multithreading(3)
    print(f'Multithreaded Processing Time: {multithreading_time:.4f} seconds.') 
    multiprocessing_time = multiprocessing(3)
    print(f'Multiprocessing Time: {multiprocessing_time:.4f} seconds.')

    os.remove('file2.txt') if os.path.exists('file2.txt') else print('file2.txt does not exist.')
    os.remove('file3.txt') if os.path.exists('file3.txt') else print('file3.txt does not exist.')


