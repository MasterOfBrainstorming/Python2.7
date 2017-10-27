import string
 
def withkeyword(i):
    while 25>=i:
        declist = []
        nwlist = listofchar[i:] + listofchar[:i]
        for r in indexlist:
            for o in nwlist:
                if r == nwlist.index(o):
                    declist.append(o)
                    x= "".join(declist)
            if keyword in x:
                s = 26-i
                return (-s)
        i = i + 1
 
 
def withoutkeyword(i,biglist):
    while 25>=i:
        text = []
        l = 0
        nwlist = listofchar[i:] + listofchar[:i]
        for r in indexlist:
            for o in nwlist:
                if r == nwlist.index(o):
                    text.append(o)
 
        while l < len(biglist):
            if biglist[l] == 1:
                temp = text[l]
                text.pop(l)
                text.insert(l,temp.upper())
                l=l+1
            else:
                l=l+1
        i = i + 1
        print "Key",27-i,":","".join(text)

 
def foundkey(s,biglist):
    text = []
    nwlist = listofchar[s:] + listofchar[:s]
    i=0
 
    for r in indexlist:
        for o in nwlist:
            if r == nwlist.index(o):
                text.append(o)
 
    while i < len(biglist):
        if biglist[i] == 1:
            temp = text[i]
            text.pop(i)
            text.insert(i,temp.upper())
            i=i+1
        else:
            i=i+1
    print "Key",abs(s),":","".join(text),"\n\n\n"
 
 
while True:
    listofchar = list(string.ascii_lowercase)
    i=0
    indexlist = []
    biglist = []
    ciphtxt = raw_input("Insert ciphered text for Bruteforce:\n>>>")
    keyword = raw_input("Insert keyword(Optional):\n>>>")
 
    for a in ciphtxt:
        for b in listofchar:
            if b == a:
                indexlist.append(listofchar.index(b))
                biglist.append(0)
            elif b.upper() == a:
                indexlist.append(listofchar.index(b))
                biglist.append(1)
    if keyword != "":
        s=withkeyword(i)
        foundkey(s,biglist)
    else:
        withoutkeyword(i,biglist) 
