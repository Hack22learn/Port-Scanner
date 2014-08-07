from datetime import datetime
import socket,sys 

class Portscan():
    # Some of most common port is default argument
    def __init__(self,remoteServer,df_list=[21, 22, 23, 25, 53, 53, 80, 110, 111,119, 123, 135, 139, 143, 161, 443, 445,465,563,587,902,912,993,995, 1024, 1723, 3389, 4567, 5000,5631, 8080, 8081,9601]):
        '''Initiate port scanner'''
        self.remoteServer=remoteServer
        self._port_ls= df_list
        try:
            self.remoteServerIP=socket.gethostbyname(remoteServer) #Resolving IP of host
            print '*'*80
            print '          Host ;-     "',remoteServer,'"      and its IP :-   "',self.remoteServerIP,'"'
            print '*'*80
        except:
            print "Unable to fetch Host"
            self.remoteServerIP='Not Found'
           #sys.exit() #we need to detroy object we have to find out a way to do this
            

    def Scan_port(self):
        '''
           We check for all commonly used  port .....
        '''
        print "................Be Patience , it will take time.................."
        print '..........We check for some commonly used Port ....'

        output_port=[self.remoteServer,str(self.remoteServerIP)] #Use in file_handler module
        
        try:  #Exception Handling
            if self.remoteServerIP != 'Not Found':
                for port in self._port_ls:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		    sock.settimeout(0.1)
                    result = sock.connect_ex((self.remoteServerIP, port))
                    if result == 0:  #If port is open(i.e using this port we can connect to host )
                        print "port -> %s Open\n"%port
                        output_port.append(port)
    
                    sock.close() #close Socket

                print ' \n        We r Done!!  '
                return output_port
            else:
                print 'Unable to Fetch host'
                
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
           We check for all commonly used  port .....
        '''
        print "................Be Patience , it will take time.................."
        print '..........We check for some commonly used Port ....'

        output_port=[self.remoteServer,str(self.remoteServerIP)] #Use in file_handler module
        
        try:  #Exception Handling
            if self.remoteServerIP != 'Not Found':
                for port in xrange(1,1025):
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		    sock.settimeout(0.1)
                    result = sock.connect_ex((self.remoteServerIP, port))
                    if result == 0:  #If port is open(i.e using this port we can connect to host )
                        print "port -> %s Open\n"%port
                        output_port.append(port)
			
                    sock.close() #close Socket

                print ' \n        We r Done!!  '
                return output_port
            else:
                print 'Unable to Fetch host'
                
        except KeyboardInterrupt:
            print "You pressed Ctrl+C"
            sys.exit()

        except socket.gaierror:
            print 'Hostname could not be resolved. Exiting'
            sys.exit()
        except socket.error:
            print "Couldn't connect to server"
            sys.exit()
   
