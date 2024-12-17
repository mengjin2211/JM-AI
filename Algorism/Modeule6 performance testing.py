
import random
import string
import timeit
import statistics
from concurrent.futures import ThreadPoolExecutor
import matplotlib.pyplot as plt
import time 
import sys
base = 256
prime = 211

def brute_force_search(text, pattern):
    brute_force_matches = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            brute_force_matches.append(i)
    return brute_force_matches

def rabin_karp(text, pattern): 
    m = len(pattern)
    n = len(text)
    if m > n:
        return []
    pattern_hash = 0
    text_hash = 0
    h = 1  # h = pow(base, m-1) % prime
    for i in range(m - 1):
        h = (h * base) % prime

    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime

    matches = []
    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if text[i:i + m] == pattern:
                matches.append(i)
 
        if i < n - m:
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if text_hash < 0:
                text_hash += prime

    return matches
#with the help of ChatGPT and Claude3
def rabin_karp1(text, pattern):
    m, n = len(pattern), len(text)

    if m > n:
        return []
    base_power = pow(base, m - 1, prime)
    def compute_hash(s, length):
        h = 0
        for i in range(length):
            h = (h * base + ord(s[i])) % prime
        return h
    pattern_hash = compute_hash(pattern, m)
    text_hash = compute_hash(text, m)
    matches = []
    for i in range(n - m + 1):
        if pattern_hash == text_hash and text[i:i+m] == pattern:
            matches.append(i)

        if i < n - m:
            text_hash = (text_hash * base - ord(text[i]) * base_power + ord(text[i + m])) % prime

            if text_hash < 0:
                text_hash += prime

    return matches

def simplified_rabin_karp(text, pattern):
    m, n = len(pattern), len(text)

    if m > n:
        return []
    matches = []
    pattern_hash = hash(pattern)

    for i in range(n - m + 1):
        if hash(text[i:i+m]) == pattern_hash:
            if text[i:i+m] == pattern:
                matches.append(i)

    return matches
#with the help of ChatGPT and Claude3
def rabin_karp2(text, pattern):
    m, n = len(pattern), len(text)

    if m > n:
        return []
    def compute_rolling_hash(s, length):
        h = 0
        for i in range(length):
            h = (h * base + ord(s[i])) & 0xFFFFFFFF
        return h

    pattern_hash = compute_rolling_hash(pattern, m)
    text_window_hash = compute_rolling_hash(text, m)

    highest_power = pow(base, m - 1, prime)

    matches = []

    for i in range(n - m + 1):
        if pattern_hash == text_window_hash:
            if text[i:i+m] == pattern:
                matches.append(i)

        if i < n - m:
            text_window_hash = (
                (text_window_hash * base -
                 ord(text[i]) * highest_power +
                 ord(text[i + m]))
                & 0xFFFFFFFF
            )

    return matches

#with the help of ChatGPT and Claude3
def rabin_karp_parallel(text, pattern):
    num_chunks = 4  # Number of chunks
    text_length = len(text)
    pattern_length = len(pattern)
    chunk_size = max(1, text_length // num_chunks)
    results = []

    def process_chunk(start, end):
        local_results = []
        pattern_hash = 0
        text_hash = 0
        h = 1

        for i in range(pattern_length - 1):
            h = (h * base) % prime

        for i in range(pattern_length):
            pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
            text_hash = (base * text_hash + ord(text[start + i])) % prime

        for i in range(start, end - pattern_length + 1):
            if pattern_hash == text_hash:
                if text[i:i + pattern_length] == pattern:
                    local_results.append(i)

            if i < end - pattern_length:
                text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + pattern_length])) % prime
                if text_hash < 0:
                    text_hash = text_hash + prime

        return local_results

    with ThreadPoolExecutor(max_workers=num_chunks) as executor:
        futures = [
            executor.submit(process_chunk, i, min(i + chunk_size + pattern_length - 1, text_length))
            for i in range(0, text_length - pattern_length + 1, chunk_size)
        ]
        for future in futures:
            results.extend(future.result())

    return sorted(set(results))

