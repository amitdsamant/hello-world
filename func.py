

def even_odd(A):
    next_even, next_odd = 0, len(A)-1 #setting the start and end of list
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even],A[next_odd] = A[next_odd],A[next_even]
            next_odd -= 1

A = [5,2,6,1,7,4,9,6]
even_odd(A)
print(A)
