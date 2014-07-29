# ___________MAIN MODULE___________________
#  V-1.1
# Port Scanner 
__author__ = "Sudhanshu Patel (sudhanshuptl13@gmail.com)"

import sys
try:
    sys.path.insert(0,'sub_program')
    import scport
except:
    print 'Unable to Find subprogram folder or scport.py'

if __name__=='__main__':
     # Information for User
    print "Enter a remote host to scane Ex:- www.nitrkl.ac.in\n"+"-"*60
    print (" "*29)+"OR\n"+"_"*60
    print "Enter a remote computer name in your local network  Ex:- Sudhanshu\n"+"-"*60

    while True:
        print """
                1 ::- Scan remote Host for most common used Port
                2 ::- Brute Scan : Scan host for all port in range 0 to 1024
                3 ::- Scan remote host for port you want (you have to enter port)
                4 ::- Exit !!
                 """
        choice=raw_input('Enter Your Choice ::- ')
        if choice=='1':
            ob=scport.Portscan(raw_input('Enter Remote Host name :- '))
            ls=ob.Scan_common_port()
            #we use ls for to store it in file
            
        elif choice=='2':
            ob=scport.Portscan(raw_input('Enter Remote Host name :- '))
            ls=ob.Brute_scan()
            
        elif choice=='3':
            ob=scport.Portscan(raw_input('Enter Remote Host name :- '))
            print 'Enter port address seperated by space on which scan is going to perform :'
            ls= ob.Given_Portscan([int(x) for x in raw_input().split(' ')])
            
        elif choice=='4':
            print 'Thank You !'
            sys.exit()
            
        else:
            print "Wrong Choice Try again"
        
       
 

