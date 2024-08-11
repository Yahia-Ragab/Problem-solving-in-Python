def max(n1,n2):
    if n1>n2: return n1
    else: return n2
def set(elements):
    unique_elements = []
    for element in elements:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements
def count(s,c):
    counter=0
    for i in range(len(s)):
        if(s[i]==c):
            counter=counter+1
    return counter
def len(s):
    counter=0
    for c in s:
        counter =counter+1
    return counter
def balanced_recursive(s,start,end):
    if len(set(s)) == 1: return 0
    if start >= end:
        return 0
    unique_char = set(s[start:end])
    if len(unique_char) == 2:
        c1, c2 = unique_char
        if count(s[start:end],c1) == count(s[start:end],c2):
            return end - start
    length1 = balanced_recursive(s,start + 1, end)
    length2 = balanced_recursive(s,start, end - 1)
    return max(length1, length2)

def balanced(s):
    if set(s) == 1:
        return 0
    else:
        length = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                substring = s[i:j+1]
                unique_char = set(substring)
                if len(unique_char) == 2:
                    c1, c2 = unique_char
                    if count(substring,c1) == count(substring,c2):
                        length = max(length, len(substring))
    return length