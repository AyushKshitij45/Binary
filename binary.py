# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 23:17:02 2020

@author: admin
"""

#TODO:add comments
#TODO: Change dick to item
#TODO: Comment read block out

import pickle


example_list=[]
example_dict=dict()

class UnacceptedValueError(Exception): 

    def __init__(self,data):
        self.data=data
    
    def __str__(self):
        return repr(self.data)
    

class NoValueError(Exception): 

    def __init__(self):
        pass
    
    def __str__(self):
        pass    
"""
#Binary write list/dictionary
with open('file.bin','wb') as file:
    
    
    
    opt='y'
    while opt=='y':
        
        try:
            dicty= input('What do you want to write? ')  
            
            example_list.append(dicty)
            example_dict= dict(enumerate(example_list))
            opt=str(input('''Do you want to add more items?, ({} for {}, {} for {}): '''.format('y','yes','n','no')))        
            
            acceptedResponses=['y','n']
            if opt not in acceptedResponses:
                raise UnacceptedValueError("Please enter {}/{}".format('y','n'))
        
        except UnacceptedValueError as e:
            print(e)
            opt=str(input('''Do you want to add more items?, ({} for {}, {} for {}): '''.format('y','yes','n','no'))) 
            
        except Exception as e:
            print(e)
        
    pickle.dump(example_dict,file)
                  
    file.close()
"""    
"""    
#Binary write list/dictionary
with open('file.bin','wb') as file:
    
    
    
    opt='y'
    while opt=='y':
        
        try:
            Name= input('Name of student: ')
            rollNo= input("Student's Roll No.: ")

            example_dict['Name:']=Name            
            example_dict['Roll No.:']=rollNo
        
            
#            example_dict= dict(enumerate(example_list))
            opt=str(input('''Do you want to add more items?, ({} for {}, {} for {}): '''.format('y','yes','n','no')))        
            
            pickle.dump(example_dict,file)
            
            acceptedResponses=['y','n']
            if opt not in acceptedResponses:
                raise UnacceptedValueError("Please enter {}/{}".format('y','n'))
                        
        except UnacceptedValueError as e:
            print(e)
            opt=str(input('''Do you want to add more items?, ({} for {}, {} for {}): '''.format('y','yes','n','no'))) 
            
        except Exception as e:
            print(e)
        
    
                  
    file.close()
"""    
           
#binary read(to be commented)
with open('file.bin','rb') as file:
    
    i=0    
    try:
        searchedName=input('Enter name of the student (Press "Enter" to view the full file) : ')
        
        
        while True:
            example_dict=pickle.load(file)
            
            if searchedName == '':
                print('Records: ' )
                print(example_dict)
                i=1
            elif example_dict['Name:'] == searchedName:
                print('Records: ' )
                print(example_dict)
                i=1
    except EOFError:
        file.close()
        
    except Exception as e:
        print(e)
    
    if i==0:
        print('No one by that name')
        
                    
#    except NoValueError:
#        print('No one by that name')            
            

     