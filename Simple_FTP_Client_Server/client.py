import socket
import logging




logging.basicConfig(filename="client_log.txt",level=logging.DEBUG)

methods = [
        "LIST",
        "LISTRESPONSE",
        "DOWNLOAD",
        "FILE",
        "ERROR"]

def parse_request(line):
        parts = line.split(" ")
        if parts[0] not in methods:
                raise FTP_ERROR("Not a valid FTP method")
        elif len(parts) < 3 or len(parts) !=3:
                raise FTP_ERROR("request lenght not valid")
        elif int(parts[1]) !=0:
                close_connection()
                raise FTP_ERROR("non-zero body lenght")
        return line 
                
#JUST FOR TESTING
def close_connection(x=False):
        return x
class FTP_ERROR(Exception):
        pass

def client_connection(request):
        host = "localhost"
        port = 1222
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
                client.connect((host, port))
                "Connected to", host, "@", port
        except Exception, e:
                print e
        sending = client.send(str(request))
        response = client.recv(1024)
        response_error_code = response.isdigit()
        if response_error_code:
                return "ERROR %s" % response
                logging.warning(response)
                client.close()
        else:
                return response
                logging.info(response)
                client.close()
               

def request_list_objects():
        print "1: LIST ALL FILES"
        print "2: LIST FILES IN DIR"
        listing = int(raw_input("->"))
        if listing == 1:
                list_all = "LIST 0 ."
                return list_all
        elif listing == 2:
                directory = raw_input("Directory name: ")
                list_dir = "LIST 0 " + directory
                return list_dir
def request_download_file():
        file_to_download = raw_input("File name: ")
        line = "DOWNLOAD 0 " + file_to_download
        return line

def client_validation():
        method = int(raw_input("What to do? -->"))
        if method == 1:
                do_request = request_list_objects()
                return do_request
        elif method == 2:
                do_request = request_download_file()
                return do_request
        elif method == 3:
                print "Thanks for using FTP client"
                sys.exit(1)
        elif method == 4:
                read_logs()


while True:
        print "FTP Client"
        print "1: List files on server"
        print "2: Download file"
        print "3: Close connection"
        print "4: Read logs"
        create_request = client_validation()
        logging.info(create_request)
        if create_request:
                client = client_connection(create_request)
                logging.info(client)
                print str(client)
                print 15 * "-"

        
