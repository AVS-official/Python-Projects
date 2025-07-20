s = input("Enter a Sentence: ")
words = s.split(' ')

a = "qwe"
b = "zxc"

coding = input("Type Code(1) for Encrypting\nType Decode(0) for Decrypting\n\nType: ")

if(coding):
    nwords = []
    for word in words:
        if(len(word) >= 3):
            sNew = a + (word[1:] + word[0])[::-1] + b   
            nwords.append(sNew)
        else:
            snew = a + word[::-1] + b
            nwords.append(snew)
    print("".join(nwords))
else:
    nwords = []
    for word in words:
        if(len(word) >= 3):
            sNew = word[::-1][3:-3]
            sNew = sNew[-1] + sNew[:-1]
            nwords.append(sNew)
        else:
            snew = word[::-1][3:-3]
            nwords.append(snew)
    print("".join(nwords))