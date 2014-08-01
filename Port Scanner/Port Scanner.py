# ___________MAIN MODULE___________________
#  V-1.02
# Port Scanner 
__author__ = "Sudhanshu Patel (sudhanshuptl13@gmail.com)"

import sys
try:
    sys.path.insert(0,'sub_program')
    import scport
    import filehand
except:
    print 'Unable to Find subprogram folder or scport.py'

if __name__=='__main__':
     # Information for User
    print "Enter a remote host to scane Ex:- www.nitrkl.ac.in\n"+"-"*60
    print (" "*29)+"OR\n"+"_"*60
    print "Enter a remote computer name in your local network  Ex:- Sudhanshu\n"+"-"*60

    while True:
        try:
            print """
            1 ::- Scan remote Host for most common used Port
            2 ::- Brute Scan : Scan host for all port in range 0 to 1024
            3 ::- Scan remote host for port you want (you have to enter port)
            4 ::- Exit !!
         """
            choice=raw_input('Enter Your Choice ::- ')
            if choice=='1':
                ob=scport.Portscan(raw_input('Enter Remote Host name :- '))
                ls=ob.Scan_port()
            #we use ls for to store it in file
                st='''
                       We Search your Given remoteHost ..
                       for most common port that are used by many server
                '''
                fh=filehand.File_handling('Result Most common port.txt',st)
                if len(ls)>2: #if any port found
                    fh.f_do_it(ls)
                else:
                    ls.append('No Port Open Port Found or  Remote host Not found')
                    fh.f_do_it(ls)
                    
                print '***See Summary of result in "Result Most common port.txt" file***'
            
            elif choice=='2':
                ob=scport.Portscan(raw_input('Enter Remote Host name :- '))
                ls=ob.Brute_scan()
                
                st='''
                       We Search your Given remoteHost ..
                       for All Open Port in range 1 to 1024
                '''
                fh=filehand.File_handling('Result Brute scan.txt',st)
                if len(ls)>2: #if any port found
                    fh.f_do_it(ls)
                else:
                    ls.append('No Port Open Port Found or  Remote host Not found')
                    fh.f_do_it(ls)
                    
                print '***See Summary of result in "Result Brute port.txt" file***'

            
            elif choice=='3':
                print 'Enter port address seperated by space on which scan is going to perform :'
                ls=[int(x) for x in raw_input().split(' ')]
                ob=scport.Portscan(raw_input('Enter Remote Host name :- '),ls)
                ls= ob.Scan_port()

                st='''
                       We Search your Given remoteHost ..
                       for All  Port Given By You
                '''
                fh=filehand.File_handling('Result your Port.txt',st)
                if len(ls)>2: #if any port found
                    fh.f_do_it(ls)
                else:
                    ls.append('No Port Open Port Found or  Remote host Not found')
                    fh.f_do_it(ls)
                    
                print '***See Summary of result in "Result your Port.txt" file***'

        
            
            elif choice=='4':
                print 'Thank You !'
                sys.exit()
            
            else:
                print "Wrong Choice Try again"
        
        except KeyboardInterrupt:
            print 'You Pressed Ctrl+C'
            sys.exit()
 

