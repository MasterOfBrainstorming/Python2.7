maxlen = 26
minlen = 0
import string
 
while True:
    k = list(string.ascii_lowercase)
 
    def userinputs():
        print """
        1.Encrypt
        2.Decrypt
        3.Quit"""
        try:
            i = int(raw_input("Choose:\n>>>"))
        except TypeError:
            print "Please input a number"
        if i == 1:
            question(i)
        elif i == 2:
            question(i)
        elif i == 3:
            quit
        else:
            print "Not a valid value!!!!"
 
    def question(i):
        try:
            inp = raw_input("Message:\n>>>")
            try:
                roll = int(raw_input("Insert a key:\n>>>"))
                while roll >= maxlen or roll <= minlen:
                    roll = int(raw_input("Please input the shift between 0-26:\n>>>"))
            except TypeError:
                print "Type a number"
        except TypeError:
            print "Please input words only"
        finally:
            rolli(inp,roll,i)
 
 
 
    def rolli(inp,x,i):
        indexlocation = []
        smbig = []
        for s in inp:
            for b in k:
                if b == s:
                    smbig.append(0)
                    indexlocation.append(k.index(b))
                elif b.upper()==s:
                    indexlocation.append(k.index(b))
                    smbig.append(1)
  #print "The index locations of the characters:\n", indexlocation
        if i == 1:
            shifting(x,indexlocation,smbig)
        elif i == 2:
            shifting(x*-1,indexlocation,smbig)
 
 
#a function for shifting list of characters for ciphering
 
 
    def shifting(x,ilist,smbig):
        rlist = k[x:] + k[:x]
        text=[]
        i=0
        print " ".join(k)
        print " ".join(rlist)
        for n in ilist:
            for l in rlist:
                if n == rlist.index(l):
                    text.append(l)
 
        while i < len(smbig):
            if smbig[i] == 1:
                temp = text[i]
                text.pop(i)
                text.insert(i,temp.upper())
                i=i+1
            else:
                i=i+1
 
        if x < 0:
            print "The decrypted text:","".join(text)
        else:
            print "The ciphered text:\n", "".join(text)
 
    userinputs() 
