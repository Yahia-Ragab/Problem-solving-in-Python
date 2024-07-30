def is_ending(word,check):
    # return word.endswith(check) lazy answer
    if(check==''and word==''):
        return True
    elif(check==""or word==''):
        return False
    word=word.lower()
    check=check.lower()
    return word[-(len(check))::] == check
print(is_ending('Yahia','hIA'))
#time O(n)