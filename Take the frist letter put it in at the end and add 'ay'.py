def pig_it(text):
    newtext=''
    text=text.split(' ')
    for i in text:
        if i.isalpha():
            last=i[0]
            i=i[1:]
            newtext=newtext+" "+i+last+'ay'
        else:
            newtext = newtext + " " + i
    return newtext.strip()

print(pig_it("Pig latin is cool ?"))