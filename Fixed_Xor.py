# Fixed XOR
# Write a function that takes two equal-length buffers and produces their XOR combination.
# If your function works properly, then when you feed it the string:
# 1c0111001f010100061a024b53535009181c
# ... after hex decoding, and when XOR'd against:
# 686974207468652062756c6c277320657965
# ... should produce:
# 746865206b696420646f6e277420706c6179

print """
                FIXED XOR:
                0+0=0
                1+1=0
                1+0=1
                0+1=1"""

#Function to convert feed and key to binary
def converting(feed, key,xor):
    feedtobinary = bin(int(feed,16))[2:]
    keytobinary = bin(int(key,16))[2:]
    #Filling binary feed to same lenght as key, we fill zeroes to the end 
    feedtobinary = feedtobinary.zfill(len(keytobinary))
    xorred = xorring(feedtobinary,keytobinary,xor)
    return xorred

#Function used to xor the feed    
def xorring(feed,key,xor):
    #For loop used with zip to go through both lists at the same time and comparing
    #values if the values are same then a 0 will be added to the xord string
    #if values differ then a 1 will be added.
    for x, y in zip(feed,key):
        if x == y:
            xor=xor+"0"
        else:
            xor=xor+"1"
    return xor

#While loop to run the program as long you need it
while True:
    print """
            Encrypting with XOR:
                1)Raw input
                2)Fixed
                3)Exit
                
"""
    xor = ""
    usr_inp = raw_input("Choose:\n>>>")
    if usr_inp == "1":
        feed = raw_input("Input a Xorred input to be decrypted:\n>>>")
        key = raw_input("Key to decrypt the Xorred input:\n>>>")
        output = converting(feed,key,xor)
        print "Feed: %s\nKey: %s\nCiphered HEX: %s" % (feed,key,hex(int(output,2))[2:-1])
    elif usr_inp == "2":
        output = converting("1c0111001f010100061a024b53535009181c","686974207468652062756c6c277320657965",xor)
        print "Feed: %s\nKey: %s\nCiphered HEX: %s" % ("1c0111001f010100061a024b53535009181c","686974207468652062756c6c277320657965",hex(int(output,2))[2:-1])
    elif usr_inp == "3":
        exit()
    else:
        print "Please choose between 1-3"
