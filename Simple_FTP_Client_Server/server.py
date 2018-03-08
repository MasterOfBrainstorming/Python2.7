import os
import sys
import socket
import logging


#if len(sys.argv) < 2:
#       print "Usage: python ftp_server.py localhost, port"
#       sys.exit(1)



logging.basicConfig(filename="server_log.txt",level=logging.DEBUG)

methods = [
        "LIST",
        "LISTRESPONSE",
        "DOWNLOAD",
        "FILE",
        "ERROR"
        ]

class FOLDER_ERROR(Exception):
        pass
        #FOLDER ERROR RESPONSE CODE IS 1
class PARAMETER_ERROR(Exception):
        pass
        #PARAMETER ERROR RESPONSE CODE IS 2
class FILE_ERROR(Exception):
        pass
        #PARAMETER ERROR RESPONSE CODE IS 3
class FTP_ERROR(Exception):
        pass

def list_response(request):
        if len(request[0]) == 1:
                print "Request is error:", request
                return request
                logging.info(request)
        else:
                print "LIST RESPONSE", request
                logging.warning(request)
                lenght = 0
                for r in request:
                        x = len(r)
                        lenght+=x
                items = len(request)
                body = request
                item_list = "\r\n".join(request)
                response = "%s %s %s\r\n%s" % ("LISTRESPONSE", lenght, items, item_list)
                return response
                logging.info(response)

def parse_list_request(request):
        parts = request.split(" ")
        if parts[2] == ".":
                server_list = os.listdir(os.getcwd())
                return server_list
                print "Server list: ", server_list
        elif parts[2] != ".":
                try:
                       search_folder(parts[2])
                       return search_folder(parts[2])
                except Exception as e:
                        print e
                        for x in e:
                                if "1" in x:
                                        return "1"
                                elif "2" in x:
                                        return "2"
                                elif "3" in x:
                                        return "3"
                                else:
                                        return "ERROR"
                #return search_folder(parts[2])

        

def search_folder(folder):
        folder_list = os.listdir(os.getcwd())
        print folder
        if folder not in folder_list:
                raise FOLDER_ERROR("1: Listing folder contents error, folder not found")
        else:
                lista = os.listdir(folder)
                return lista
             

def get_file_contents(file):
        print "Get file contents",file
        f = open(file, "r")
        body = ""
        for j in f:
                body+=j
                body+="\n"
                size = len(j)
        return body, size

def parse_download_request(request):
        parts = request.split(" ")
        file = parts[2]
        print parts
        #valid_file = search_file(file)
        try:
                search_file(file)
                file_contents = get_file_contents(file)
                file_lenght = file_contents[1]
                file_contents_to_string = "%s" % (file_contents[0])
                response = "%s %s %s %s %s %s" % ("FILE", str(file_lenght), search_file(file),"\r\n", file_contents_to_string,"\n")
                return response
        except Exception as e:
                for x in e:
                        if "1" in x:
                                return "1"
                        elif "2" in x:
                                return "2"
                        elif "3" in x:
                                return "3"
                        else:
                                return "ERROR"
                logging.warning(e)
                #return e

def find_from_folder(line):
    items = line.split("/")
    directory = items[0]
    file = items[1]
    print "Dir:", directory, "File:", file
    if directory not in os.listdir(os.getcwd()):
        raise FOLDER_ERROR("1: Folder not found or it is a file")
        return 1
    elif "." not in file:
        raise PARAMETER_ERROR("2: Given parameter is a folder, cannot download")
        return 2
    elif file not in os.listdir(directory):
        raise FILE_ERROR("3: File not found")
        return 3
    else:
        return file
def find_file(line):
    if line not in os.listdir(os.getcwd()):
        raise FILE_ERROR("3: File not found")
        return 3
    elif "." not in line:
        raise PARAMETER_ERROR("2: Given parameter is a folder")
        return 2
    else:
        return line


def search_file(line):
        if "/" in line:
                fff = find_from_folder(line)
                return fff
        else:
                ff = find_file(line)
                return ff
    
def check_validation(line):
        parts = line.split(" ")
        if parts[0] not in methods:
                raise FTP_ERROR("Not a valid FTP method")
        elif len(parts) < 3 or len(parts) !=3:
                raise FTP_ERROR("request lenght not valid")
        elif int(parts[1]) !=0:
                close_connection()
                raise FTP_ERROR("non-zero body lenght")
        status = True
        return line, status

def parse_request(request):
        try:
                check_validation(request)
                code = check_validation(request)[1]
        except Exception, e:
                print e
        #check = check_validation(request)
        #code = check[1]
        parts = request.split(" ")
        method = parts[0]
        if method == "LIST" and code == True:
                lista = parse_list_request(request)
                print "parsen palautus:", lista
                response = list_response(lista)
                return response
        elif method == "DOWNLOAD" and code == True:
                down = parse_download_request(request)
                return down

def ftp_server():
        #host = sys.argv[1]
        #port = int(sys.argv[2])
        host = "localhost"
        port = 1222
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
                server.bind((host, port))
                server.listen(5)
                print "Listening on port", port, "@", host
        except Exception, e:
                print e
        (client, addr) = server.accept()
        request = client.recv(1024)
        while request != "":
                print addr, "Requested", request
                response = parse_request(request)
                logging.info(response)
                print "Response to", addr, "is:",response
                client.send(str(response))
                request = ""
        server.close()
while True:
	ftp_server()


