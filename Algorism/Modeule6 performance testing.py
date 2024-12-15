import random
import string
import timeit
import statistics
from concurrent.futures import ThreadPoolExecutor
base = 256
prime = 211

def brute_force_search(text, pattern):
    brute_force_matches = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            brute_force_matches.append(i)
    return brute_force_matches

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

def alternative_rabin_karp(text, pattern):
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

def rabin_karp2(text, pattern):
    m, n = len(pattern), len(text)

    if m > n:
        return []
    def compute_rolling_hash(s, length):
        h = 0
        for i in range(length):
            h = (h * BASE + ord(s[i])) & 0xFFFFFFFF
        return h

    pattern_hash = compute_rolling_hash(pattern, m)
    text_window_hash = compute_rolling_hash(text, m)

    highest_power = pow(BASE, m - 1, PRIME)

    matches = []

    for i in range(n - m + 1):
        if pattern_hash == text_window_hash:
            if text[i:i+m] == pattern:
                matches.append(i)

        if i < n - m:
            text_window_hash = (
                (text_window_hash * BASE -
                 ord(text[i]) * highest_power +
                 ord(text[i + m]))
                & 0xFFFFFFFF
            )

    return matches

def rabin_karp3(text, pattern): 
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

def rabin_karp_parallel(text, pattern):
    num_chunks = 4  # Number of chunks
    text_length = len(text)
    pattern_length = len(pattern)

    # Ensure chunk_size is at least 1
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

def detailed_performance_analysis():
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

    scenarios = [
        (1_000, 0.001, 5),      # Very short text
        (10_000, 0.01, 10),      # Short text
        (100_000, 0.1, 15),      # Medium text
        (1_000_000, 0.001, 20),  # Large text
        (10_000_000, 0.001, 50)  # Very large text
    ]
    print(f"{scenarios}") 
    print(f"{'Algorithm':^15} | {'Mean Time':^12} | {'Median Time':^12}")
    print("-" * 70)

    for length, freq, pat_len in scenarios:
        text, pattern = generate_text(length, freq, pat_len)

        algorithms = [
            ("Brute Force", brute_force_search),
            ("Alternative Rabin-Karp", alternative_rabin_karp),
            ("Rabin-Karp1", rabin_karp1),
            ("Rabin-Karp2", rabin_karp2)  ,
            ("Rabin-Karp3", rabin_karp3) ,
            ("Rabin-Karp_parallel",rabin_karp_parallel )
        ]

        print(f"Text Length: {length}, Pattern Freq: {freq}, Pattern Len: {pat_len}")

        for name, algo in algorithms:
            times = timeit.repeat(lambda: algo(text, pattern), number=1, repeat=10)

            mean_time = statistics.mean(times)
            median_time = statistics.median(times)

            print(f"{name:20} | {mean_time:12.6f} | {median_time:12.6f}")

        print("\n")

detailed_performance_analysis()

