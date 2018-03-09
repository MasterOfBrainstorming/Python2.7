# This is a bruteforce password list generator where you deside the lenght of the password, password
# starting point and end point(example aaaaaa-bababa), lowercase, uppercase, numbers and special characters.
# The program generates the words into a text file that the user defines
# WARNING lenght that are bigger than 5 strings that have from aaaaa-zzzzz with all atributes
# cost a large amount of harddisk space and are not considered just waste of space.
# If you want to use that method you need to just use bruteforce attack strait away.
# This is merely a test where I test if I manage to pull a somewhat usefull program.

# The reason for this program to exist is that, you can use statitically acquired information to
# limit the passwords for certain atributes lenght and range

# There is also an option to make a social hacking wordlist of the specific victim,
# of course you need to use cewl to acquire the information or to manuallyt dig them.
# This is a good method if you get large amount of information of the victim.

# 1. option for bruteforce list parameters are:
#       lenght, smallcase/uppercase, numbers, special characters,

# 2. option for social wordlist parameters are:
#       victims full name,age, music, country, sibling name/nicknames+age, parents full name+age,
#       bestfriend+nickname, workplace,job,, car, hobbies, nickname,


import itertools
import re
import os
import time
import sys
import string

class ERROR_USER_INPUT(Exception):
    pass

def brute_attack():
    pass
def list_brute_attack():
    pass

def elite_list(passwd):
    elitechr = {"a":4,
                "e":3,
                "s":5,
                "i":1,
                "o":0,
                "z":2}
    pass

def social_attack():
    pass

# This is the answer function that is called through the program. The fucntion just parses the input
# so that if a user inputs Y or y / N or n as the first character, it will return a 1 or 0
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

# NOTE TO SELF
# In PROGRESS, implement into the file writing

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

# This is the brutelist that defines the output.
# First there are objects for lowercase, uppercase, numbers and special characters
# NOTE TO SELF (could be inside a dictionary)

# Formatting the brute

# The user will be prompted with 4 question where he answers eather yes or no.

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

# The Function will ask the user for input the lenght of the pasword, then just compares the output
# with the input and if it is 6 or over then the user will be prompted with a warning.
# If the warning returns as 1 then the code will proceed and will send the lenght to the function
# brute_list

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

# First thing that pops up, these are the asnwers to the question at start.
# [Option 1] call the function password leght
# [Option 2] doesm't do anything at the momement, same goes for the rest of all
# except the [Option 0] which exits
    
def main():
    
    print "1=bruteforce list\n2=social list\n3=use the wordlist"\
              "\n4=brute attack,\n5=social attack\n6=Word combination\n\n0=EXIT"
    try:
        option = int(raw_input("[+] Choose an option:\n   >"))
        if option in [1,2,3,4,5,6,0]:
            if option == 1:
                dobrutelist = password_lenght()
                return dobrutelist
            elif option == 2:
                doelitelist = elite_list()
                return doelitelist
            elif option == 3:
                listbruteattack == list_brute_attack()
                return dobruteattack
            elif option == 4:
                dobruteattack == brute_attack()
            elif option == 5:
                dosocialattack == social_attack()
            elif option == 6:
                parse_user_range()
                #dowordcombination == word_combination()
            elif option == 0:
                exit()
        elif len(option)>2:
            print "Input one number only"
    except Exception as e:
        print "\n-Please use the numbers assingned-\n"
    
while True:
    if __name__=="__main__":
        main()
