s = input("Enter a Message: ")
words = s.split(' ')

coding = int(input("Enter 1 for coding and 0 for decoding: "))

if(coding == 1):
    nwords = []
    for word in words:
        if(len(word) >= 3):
            r1 = "aef"
            r2 = "pse"
            s1 = r1 + word[1:] + word[0] + r2
            nwords.append(s1)
        else:
            nwords.append(word[::-1])
    print(' '.join(nwords))
if(coding == 0):
    nwords = []
    for word in words:
        if(len(word) >= 3):
            r1 = "aef"
            r2 = "pse"
            s1 = word[3:-3]
            s3 = s1[-1] + s1[:-1]
            nwords.append(s3)
        else:
            nwords.append(word[::-1])
    print(' '.join(nwords))