def counting_sort(A):
  
    k = max(A)

    C = [0] * (k + 1)
    B = [0] * len(A)
    
    for num in A:
        C[num] += 1
    
    
    for i in range(1, len(C)):
        C[i] += C[i - 1]
  
    for num in reversed(A):  
        B[C[num] - 1] = num
        C[num] -= 1
    
    return B

#Example
A = [4, 2, 2, 8, 3, 3, 1, 5, 7, 5]
sorted_A = counting_sort(A)
print("Sorted Array:", sorted_A)
