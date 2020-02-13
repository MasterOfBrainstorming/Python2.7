
import itertools
import re
import os
import time
import sys
import string

class ERROR_USER_INPUT(Exception):
    pass




def answer():
    try:
        answ = raw_input("Yes/No >")
        answer = answ[0]
        if answer in ["Y","y"]:
            return 1
        elif answer in ["n","N"]:
            return 0
    except Exception as e:
        print "Wrong input"



def proggress_bar():
    width = 40

    sys.stdout.write("[%s]" %(" " * width))
    sys.stdout.flush()
    sys.stdout.write("\b"*(width+1))

    for i in xrange(width):
        time.sleep(0.1)
        sys.stdout.write("-")
        sys.stdout.flush()
    sys.stdout.write("\n")


def brute_list(lenght):
    chars = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special = '!"'+"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    brute = []
    print "[+] Password uses lowercase:"
    answ1 = answer()
    print "[+] Password uses uppercase:"
    answ2 = answer()
    print "[+] Password uses numbers:"
    answ3 = answer()
    print "[+] Password uses special characters:"
    answ4 = answer()
    filename = makefile()
    with open(filename,"wb") as save:
        
        print """
                ***************************************************************
                PLEASE WAIT. Creating %s file, this may take time
                [+] Start Time: """%(filename), time.strftime('%H:%M:%S')
        if answ1 == 1:
            if answ2 == 1:
                if answ3 == 1:
                    if answ4 == 1:
                        for word in itertools.product(chars+uppercase+numbers+special,repeat=lenght):
                            save.write("".join(word)+"\n")
                    else:
                        for word in itertools.product(chars+uppercase+numbers,repeat=lenght):
                            save.write("".join(word)+"\n")
                else:
                    if answ4 == 1:
                        for word in itertools.product(chars+uppercase+special,repeat=lenght):
                            save.write("".join(word)+"\n")
                    else:
                        for word in itertools.product(chars+uppercase,repeat=lenght):
                            save.write("".join(word)+"\n")
            else:
                if answ3 == 1:
                    if answ4 ==1:
                        for word in itertools.product(chars+numbers+special,repeat=lenght):
                            save.write("".join(word)+"\n")
                    else:
                        for word in itertools.product(chars+numbers,repeat=lenght):
                            save.write("".join(word)+"\n")
                else:
                    if answ4 == 1:
                        for word in itertools.product(chars+special,repeat=lenght):
                            save.write("".join(word)+"\n")
                    else:
                        for word in itertools.product(chars,repeat=lenght):
                            save.write("".join(word)+"\n")
        else:
            if answ2 == 1:
                if answ3 == 1:
                    if answ4 == 1:
                        for word in itertools.product(uppercase+numbers+special,repeat=lenght):
                            save.write("".join(word)+"\n")
                    else:
                        for word in itertools.product(uppercase+numbers,repeat=lenght):
                            save.write("".join(word)+"\n")
                else:
                    if answ4 == 1:
                        for word in itertools.product(uppercase+special,repeat=lenght):
                            save.write("".join(word)+"\n")
                    else:
                        for word in itertools.product(uppercase,repeat=lenght):
                            save.write("".join(word)+"\n")
        
            else:
                if answ3 == 1:
                    if answ4 == 1:
                        for word in itertools.product(numbers+special,repeat=lenght):
                            save.write("".join(word)+"\n")
                    else:
                        for word in itertools.product(numbers,repeat=lenght):
                            save.write("".join(word)+"\n")
                else:
                    if answ4 == 1:
                        for word in itertools.product(special,repeat=lenght):
                            save.write("".join(word)+"\n")
                    else:
                        print "--------------------------------\n"\
                                "You didn't choose any parameters\n"\
                                "--------------------------------"
    save.close()
    fsize = os.stat(filename)
    print """
                [+] %s'%s' size: %ibytes [+]                       
                [-] End Time: """%("Bruteforce list created in ",filename, fsize.st_size)\
                , time.strftime('%H:%M:%S')+"""
                ***************************************************************"""


    
def parse_user_range(lenght):
    usr = raw_input("Input a starting point example aaaaa-zzzzz:\n   >")
    lst_u= []
    lst_u += "".join(usr.split("-"))
    if lenght*2 == len(lst_u):
        p = ""
        lst =[]
        for i in lst_u:
            p += str(ord(i))+" "
        print p
        lst+= "".join(p.split(","))
        
        
        print "jes"
    else:
        print "nope"
    #NOTE TO SELF USE MAP TO GET THE MIN MAX ENDPOINT 

                   
def makefile():
    try:
        filename = raw_input("[+] Input savefile name:\n   >")
        if filename in [""," "]:
            return "brutelist.txt"
        
        elif filename[1].split(".") != "txt":
            return filename + ".txt"
        return filename
    except Exception as e:
            print "failed to make a file"



def password_lenght():
    answ = int(raw_input("[+] How many characters in the password?\n   >"))
    if answ >= 6:
        print "!!!CAUTION the bruteforce list can make extremely large files!!!\n"\
              "Would you like to proceed?"
        caution = answer()
        if caution == 1:
            brute_list(answ)
            test = parse_user_range(answ)
        elif caution == 0:
            return
    elif answ < 6:
        test = parse_user_range(answ)
        brute_list(answ)


    
def main():
    
    print "1=bruteforce list\n\n0=EXIT"
    try:
        option = int(raw_input("[+] Choose an option:\n   >"))
        if option in [1,2,0]:
            if option == 1:
                dobrutelist = password_lenght()
                return dobrutelist
            elif option == 2:
                doelitelist = elite_list()
                return doelitelist
            
            elif option == 0:
                exit()
        elif len(option)>2:
            print "Input one number only"
    except Exception as e:
        print "\n-Please use the numbers assingned-\n"
    
while True:
    if __name__=="__main__":
        main()
