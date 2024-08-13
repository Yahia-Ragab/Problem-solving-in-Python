def find_it(seq):
    digit=list(seq)
    i=0
    while i<len(seq):
        pop=digit.pop()
        num=seq.count(pop)
        if num%2!=0:
            return pop