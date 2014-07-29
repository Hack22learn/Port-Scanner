# ___________MAIN MODULE___________________
#  V-1.0
# Port Scanner 
__author__ = "Sudhanshu Patel (sudhanshuptl13@gmail.com)"

import subprocess
from datetime import datetime
import socket ,sys

class portscan():
    def __init__(self,remoteServer):
        '''Initiate port scanner'''
        self.remoteServer=remoteServer
        self._port_ls=[21, 22, 23, 25, 53, 53, 80, 81, 110, 111,119, 123, 135, 139, 143, 161, 443, 445,465,563,587,902,912,993,995, 1024, 1723, 3389, 4567, 5000,5631, 8080, 8081,9601]
        # Some of most common port
        try:
            self.remoteServerIP=socket.gethostbyname(remoteServer) #Resolving IP of host
        except:
            print "Unable to fetch Host"

    def scanport(self):
        '''
           Using Range Function to specify ports (here We scan all port in range 1 to 1024
           we also create some Error handler to handle Error
        '''
        print "be patience , it will take time..."
        try:  #Exception Handling
            for port in range(1,1024):#self._port_ls:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((self.remoteServerIP, port))
                if result == 0:  #If port is open(i.e using this port we can connect to host )
                    print "Port {}: \t Open".format(port) #print port
                sock.close() #close Socket
        except KeyboardInterrupt:
            print "You pressed Ctrl+C"
            sys.exit()

        except socket.gaierror:
            print 'Hostname could not be resolved. Exiting'
            sys.exit()
        except socket.error:
            print "Couldn't connect to server"
            sys.exit()
        



if __name__=='__main__':
    
    #Clear Screen
    #subprocess.call('clear',shell=True)
    
    # Information for User
    print "Enter a remote host to scane Ex:- www.nitrkl.ac.in\n"+"-"*60
    print (" "*29)+"OR\n"+"_"*60
    print "Enter a remote computer name in your local network  Ex:- Jai_Hind\n"+"-"*60

    #Ask for input and create object scan
    scan=portscan(raw_input('Enter a remote host to scan : '))

    # Scanning Port and printing Result
    scan.scanport()
    print """
                        We r Done !!
                          Thank You!!"
                        """
    raw_input()
    
