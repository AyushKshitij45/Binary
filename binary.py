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

#Binary write list/dictionary
with open('file.bin','wb') as file:
    
    
    
    opt='y'
    while opt=='y':
        
        try:
            
        
            dick= input('What do you want to write? ')  
            
            example_list.append(dick)
            example_dict= dict(enumerate(example_list))
            print(example_dict)
            opt=str(input('''Do you want to add more items?, ({} for {}, {} for {}): '''.format('y','yes','n','no')))        
            
            acceptedResponses=['y','n']
            
            if opt not in acceptedResponses:
                raise UnacceptedValueError("Please enter {}/{}".format('y','n'))
        
        except UnacceptedValueError as e:
            print(e)
            opt=str(input('''Do you want to add more items?, ({} for {}, {} for {}): '''.format('y','yes','n','no')))        
        
    pickle.dump(example_dict,file)
           
        
    file.close()
           

with open('file.bin','rb') as file:
    
    
    
    try:
        print('Records are:' )
        
        while True:
            example_dict=pickle.load(file)
            print(example_dict)
            
    except EOFError:
        file.close()
        
    except Exception as e:
        print(e)
     