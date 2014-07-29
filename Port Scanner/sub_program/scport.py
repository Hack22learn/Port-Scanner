from datetime import datetime
import socket,sys 

class Portscan():
    def __init__(self,remoteServer):
        '''Initiate port scanner'''
        self.remoteServer=remoteServer
        self._port_ls=[21, 22, 23, 25, 53, 53, 80, 81, 110, 111,119, 123, 135, 139, 143, 161, 443, 445,465,563,587,902,912,993,995, 1024, 1723, 3389, 4567, 5000,5631, 8080, 8081,9601]
        # Some of most common port
        try:
            self.remoteServerIP=socket.gethostbyname(remoteServer) #Resolving IP of host
            print '*'*80
            print '          Host ;-     "',remoteServer,'"      and its IP :-   "',self.remoteServerIP,'"'
            print '*'*80
        except:
            print "Unable to fetch Host"
            

    def Scan_common_port(self):
        '''
           We check for all commonly used  port .....
        '''
        print "................Be Patience , it will take time.................."
        print '..........We check for some commonly used Port ....'

        output_port=[]
        try:  #Exception Handling
            for port in self._port_ls:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((self.remoteServerIP, port))
                if result == 0:  #If port is open(i.e using this port we can connect to host )
                    print "Port {}: \t Open".format(port) #print port
                    output_port.append(port)
                sock.close() #close Socket

            print ' \n        We r Done!!  '
            return output_port
                
                
        except KeyboardInterrupt:
            print "You pressed Ctrl+C"
            sys.exit()

        except socket.gaierror:
            print 'Hostname could not be resolved. Exiting'
            sys.exit()
        except socket.error:
            print "Couldn't connect to server"
            sys.exit()
        
    
    def Brute_scan(self):
        '''
           Using Range Function to specify ports (here We scan all port in range 1 to 1024
           we also create some Error handler to handle Error
        '''
        print "....................Be Patience , it will take time.................... "
        print ' We Gonna Check for All port in range 0 to 1024 '

        output_port=[]
        try:  #Exception Handling
            for port in range(0,1025):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((self.remoteServerIP, port))
                if result == 0:  #If port is open(i.e using this port we can connect to host )
                    print "Port {}: \t Open".format(port) #print port
                    output_port.append(port)
                sock.close() #close Socket

            print ' \n        We r Done!!  '
            return output_port
                
                
        except KeyboardInterrupt:
            print "You pressed Ctrl+C"
            sys.exit()

        except socket.gaierror:
            print 'Hostname could not be resolved. Exiting'
            sys.exit()
        except socket.error:
            print "Couldn't connect to server"
            sys.exit()

    def Given_Portscan(self,ls=[1]):
        '''
           Using Range Function to specify ports (here We scan all port in range 1 to 1024
           we also create some Error handler to handle Error
        '''
        print "....................Be Patience , it will take time.................... "
        print ' We Gonna Check for All port in range 0 to 1024\n '

        output_port=[]
        try:  #Exception Handling
            for port in ls:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((self.remoteServerIP, port))
                if result == 0:  #If port is open(i.e using this port we can connect to host )
                    print "Port {}: \t Open".format(port) #print port
                    output_port.append(port)
                sock.close() #close Socket

            print ' \n        We r Done!! \n '
            return output_port
                
                
        except KeyboardInterrupt:
            print "You pressed Ctrl+C"
            sys.exit()

        except socket.gaierror:
            print 'Hostname could not be resolved. Exiting'
            sys.exit()
        except socket.error:
            print "Couldn't connect to server"
            sys.exit()
            
