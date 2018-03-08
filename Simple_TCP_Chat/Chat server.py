import socket, time, os, select, threading

class SERVER_ERROR(Exception):
    pass


def server_connection():
    host = "localhost"
    port = 6421
    clients = []

    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host,port))
        s.setblocking(0)
        #s.listen(5)
        print "Server running %s @ %i" %(host,port)
    except Exception as e:
        print e

    #(client, addr) = s.accept()
    #request = client.recv(1024)
    quitting = False
    while not quitting:
    #while request != "":
        try:
            data, addr = s.recvfrom(1024)
            if "Quit" in str(data) or quit in str(data):
                quitting = True 

            if addr not in clients:
                clients.append(addr)
            print time.ctime(time.time()) + str(addr) + ": :" + str(data)
            for client in clients:
                s.sendto(data,client)
        except:
            pass
            #raise SERVER_ERROR("")
    s.close()


    


while True:
    server_connection()



