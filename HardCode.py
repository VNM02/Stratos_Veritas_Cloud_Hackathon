import os
import csv
from cryptography.fernet import Fernet
import random
import pathlib
import pandas as pd 
import shutil
#'E:\Veritas\Files/'
vec = os.listdir('E:\Veritas\Files/')
print(vec)

data_frame=pd.DataFrame(columns=['File','Key','Node'])

location=["D:\\NODE1" , "D:\\NODE2" , "D:\\NODE3"]

for x in vec:
    key = Fernet.generate_key()
    fernet = Fernet(key)  
    with open(x, 'rb') as file:
        original = file.read()

    with open('E:\Veritas\hash.key', 'wb') as filekey:
        filekey.write(key)

    encrypted = fernet.encrypt(original)

    with open(x, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
     
    l=len(location)
    node=random.randint(0,2)
    
    data=[]
    pa=os.path.abspath(x)
    # data.append(pa)
    print(os.path.abspath(x))
    data.append(key)
    # print(key)
    data.append(node)
    # print(node)
    with open('Table.csv', 'a', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        f.close()
        print(data)    
    
    shutil.move(pa, location[node])   
    print("Success!!!")

        
