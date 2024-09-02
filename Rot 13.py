def rot13(message):
    letter=[]
    for c in message:
        if not c.isalpha():
            letter.append(c)

        elif c.isupper():
            word=ord(c)+13
            if word>ord('Z'):
                word=word-26
            letter.append(chr(word))
        else:
            word=ord(c)+13
            if word>ord('z'):
                word=word-26
            letter.append(chr(word))
    return ''.join(letter)
