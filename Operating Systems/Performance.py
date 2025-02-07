#!/usr/bin/env python
 

import time
chunk_size = 1024 * 1024 * 1024  # 1 GB
memory_chunks = []
try:
    while True:
        memory_chunks.append(bytearray(chunk_size))
        print(f"Allocated {len(memory_chunks)} GB of memory")
        time.sleep(1)
except MemoryError:
    print("Memory allocation failed. System is out of memory.")

 




