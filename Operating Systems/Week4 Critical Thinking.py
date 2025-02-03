
#Week4 Critical Thinking Comparing First_Fit and Best_Fit Algorithms

def first_fit(memory_blocks, process_sizes):
    allocation = [-1] * len(process_sizes)    
    for i in range(len(process_sizes)):
        for j in range(len(memory_blocks)):
            if memory_blocks[j] >= process_sizes[i]:
                allocation[i] = j
                memory_blocks[j] -= process_sizes[i] #memory_blocks[j] = -1
                break
                
    return allocation, memory_blocks 

def best_fit(memory_blocks, process_sizes):
    allocation = [-1] * len(process_sizes)    
    for i in range(len(process_sizes)):
        best_idx = -1
        min_size = float('inf')
        for j in range(len(memory_blocks)):
            if memory_blocks[j] >= process_sizes[i]:
                if memory_blocks[j] < min_size:
                    min_size = memory_blocks[j]
                    best_idx = j

        if best_idx != -1:
            allocation[i] = best_idx
            memory_blocks[best_idx] -= process_sizes[i]
                
    return allocation, memory_blocks 
 
def display_outcome (allocation, remaining_memo):
    print(f"{'Process No.':<15}{'Process Size':<15}{'Block No.':<15}{'Remaining Memory':<15}")
    for i in range(len(process)):
        if allocation[i] != -1:
            block_num = allocation[i] + 1 
            rem_mem = remaining_memo[allocation[i]]
        else:
            block_num = "Not Allocated"
            rem_mem = "N/A"
        print(f"{i+1 :<15}{process[i]:<15}{block_num:<15}{rem_mem:<15}")

if __name__ == "__main__":
    memory = [100, 700, 200, 300, 600, 400]
    process = [220, 417, 112, 601, 50]

    allocation, remaining_memo = first_fit(memory.copy(), process)
    print('First_Fit Algorithm')
    display_outcome (allocation, remaining_memo)
    allocation, remaining_memo = best_fit(memory.copy(), process)
    print('Best_Fit Algorithm')
    display_outcome (allocation, remaining_memo)




