import os
import csv
from cryptography.fernet import Fernet
import random
import pathlib

vec = os.listdir('E:\Veritas\Files/')
print(vec)

header = ['Name_of_File', 'Key', 'Node']

with open('Table.csv', 'a', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    f.close()
location=["D:\\NODE1" , "D:\\NODE2" , "D:\\NODE3"]

for x in vec:
    key = Fernet.generate_key()
    fernet = Fernet(key)  
    with open(x, 'rb') as file:
        original = file.read()

    with open('D:\C++\hash.key', 'wb') as filekey:
        filekey.write(key)

    encrypted = fernet.encrypt(original)

    with open(x, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
     
    l=len(location)
    node=random.randint(0,l-1)
    
    data=[]
    pa=os.path.abspath(x)
    data.append((os.path.basename(pa).split('/')[-1]))
    print(os.path.abspath(x))
    data.append(key)
    data.append(node)
    
    with open('Table.csv', 'a', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        f.close()
        print(data)
        
