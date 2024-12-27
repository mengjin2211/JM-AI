
import random
import string
from datetime import datetime, timedelta
import time 
import sys
import matplotlib.pyplot as plt
 
base=256
prime=211

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

def validation(text, pattern):
    rabin_karp_result = rabin_karp(text, pattern)
    brute_force_result=brute_force_search(text, pattern)
    if rabin_karp_result==brute_force_result:
        print ('rabin_karp_result validated')
    else: print (f'rabin_karp_result is different from brute force: rk {rabin_karp_result}; bf {brute_force_result}' )

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

def visualize_time_complexity(text_lengths, rabin_karp_times, rabin_karp_simplified_times, brute_force_times):
    plt.figure(figsize=(10, 6))
    plt.plot(text_lengths, rabin_karp_times, label='Rabin-Karp Time', marker='o', color='b')
    plt.plot(text_lengths, rabin_karp_simplified_times, label='Simplified Rabin-Karp Time', marker='o', color='g')
    plt.plot(text_lengths, brute_force_times, label='Brute Force Time', marker='o', color='r')    
    plt.xlabel('Text Length')
    plt.ylabel('Time (seconds)')
    plt.title('Time Complexity of Rabin-Karp vs Brute Force')
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    plt.show()

def visualize_space_complexity(text_lengths, rabin_karp_space, rabin_karp_simplified_space, brute_force_space):
    plt.figure(figsize=(10, 6))
    plt.plot(text_lengths, rabin_karp_space, label='Rabin-Karp Space', marker='o', color='b')
    plt.plot(text_lengths, rabin_karp_simplified_space, label='Simplified Rabin-Karp Space', marker='o', color='g')
    plt.plot(text_lengths, brute_force_space, label='Brute Force Space', marker='o', color='r')
    
    plt.xlabel('Text Length')
    plt.ylabel('Space (bytes)')
    plt.title('Space Complexity of String Search Algorithms')
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    plt.show()

def main(): 
    # text_validate, pattern_validate = generate_text(1000, 0.001, 3)  
    # validation(text_validate,pattern_validate) # This is only needed for initial checks.  
    rabin_karp_simplified_times = []
    rabin_karp_times = []
    brute_force_times = []
    rk_simiplified_spaces = []
    rk_spaces = []
    bf_spaces = []

    print(f"""{'Text Length':<15}{'Pattern Length':<15}{'RK Simplified Time':<20}{'Rabin-Karp Time':<20}{'Brute Force Time':<20}{'RK Space':<20}{'BF Space':<20}""")

    print("-" * 120) 
 
    text_len = [1000, 10000, 100000, 1000000, 10000000]
    frequency=[0.001, 0.01, 0.1,   0.001, 0.001] 
    pattern_len=[5,   10,    15,  20,   50]

    for text_length, freq, pattern_length in zip(text_len, frequency, pattern_len):
        text, pattern = generate_text(text_length, freq, pattern_length)           
        num_iterations=20
               
        rk_time_simplified, rk_simiplified_space= time_space_complexity(simplified_rabin_karp, text, pattern, num_iterations)
        rk_time, rk_space= time_space_complexity(rabin_karp, text, pattern, num_iterations) 
        bf_time,bf_space = time_space_complexity(brute_force_search, text, pattern, num_iterations)  
               
        print(f"{text_length:<15}{pattern_length:<15}{rk_time_simplified:<20.6f}{rk_time:<20.6f}{bf_time:<20.6f}{rk_space:<20.2f}{bf_space:<20.2f}")

        rabin_karp_simplified_times.append(rk_time_simplified)
        rabin_karp_times.append(rk_time)
        brute_force_times.append(bf_time) 
        rk_simiplified_spaces.append(rk_simiplified_space)
        rk_spaces.append(rk_space)
        bf_spaces.append(bf_space) 
     
    visualize_time_complexity(text_len, rabin_karp_times,rabin_karp_simplified_times,brute_force_times)
    visualize_space_complexity(text_len, rk_spaces, rk_simiplified_spaces, bf_spaces )


if __name__ == "__main__":
    main()

