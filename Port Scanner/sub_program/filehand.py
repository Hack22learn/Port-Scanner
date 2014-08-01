
class File_handling():
    '''
           File handling module used to save data of open port in text file 
    '''
    def __init__(self,name="Result Port-scanner.txt",st='Result of Port Sacn'):
        self.fname=name
        self.info=st

    def f_do_it(self,ls):
        '''
          Create a text file and Store data about host its IP Address and list of open port
       '''
        f=open(self.fname,'w')
        f.write('\t Host name :-'+str(ls[0])+'\t\t IP Address :- '+str(ls[1]))
        f.write('\n\n'+self.info+'\n\n')
        f.write('\t\t\tList Of Open Port \n\t\t\t')
        count =0
        for i in range(2,len(ls)):
            if count <=5:
                f.write(str(ls[i])+' , ')
                count +=1
            else:
                count=0
                f.write('\n\t\t\t'+str(ls[i])+' , ')
                
        f.close() #close file
            
                

        
