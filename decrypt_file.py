import os
import csv
from cryptography.fernet import Fernet

import pandas as pd 
import shutil
location = [os.getcwd() + "/NODE1", os.getcwd() + "/NODE2", os.getcwd() + "/NODE3"]
with open('Table.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    list_of_csv = list(csv_reader)
    print(len(list_of_csv))
print(list_of_csv)
for i in range(0, len(list_of_csv)):
    if(1):
        print("i :: {} ".format(i))
        curr_node_num = int(list_of_csv[i][2])
        print(curr_node_num)
        # print(curr_node_num + type(curr_node_num))
        # print(curr_node_num)
        pa = location[curr_node_num]
        file_path = list_of_csv[i][0].split('/')
        print("FILE PATH: ",file_path)
        # rev_list = file_path.split('\\').reverse()
        # file_name = file_path[2] #TODO this needs to be generalised
            # // get the file name from the file_path
        print("file_path: ",file_path)
        file_name = file_path[len(file_path) - 1]

        key = list_of_csv[i][1]
        print("key: ",key)
        fernet = Fernet(bytes(key, 'utf-8'))
        print(file_name)
        # print(
        #       pa + "/"+file_name
        # )
        with open(
              pa + "/" +file_name
            , 'rb') as file:
            original = file.read()
            print("original: ",original)
        decrypted = fernet.decrypt(original)
        with open(
              pa + "/" +file_name
            , 'wb') as decrypted_file:
            decrypted_file.write(decrypted)
        shutil.move(
            pa + "/" +file_name,os.getcwd() + "/Files/" )
        print("Succesfully decrypted {}".format(file_name))
        print(i)