def time_space_complexity(algorithm, text, pattern, num_iteration=50):
    time_complexity=[]
    total_size = 0 
    for i in range (num_iteration):
        start_time = time.time()
        result=algorithm(text, pattern)
        end_time = time.time()
        time_complexity.append(end_time - start_time)
        total_size += sys.getsizeof(result) + sys.getsizeof(text) + sys.getsizeof(pattern)
    avg_time = sum(time_complexity)  / num_iteration
    avg_space = total_size / num_iteration
    return avg_time, avg_space

def visualize_time_complexity(text_lengths, rabin_karp_simplified_times,rabin_karp_times,brute_force_times, rk1_times, rk2_times,rk_paras):
    plt.figure(figsize=(10, 6))
    plt.plot(text_lengths, rabin_karp_simplified_times, label='Simplified Rabin-Karp Time', marker='o', color='g')
    plt.plot(text_lengths, rabin_karp_times, label='Rabin-Karp Time', marker='o', color='b')    
    plt.plot(text_lengths, brute_force_times, label='Brute Force Time', marker='o', color='r')
    plt.plot(text_lengths, rk1_times, label='Rabin-Karp2 Time', marker='o', color='m')
    plt.plot(text_lengths, rk2_times, label='Rabin-Karp3 Time', marker='o', color='y')
    plt.plot(text_lengths, rk_paras, label='Rabin-Karp Parallel Time', marker='o', color='c')
    plt.xlabel('Text Length')
    plt.ylabel('Time (seconds)')
    plt.title('Model Time Comparison')
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()

    plt.show()

def test():
    def generate_text(length, pattern_frequency=0.01, pattern_length=10):
        text = []
        characters = string.ascii_uppercase
        pattern = ''.join(random.choices(characters, k=pattern_length))

        i = 0
        while i < length:
            if random.random() < pattern_frequency:
                text.extend(pattern)
                i += pattern_length
            else:
                text.append(random.choice(characters))
                i += 1

        return ''.join(text[:length]), pattern
     
    rabin_karp_simplified_times = []
    rabin_karp_times = []
    brute_force_times = []
    print(f"{'TextLen':<10}{'PatternLen':<15}{'RK Simplified':<15}{'RK':<10}{'BF':<10}{'RK1':<10}{'RK2':<10}{'RK_par':<10}{'min':<10}")
    print("-" * 150) 
    text_len = [1000, 10000, 100000, 1000000, 10000000]
    frequency=[0.001, 0.01, 0.1,   0.001, 0.001] 
    pattern_len=[5,   10,    15,  20,   50]
    rk_simple_times=[]
    rk_times=[]
    bf_times=[]
    rk1_times=[]
    rk2_times=[]
    rk_paras=[]
    for text_length, freq, pattern_length in zip(text_len, frequency, pattern_len):
        text, pattern = generate_text(text_length, freq, pattern_length)            
        num_iterations=20
        rk_time_simplified, _= time_space_complexity(simplified_rabin_karp, text, pattern, num_iterations)
        rk_time, _= time_space_complexity(rabin_karp, text, pattern, num_iterations) 
        bf_time,_ = time_space_complexity(brute_force_search, text, pattern, num_iterations)
        rk1_time, _= time_space_complexity(rabin_karp1, text, pattern, num_iterations) 
        rk2_time, _= time_space_complexity(rabin_karp2, text, pattern, num_iterations)  
        rk_para, _= time_space_complexity(rabin_karp_parallel, text, pattern, num_iterations) 
        time_dict = {
        'rk_time_simplified': rk_time_simplified,
        'rk_time': rk_time,
        'bf_time': bf_time,
        'rk1_time': rk1_time,
        'rk2_time': rk2_time,
        'rk_para': rk_para}
        min_var = min(time_dict, key=time_dict.get)
        print(f"{text_length:<10}{pattern_length:<15}{rk_time_simplified:<15.6f}{rk_time:<10.6f}{bf_time:<10.6f}{rk1_time:<10.6f}{rk2_time:<10.6f}{rk_para:<10.6f}{min_var:<10}")
        rk_simple_times.append(rk_time_simplified)
        rk_times.append(rk_time)
        bf_times.append(bf_time) 
        rk1_times.append(rk1_time)
        rk2_times.append(rk2_time)
        rk_paras.append(rk_para)
    
    visualize_time_complexity(text_len, rk_simple_times,rk_times,bf_times, rk1_times, rk2_times,rk_paras)
    
if __name__ == "__main__":
    test()


