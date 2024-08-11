def count_bits(n):
    binary=[]
    while(0<n):
        binary.insert(0,n%2)
        n=n//2
    return binary.count(1)